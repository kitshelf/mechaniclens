#!/usr/bin/env python3
"""Run the fixture gauntlet against a local or hosted OpenAI-compatible model.

Every run captures three files in one folder, so the exchange is auditable
byte for byte:

    tests/results/<model-slug>/<fixture>/<date>-<mode>.md          report + Run block
    tests/results/<model-slug>/<fixture>/<date>-<mode>.prompt.txt   exact input sent
    tests/results/<model-slug>/<fixture>/<date>-<mode>.meta.json    hashes, model id, settings, usage

The `.md` holds the model's FULL response. The `.prompt.txt` holds the exact
system and user text. The `.meta.json` holds the sha256 of both, the model id
the server reported, and the request settings — so a reader can prove which
input produced which output without trusting the note at the top.

The `## Self-assessment` block is authored by a reader afterwards. A script
cannot judge, and a generated "PASS" is not evidence.

Modes:
  quick (default) — estimate/SPINE.md + message.txt   (the two-paste path users get)
  full            — 00-principles, labels, anatomy, document-types, redaction,
                    rubric, estimate.md + message.txt

Local endpoint (oMLX / Ollama / LM Studio) by default. Pass --base-url and
--api-key-env for a hosted provider such as OpenRouter. The key is read from
the environment and never written to a result file.

    python3 tests/run_local.py --model Qwen3.5-9B-MLX-4bit
    python3 tests/run_local.py --model Qwen3.5-4B-4bit --fixtures 07,14,15
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

DEFAULT_BASE = "http://127.0.0.1:8000/v1/chat/completions"

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
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--api-key-env", default=None, help="env var holding the provider key (hosted runs)")
    ap.add_argument("--mode", choices=["quick", "full"], default="quick")
    ap.add_argument("--fixtures", default="all")
    ap.add_argument("--out", default="tests/results")
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--max-tokens", type=int, default=2400)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--runner", default="unattributed")
    args = ap.parse_args()

    headers = {"Content-Type": "application/json"}
    if args.api_key_env:
        key = os.environ.get(args.api_key_env)
        if not key:
            raise SystemExit(f"{args.api_key_env} is not set — cannot run a hosted model")
        headers["Authorization"] = f"Bearer {key}"
        headers["HTTP-Referer"] = "https://github.com/kitshelf/mechaniclens"
        headers["X-Title"] = "MechanicLens fixture run"

    system_parts = build_system(args.mode)
    system = "".join(f"\n\n<!-- {p} -->\n\n{t}" for p, t in system_parts) if len(system_parts) > 1 else system_parts[0][1]
    today = datetime.date.today().isoformat()
    model_slug = slug(args.model)
    endpoint_host = re.sub(r"^https?://([^/]+).*$", r"\1", args.base_url)

    failures = 0
    for d in pick_fixtures(args.fixtures):
        name = os.path.basename(d.rstrip("/"))
        msg_path = os.path.join(d, "message.txt")
        user = open(msg_path, encoding="utf-8").read()
        body = json.dumps({
            "model": args.model,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
        }).encode()
        req = urllib.request.Request(args.base_url, data=body, headers=headers)

        print(f"\n### {name}")
        try:
            with urllib.request.urlopen(req, timeout=args.timeout) as r:
                payload = json.loads(r.read())
            out = payload["choices"][0]["message"]["content"]
        except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
            failures += 1
            print(f"  ERROR: {e}")
            continue

        out_dir = os.path.join(args.out, model_slug, name)
        os.makedirs(out_dir, exist_ok=True)
        base_name = f"{today}-{args.mode}"

        # 1. exact input
        with open(os.path.join(out_dir, base_name + ".prompt.txt"), "w", encoding="utf-8") as f:
            f.write(f"<!-- mode {args.mode} · fixtures {name} · recorded {today} -->\n")
            f.write("=== SYSTEM ===\n" + system + "\n=== USER ===\n" + user)

        # 2. output + run block
        with open(os.path.join(out_dir, base_name + ".md"), "w", encoding="utf-8") as f:
            f.write(out.rstrip() + "\n\n---\n## Run\n")
            f.write(f"- Model requested: `{args.model}`\n")
            f.write(f"- Model reported: `{payload.get('model', 'not returned')}`\n")
            f.write(f"- Endpoint: {endpoint_host} · mode {args.mode} · temperature {args.temperature}"
                    f" · max_tokens {args.max_tokens}\n")
            f.write(f"- Runner: {args.runner} · Recorded: {today}\n")
            f.write(f"- Input sha256: system `{sha(system)[:16]}…` · user `{sha(user)[:16]}…` "
                    f"(full text in `{base_name}.prompt.txt`)\n\n")
            f.write("## Self-assessment\n_Authored after reading the report above against "
                    "`expected.md`. Not generated._\n")

        # 3. metadata
        meta = {
            "fixture": name,
            "mode": args.mode,
            "date": today,
            "runner": args.runner,
            "endpoint": endpoint_host,
            "model_requested": args.model,
            "model_reported": payload.get("model"),
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "system_files": [p for p, _ in system_parts],
            "system_sha256": sha(system),
            "user_file": msg_path,
            "user_sha256": sha(user),
            "usage": payload.get("usage"),
            "finish_reason": payload["choices"][0].get("finish_reason"),
            "output_file": base_name + ".md",
            "prompt_file": base_name + ".prompt.txt",
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
        print(f"  saved: {out_dir}/{base_name}.{{md,prompt.txt,meta.json}}")

    print("\nInputs, outputs, and metadata saved. Author a Self-assessment in each .md before calling a fixture pass.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())