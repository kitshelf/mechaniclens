#!/usr/bin/env python3
"""MechanicLens fixture runner — run the synthetic gauntlet against a model.

USAGE

    # local (oMLX on :8000) — no key needed
    python3 tests/run_local.py --provider omlx --model Qwen3.5-9B-MLX-4bit --version 4bit

    # hosted (OpenRouter) — key read from env var OPENROUTER_API_KEY
    OPENROUTER_API_KEY=sk-... python3 tests/run_local.py \\
        --provider openrouter --model openai/gpt-6.2-sol --version latest \\
        --base-url https://openrouter.ai/api/v1/chat/completions

ARGUMENTS

    --llm / --model <id>   the model id exactly as the endpoint expects it
                           (required; --llm is the short alias for --model)
    --results <dir>        where the run is written (default tests/results)
    --provider <name>      endpoint provider: omlx | openrouter (default omlx)
    --version <ver>        model version/snapshot, e.g. 4bit, :free, 2026-11-15
                           (required for the path; default "unspecified")
    --mode quick|full      quick = SPINE.md + message (the two-paste path);
                           full = workflow files + rubric + message
    --fixtures all|01,07,… limit to specific fixtures (default all)

KEYS

    Local endpoints need no key. Hosted endpoints read their key from an env
    var — never a flag, never a file, never echoed: --api-key-env names it
    (default OPENROUTER_API_KEY for the openrouter provider). The key is used
    for the request and never written into any output file.

OUTPUT — one folder per provider/model/version, one per fixture; a run is
captured, not summarised. Four files per run:

    <results>/<provider>/<model>__<version>/<fixture>/<date>-<mode>.md
        the model's report + a ## Run block + an authored ## Self-assessment
    …/<date>-<mode>.prompt.txt     the EXACT input sent (system + user)
    …/<date>-<mode>.response.json the model's RAW response, verbatim, unedited
    …/<date>-<mode>.meta.json     provider, model requested + reported, version,
                                  hashes, settings, usage, finish reason

A folder with no .prompt.txt/.response.json/.meta.json beside the .md is a
summary, not evidence. The ## Self-assessment block is authored by a reader
afterwards; a script cannot judge, and a generated "PASS" is not evidence.
"""

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

PROVIDERS = {
    "omlx": "http://127.0.0.1:8000/v1/chat/completions",
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
}
KEY_ENV = {"openrouter": "OPENROUTER_API_KEY"}
FULL_MODE_FILES = [
    "estimate/00-principles.md",
    "shared/labels.md",
    "shared/anatomy.md",
    "shared/document-types.md",
    "shared/redaction.md",
    "estimate/rubrics/patterns-estimate.md",
    "estimate/01-estimate/estimate.md",
]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def pick_fixtures(spec):
    dirs = sorted(d for d in glob.glob("tests/fixtures/*/") if os.path.isdir(d))
    if spec in (None, "", "all"):
        return dirs
    chosen = []
    for want in [w.strip() for w in spec.split(",") if w.strip()]:
        for d in dirs:
            base = os.path.basename(d.rstrip("/"))
            if base == want or base.startswith(want.zfill(2)):
                chosen.append(d)
                break
        else:
            raise SystemExit(f"no fixture matches {want!r}")
    return chosen


def build_system(mode):
    if mode == "quick":
        return [("estimate/SPINE.md", open("estimate/SPINE.md", encoding="utf-8").read())]
    return [(p, open(p, encoding="utf-8").read()) for p in FULL_MODE_FILES]


