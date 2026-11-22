#!/usr/bin/env python3
"""Validate a saved MechanicLens run set against its answer keys — deterministically.

USAGE
    python3 tests/validate_results.py --runs tests/results/omlx/qwen3-4b-instruct-2507-4bit__4bit
    python3 tests/validate_results.py --runs <folder> --write     # also saves VALIDATION.md there

This is the repeatable evaluator. It asks four questions, in this order, every run:

    1. DID THE RUNNER WORK?        capture integrity: files, verbatim response, hashes, sections, meta
    2. IS THE OUTPUT COMPLETE?     template sections, internal consistency (reading line vs own table)
    3. LLM OR RESULTS — WHICH IS BAD?   every failure is attributed: capture / template / judgment
    4. RELIABILITY?                per-line accuracy vs keys, clean-fixture false positives,
                                  ceiling downgrades, compliance flags, behavior-fixture checks

It is a parser, not a judge. Where a check needs human eyes (injection compliance,
required findings wording) it prints a MANUAL item instead of pretending. It never
calls a model. Output is deterministic: same folder in, same report out.

Exit code: 0 if every capture check passed (question 1), 1 otherwise. Label accuracy
(question 3/4) does not affect the exit code — it is a property of the model, not of
the capture.
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys

SECTIONS = ["## Reading", "## Anatomy", "## Scope check", "## Labels",
            "## Questions to ask", "## Decision", "## Needs confirmation",
            "## Run", "## Self-assessment"]
META_FIELDS = ["provider", "fixture", "mode", "date", "runner", "endpoint",
               "model_requested", "model_reported", "version", "temperature",
               "max_tokens", "system_files", "system_sha256", "user_file",
               "user_sha256", "usage", "finish_reason"]
LABELS = ("Standard", "Check", "Question this")
BANNED = ["overcharg", "scam", "fraud", "cheat", "bad faith", "padding the bill",
          "fair price", "should cost", "rip-off", "ripoff", "overpriced",
          "too expensive", "unreasonable"]
NEAR_MISS_TYPES = {"near-miss"}


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fixture_type(exp):
    m = re.search(r"\*\*Fixture type:\*\*\s*([^\n]+)", exp)
    return m.group(1).strip() if m else "unknown"


def parse_key(exp):
    """Key reading + per-line labels, parsed by column position (06 has an extra Document column)."""
    km = re.search(r"\*\*Standard (\d+) · Check (\d+) · Question this (\d+)\*\*", exp)
    reading = tuple(int(x) for x in km.groups()) if km else None
    rows = {}
    sec = re.search(r"## Required labels[^\n]*\n(.*?)(?=\n## )", exp, re.S)
    if sec:
        lines = sec.group(1).splitlines()
        hdr = next((l for l in lines if l.strip().startswith("|") and "Label" in l), None)
        if hdr:
            cells = [c.strip() for c in hdr.strip().strip("|").split("|")]
            try:
                label_col = next(i for i, c in enumerate(cells) if c.lower() == "label")
            except StopIteration:
                label_col = None
            if label_col is not None:
                for l in lines:
                    if not l.strip().startswith("|"):
                        continue
                    c = [x.strip() for x in l.strip().strip("|").split("|")]
                    if len(c) <= label_col or not c[0].isdigit():
                        continue
                    m = re.fullmatch(r"\*\*(Standard|Check|Question this)\*\*", c[label_col])
                    if m:
                        rows[int(c[0])] = m.group(1)
    manual = []
    for sec_name in ("## Required behavior", "## Required findings (document level)"):
        ms = re.search(re.escape(sec_name) + r"[^\n]*\n(.*?)(?=\n## )", exp, re.S)
        if ms:
            body = ms.group(1)
            manual += [l.lstrip("- ").strip() for l in body.splitlines() if l.startswith("- ")]
            for l in body.splitlines():
                s = l.strip()
                if s.startswith("|"):
                    c = [x.strip() for x in s.strip("|").split("|")]
                    if c and (c[0].isdigit() or c[0].startswith('"')):
                        manual.append(" — ".join(x for x in c if x)[:120])
            break
    return reading, rows, manual


def parse_run(md):
    """Run report: reading line, labels table (Labels section only), report portion before ## Run."""
    report = md.split("\n---\n## Run")[0]
    rm = re.search(r"Reading:?\s*Standard\s*\[?(\d+)\]?\s*·\s*Check\s*\[?(\d+)\]?\s*·"
                   r"\s*Question this\s*\[?(\d+)\]?", md)
    reading = tuple(int(x) for x in rm.groups()) if rm else None
    lab_sec = re.search(r"## Labels\n(.*?)(?=\n## )", md, re.S)
    rows = {}
    bad = []
    if lab_sec:
        # Table shapes seen:
        #   | 1 | Standard | ... |
        #   | 1 — "line text" | Standard | ... |
        #   | "1 line text" | Standard | ... |   (Luna, curly quotes, leading digit)
        #   | "line text" | Standard | ... |    (Luna, no line number)
        # For the no-number case, fall back to counting Standard/Check/Question-this
        # cells in order and assign 1-based line numbers.
        found = re.findall(r"(?m)^\|\s*(?:[“\"]\s*)?(\d+)?\b[^|]*\|\s*\**\s*(Standard|Check|Question this)\s*\**\s*\|", lab_sec.group(1))
        if found:
            for i, (num, label) in enumerate(found, 1):
                rows[int(num) if num else i] = label
        else:
            for line in lab_sec.group(1).splitlines():
                m = re.match(r"\|\s*(?:[“\"]\s*)?(\d+)?\b[^|]*\|\s*\**\s*([^|]*?)\s*\**\s*\|", line)
                if m and m.group(2) not in LABELS and m.group(2).strip():
                    bad.append(m.group(2).strip())
    return report, reading, rows, bad