def main():
    ap = argparse.ArgumentParser(
        description="Run the MechanicLens fixture gauntlet against a local or hosted model.",
        epilog=__doc__.split("OUTPUT")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--llm", "--model", dest="model", required=True,
                    help="model id exactly as the endpoint expects it (e.g. Qwen3.5-9B-MLX-4bit, openai/gpt-6.2-sol)")
    ap.add_argument("--results", dest="out", default="tests/results",
                    help="where the run is written (default tests/results)")
    ap.add_argument("--provider", default="omlx", choices=sorted(PROVIDERS),
                    help="endpoint provider (default omlx; openrouter needs a key)")
    ap.add_argument("--version", default="unspecified",
                    help="model version/snapshot for the path, e.g. 4bit, :free, 2026-11-15")
    ap.add_argument("--base-url", default=None, help="override the provider's default endpoint URL")
    ap.add_argument("--api-key-env", default=None,
                    help="env var holding the provider key (default: OPENROUTER_API_KEY when --provider openrouter)")
    ap.add_argument("--mode", choices=["quick", "full"], default="quick",
                    help="quick = SPINE.md + message; full = workflow files + rubric + message (default quick)")
    ap.add_argument("--fixtures", default="all", help='"all", or fixture numbers/ids, e.g. 07,14,15')
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--max-tokens", type=int, default=32000,
                    help="output token budget. Reasoning models (Qwen3.5-*) spend tokens in "
                         "reasoning_content before producing content; 2400 fits a non-reasoning "
                         "Instruct model but is too small for reasoning + answer. Default 32000 "
                         "(safe across all oMLX models; the smallest context window is 40960).")
    ap.add_argument("--timeout", type=int, default=0,
                    help="socket timeout in seconds; 0 = no timeout (wait indefinitely). "
                         "Reasoning models at high max_tokens can run for several minutes; "
                         "default 0 so a long run is not killed mid-answer.")
    ap.add_argument("--runner", default=os.environ.get("USER", "unattributed"),
                    help="who ran it, recorded in the metadata")
    args = ap.parse_args()

    if not os.path.exists("estimate/SPINE.md"):
        raise SystemExit("run me from the kit root (estimate/SPINE.md not found)")

    base_url = args.base_url or PROVIDERS[args.provider]
    key_env = args.api_key_env or KEY_ENV.get(args.provider)
    headers = {"Content-Type": "application/json"}
    if key_env:
        key = os.environ.get(key_env)
        if not key:
            raise SystemExit(f"{key_env} is not set — a key is required for the {args.provider} provider "
                             f"(env var only; never a flag)")
        headers["Authorization"] = f"Bearer {key}"
        headers["HTTP-Referer"] = "https://github.com/kitshelf/mechaniclens"
        headers["X-Title"] = "MechanicLens fixture run"

    system_parts = build_system(args.mode)
    system = system_parts[0][1] if len(system_parts) == 1 else \
        "".join(f"\n\n<!-- {p} -->\n\n{t}" for p, t in system_parts)

    today = datetime.date.today().isoformat()
    run_root = os.path.join(args.out, slug(args.provider), f"{slug(args.model)}__{slug(args.version)}")
    endpoint_host = re.sub(r"^https?://([^/]+).*$", r"\1", base_url)

    print(f"provider={args.provider} model={args.model} version={args.version} mode={args.mode}")
    print(f"endpoint={base_url} key={'required from ' + key_env if key_env else 'not needed'}")
    print(f"results={run_root}")

    failures = 0
    for d in pick_fixtures(args.fixtures):
        name = os.path.basename(d.rstrip("/"))
        user = open(os.path.join(d, "message.txt"), encoding="utf-8").read()
        body = json.dumps({
            "model": args.model,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
        }).encode()
        req = urllib.request.Request(base_url, data=body, headers=headers)

        print(f"\n### {name}")
        try:
            with urllib.request.urlopen(req, timeout=(args.timeout or None)) as r:
                raw = r.read()
            payload = json.loads(raw)
            choice = payload["choices"][0]
            message = choice["message"]
            out = message.get("content")
            reasoning = message.get("reasoning_content")
            finish = choice.get("finish_reason")
        except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
            failures += 1
            print(f"  ERROR: {e}")
            continue

        out_dir = os.path.join(run_root, name)
        os.makedirs(out_dir, exist_ok=True)
        base_name = f"{today}-{args.mode}"

        # Reasoning models can spend every token in reasoning_content and return
        # content=None with finish_reason="length". That is a budget failure,
        # not a crash. Record it as a failed run (response + meta, no report)
        # so it is evidenced, not swallowed by a KeyError.
        if not out:
            why = "ran out of tokens before producing an answer"
            if finish == "length":
                why += f" (finish_reason=length; reasoning_content {len(reasoning or '')} chars)"
            with open(os.path.join(out_dir, base_name + ".prompt.txt"), "w", encoding="utf-8") as f:
                f.write(f"<!-- provider {args.provider} · model {args.model} · version {args.version} "
                        f"· mode {args.mode} · recorded {today} -->\n")
                f.write("=== SYSTEM ===\n" + system + "\n=== USER ===\n" + user)
            with open(os.path.join(out_dir, base_name + ".response.json"), "w", encoding="utf-8") as f:
                f.write(raw.decode("utf-8", errors="replace"))
            meta = {
                "provider": args.provider, "fixture": name, "mode": args.mode,
                "date": today, "runner": args.runner, "endpoint": endpoint_host,
                "model_requested": args.model, "model_reported": payload.get("model"),
                "version": args.version, "temperature": args.temperature,
                "max_tokens": args.max_tokens, "system_files": [p for p, _ in system_parts],
                "system_sha256": sha(system),
                "user_file": f"tests/fixtures/{name}/message.txt", "user_sha256": sha(user),
                "usage": payload.get("usage"), "finish_reason": finish,
                "reasoning_content_chars": len(reasoning or ""),
                "status": "no_answer", "reason": why,
                "output_file": None, "prompt_file": base_name + ".prompt.txt",
                "response_file": base_name + ".response.json",
            }
            with open(os.path.join(out_dir, base_name + ".meta.json"), "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=2, sort_keys=True)
            print(f"  NO ANSWER: {why}")
            print(f"  saved: {out_dir}/{base_name}.{{prompt.txt,response.json,meta.json}} (no .md report)")
            continue

        with open(os.path.join(out_dir, base_name + ".prompt.txt"), "w", encoding="utf-8") as f:
            f.write(f"<!-- provider {args.provider} · model {args.model} · version {args.version} "
                    f"· mode {args.mode} · recorded {today} -->\n")
            f.write("=== SYSTEM ===\n" + system + "\n=== USER ===\n" + user)

        with open(os.path.join(out_dir, base_name + ".response.json"), "w", encoding="utf-8") as f:
            f.write(raw.decode("utf-8", errors="replace"))

        with open(os.path.join(out_dir, base_name + ".md"), "w", encoding="utf-8") as f:
            f.write(out.rstrip() + "\n\n---\n## Run\n")
            f.write(f"- Provider: {args.provider}\n")
            f.write(f"- Model requested: `{args.model}`\n")
            f.write(f"- Model reported: `{payload.get('model', 'not returned')}`\n")
            f.write(f"- Version: {args.version}\n")
            f.write(f"- Endpoint: {endpoint_host} · mode {args.mode} · temperature {args.temperature}"
                    f" · max_tokens {args.max_tokens}\n")
            f.write(f"- Runner: {args.runner} · Recorded: {today}\n")
            f.write(f"- Input sha256: system `{sha(system)[:16]}…` · user `{sha(user)[:16]}…` "
                    f"(full text in `{base_name}.prompt.txt`)\n")
            f.write(f"- Raw response: `{base_name}.response.json` — stored verbatim, unedited\n\n")
            f.write("## Self-assessment\n_Authored after reading the report above against "
                    "`expected.md`. Not generated._\n")

        meta = {
            "provider": args.provider,
            "fixture": name,
            "mode": args.mode,
            "date": today,
            "runner": args.runner,
            "endpoint": endpoint_host,
            "model_requested": args.model,
            "model_reported": payload.get("model"),
            "version": args.version,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "system_files": [p for p, _ in system_parts],
            "system_sha256": sha(system),
            "user_file": f"tests/fixtures/{name}/message.txt",
            "user_sha256": sha(user),
            "usage": payload.get("usage"),
            "finish_reason": payload["choices"][0].get("finish_reason"),
            "reasoning_content_chars": len(message.get("reasoning_content") or ""),
            "output_file": base_name + ".md",
            "prompt_file": base_name + ".prompt.txt",
            "response_file": base_name + ".response.json",
        }
        with open(os.path.join(out_dir, base_name + ".meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, sort_keys=True)

        reading = re.search(r"Reading:?\s*(Standard[^\n]*)", out)
        print("  reading:", reading.group(1).strip() if reading else "NOT FOUND")
        rows = re.findall(r"(?m)^\|\s*([^\n|]{0,60}?)\s*\|\s*\**\s*(Standard|Check|Question this)\s*\**", out)
        for line, label in rows[:14]:
            print(f"  {label:14} {line.strip()[:60]}")
        if not rows:
            print("  (no label table parsed — record as 'did not follow the template')")
        print(f"  saved: {out_dir}/{base_name}.{{md,prompt.txt,response.json,meta.json}}")

    print("\nInputs, raw responses, and metadata saved.")
    print("Author a Self-assessment in each .md before calling a fixture pass.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())