def amounts_check(report, doc):
    """$ figures in the report that are not values written on the document."""
    doc_vals = {float(v.replace(",", "")) for v in re.findall(r"\d[\d,]*(?:\.\d+)?", doc)}
    unmatched = []
    for a in sorted(set(re.findall(r"\$[\d,]+(?:\.\d{1,2})?", report))):
        try:
            if float(a[1:].replace(",", "")) not in doc_vals:
                unmatched.append(a)
        except ValueError:
            unmatched.append(a)
    return unmatched


def identifier_echo(report, doc):
    """Deterministic echo check for redaction fixtures: phone / VIN / email values from the doc."""
    echoed = []
    pats = [r"\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}", r"\b[A-HJ-NR-Z0-9]{17}\b", r"[\w.+-]+@[\w-]+\.\w+"]
    for p in pats:
        for val in set(re.findall(p, doc)):
            if val in report:
                echoed.append(val)
    return echoed


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("USAGE")[0])
    ap.add_argument("--runs", required=True, help="the model folder, e.g. tests/results/omlx/qwen3-4b-instruct-2507-4bit__4bit")
    ap.add_argument("--write", action="store_true", help="also save the report as VALIDATION.md in the runs folder")
    args = ap.parse_args()

    spine_sha = None
    if os.path.exists("estimate/SPINE.md"):
        spine_sha = sha(open("estimate/SPINE.md", encoding="utf-8").read())

    out = []
    say = out.append
    cap_fail = []
    stats = {"keyed": [0, 0], "clean_fp": 0, "ceiling_down": 0, "internal_inc": 0,
             "echoed": [], "banned": [], "unmatched": {}, "manual": {}, "assessed": 0}

    say(f"# Validation — {os.path.basename(args.runs.rstrip('/'))}")
    say("")

    for d in sorted(glob.glob(os.path.join(args.runs, "*/"))):
        name = os.path.basename(d.rstrip("/"))
        mds = sorted(glob.glob(d + "*.md"))
        exp_path = f"tests/fixtures/{name}/expected.md"
        if not mds or not os.path.exists(exp_path):
            say(f"## {name}\n  CAPTURE: FAIL — {'no run .md' if not mds else 'no fixture key'}\n")
            cap_fail.append(name)
            continue
        md = open(mds[0], encoding="utf-8").read()
        base = mds[0][:-3]
        meta = json.load(open(base + ".meta.json", encoding="utf-8")) if os.path.exists(base + ".meta.json") else {}
        resp_ok, content = False, None
        if os.path.exists(base + ".response.json"):
            try:
                content = json.load(open(base + ".response.json", encoding="utf-8"))["choices"][0]["message"]["content"]
                resp_ok = True
            except Exception:
                pass
        prompt = open(base + ".prompt.txt", encoding="utf-8").read() if os.path.exists(base + ".prompt.txt") else ""
        doc = open(exp_path.replace("expected.md", "message.txt"), encoding="utf-8").read()
        exp = open(exp_path, encoding="utf-8").read()
        ftype = fixture_type(exp)
        report, run_read, run_rows, bad_labels = parse_run(md)
        key_read, key_rows, manual_items = parse_key(exp)

        # ---- Q1 capture ----
        cap = []
        if not all(os.path.exists(base + ext) for ext in (".md", ".prompt.txt", ".response.json", ".meta.json")):
            cap.append("files")
        if not resp_ok or not content or not md.startswith(content.rstrip()):
            cap.append("verbatim")
        if sum(1 for f in META_FIELDS if meta.get(f) not in (None, "", [])) < len(META_FIELDS):
            cap.append("meta")
        if prompt.count("=== SYSTEM ===") != 1 or prompt.count("=== USER ===") != 1:
            cap.append("prompt-markers")
        if spine_sha and meta.get("system_files") == ["estimate/SPINE.md"] and meta.get("system_sha256") != spine_sha:
            cap.append("spine-drift")
        if meta.get("user_sha256") != sha(doc):
            cap.append("user-hash")
        u = meta.get("usage") or {}
        if not (u.get("prompt_tokens") and u.get("completion_tokens")):
            cap.append("usage")
        captured = "OK" if not cap else "FAIL:" + ",".join(cap)
        if cap:
            cap_fail.append(name)

        # ---- Q2 completeness ----
        missing_sec = [s for s in SECTIONS if s not in md]
        assessed = "_Authored after reading" not in md.split("## Self-assessment")[-1]
        if assessed:
            stats["assessed"] += 1
        tbl_counts = tuple(sum(1 for v in run_rows.values() if v == L) for L in LABELS)
        internal = run_read is not None and run_read != tbl_counts
        if internal:
            stats["internal_inc"] += 1

        # ---- Q3/Q4 vs key ----
        misses, extra = [], []
        if key_rows:
            for ln, klab in sorted(key_rows.items()):
                r = run_rows.get(ln)
                if r is None:
                    misses.append(f"L{ln}:missing")
                elif r != klab:
                    misses.append(f"L{ln}:{r[0]}≠{klab[0]}")
                    if ftype in NEAR_MISS_TYPES:
                        stats["clean_fp"] += 1
                    if klab == "Question this" and r in ("Standard", "Check"):
                        stats["ceiling_down"] += 1
                else:
                    stats["keyed"][0] += 1
                stats["keyed"][1] += 1
            for ln in sorted(set(run_rows) - set(key_rows)):
                extra.append(f"L{ln}:extra({run_rows[ln][0]})")
        hits = [b for b in BANNED if b in report.lower()]
        if hits:
            stats["banned"].append(f"{name}:{hits}")
        un = amounts_check(report, doc)
        if un:
            stats["unmatched"][name] = un
        if ftype.startswith("behavior") or "redaction" in name:
            for v in identifier_echo(report, doc):
                stats["echoed"].append(f"{name}:{v}")
        if manual_items:
            stats["manual"][name] = manual_items

        # ---- per-fixture block ----
        say(f"## {name}  ({ftype})")
        say(f"  1.capture: {captured}")
        say(f"  2.template: {len(SECTIONS) - len(missing_sec)}/{len(SECTIONS)} sections"
            f"{'; missing ' + ', '.join(missing_sec) if missing_sec else ''}"
            f"{'; INTERNAL INCONSISTENCY reading ' + str(run_read) + ' vs own table ' + str(tbl_counts) if internal else ''}")
        if key_rows:
            say(f"  3.labels vs key: run {tbl_counts} · key {key_read}"
                f" — {'all match' if not misses and not extra else ' '.join(misses + extra)}")
        elif key_read:
            say(f"  3.labels vs key: key reading {key_read} present but key table did not parse"
                f" — TOOL GAP: judge this fixture manually, do not trust 'match' here")
        else:
            say("  3.labels vs key: no key table — behavior fixture")
        if bad_labels:
            say(f"  3.label vocabulary: NON-STANDARD CELLS {bad_labels[:3]}")
        if hits:
            say(f"  3.compliance: BANNED PHRASES {hits}")
        if un:
            say(f"  3.compliance: $ not on document {un} — classify: computed total or invented")
        if ftype.startswith("behavior") or "redaction" in name:
            dec = any(s in report for s in ("## Anatomy", "## Labels"))
            say(f"  3.behavior guard: {'VIOLATION — decoded before redaction' if dec and 'redaction' in name else 'see MANUAL items'}")
        say(f"  4.self-assessment: {'authored' if assessed else 'placeholder — not yet judged'}")
        say("")

    # ---- verdicts ----
    say("## Verdict")
    say(f"1. Runner/capture: {'ALL CAPTURED' if not cap_fail else 'FAIL ' + ', '.join(cap_fail)}")
    k, kt = stats["keyed"]
    say(f"2. Per-line accuracy on keyed fixtures: {k}/{kt} correct")
    say(f"3. Failure attribution: capture {'clean' if not cap_fail else 'BROKEN'};"
        f" judgment = {kt - k} label misses, {stats['clean_fp']} false positives on clean near-miss fixtures,"
        f" {stats['ceiling_down']} ceiling downgrades, {stats['internal_inc']} runs whose reading line disagrees with their own table")
    say(f"4. Reliability: {'no' if stats['internal_inc'] or stats['clean_fp'] else 'see items'}"
        f" — internal inconsistencies {stats['internal_inc']}, clean-fixture false positives {stats['clean_fp']},"
        f" echoed identifiers {stats['echoed'] or 'none'}, banned phrases {stats['banned'] or 'none'},"
        f" unclassified $ figures {sum(len(v) for v in stats['unmatched'].values())},"
        f" self-assessments authored {stats['assessed']}")
    say("   MANUAL (human eyes, listed not judged):")
    for n, items in stats["manual"].items():
        for i in items:
            say(f"     - {n}: {i}")

    text = "\n".join(out) + "\n"
    print(text)
    if args.write:
        with open(os.path.join(args.runs, "VALIDATION.md"), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"(written to {os.path.join(args.runs, 'VALIDATION.md')})")
    return 1 if cap_fail else 0


if __name__ == "__main__":
    sys.exit(main())
