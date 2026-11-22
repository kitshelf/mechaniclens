#!/usr/bin/env python3
"""Fixture consistency check.

Every fixture must agree with its own answer key: the reading count must equal
the number of numbered line items, the key must label exactly those lines, and
the stated total must equal the lines plus the stated tax.

Fixture 11 is the deliberate exception — its arithmetic is wrong on purpose,
because that is the D-3 pattern it plants.

Read-only. Run from the kit root after adding or editing a fixture:

    python3 tests/verify_fixtures.py
"""

import glob
import os
import re

DIRS = sorted(glob.glob("tests/fixtures/*/"))
fails = []

for d in DIRS:
    if not os.path.isdir(d):
        continue
    name = os.path.basename(d.rstrip("/"))
    exp_path = os.path.join(d, "expected.md")
    msg_path = os.path.join(d, "message.txt")
    if not (os.path.exists(exp_path) and os.path.exists(msg_path)):
        fails.append(f"{name}: missing expected.md or message.txt")
        continue
    exp = open(exp_path, encoding="utf-8").read()
    msg = open(msg_path, encoding="utf-8").read()

    m = re.search(r"Standard (\d+) · Check (\d+) · Question this (\d+)", exp)
    if not m:
        # Behavior fixture: no single reading, but required-behavior steps and a
        # forbidden set are mandatory. A refusal-only key may carry no label rows;
        # a decode-conditional key may label only lines the document has.
        if "## Required behavior" not in exp:
            fails.append(f"{name}: behavior key has no Required behavior section")
        if "## Forbidden" not in exp:
            fails.append(f"{name}: behavior key has no Forbidden section")
        nums = [int(n) for n in re.findall(r"(?m)^\s*(\d+)\s{2,}", msg)]
        if re.search(r"(?m)^## Required labels", exp):
            key_rows = [int(x) for x in re.findall(r"(?m)^\|\s*(\d+)\s*\|", exp)]
            for k in key_rows:
                if k not in nums:
                    fails.append(f"{name}: decode key labels line {k}, document has {nums}")
        elif "## Required labels" in exp:
            fails.append(f"{name}: refusal-only key carries a Required labels section")
        print(f"{name}: behavior fixture — structure checked")
        continue
    s, c, q = map(int, m.groups())
    declared = s + c + q

    nums = [int(n) for n in re.findall(r"(?m)^\s*(\d+)\s{2,}", msg)]
    if len(nums) != declared:
        fails.append(f"{name}: key says {declared} lines ({s}/{c}/{q}), document has {len(nums)}")

    key_rows = [int(x) for x in re.findall(r"(?m)^\|\s*(\d+)\s*\|", exp)]
    if key_rows and sorted(key_rows) != sorted(nums):
        fails.append(f"{name}: key labels lines {sorted(key_rows)}, document has {nums}")

    for block in re.split(r"(?m)^===.*$", msg):
        if "TOTAL" not in block.upper():
            continue
        parts, tax = [], None
        for mm in re.finditer(r"(?m)^\s*(\d+)\s{2,}(.*)$", block):
            body = mm.group(2)
            amt = re.search(r"([\d,]+\.\d\d)\s*$", body)
            if not amt:
                continue
            val = float(amt.group(1).replace(",", ""))
            if "sales tax" in body.lower():
                tax = val
            elif "total" in body.lower():
                continue
            else:
                parts.append(val)
        stated_m = re.search(r"(?i)total\s*\.*\s*([\d,]+\.\d\d)", block)
        if tax is None or not stated_m:
            continue
        stated = float(stated_m.group(1).replace(",", ""))
        calc = round(sum(parts) + tax, 2)
        if abs(calc - stated) > 0.02:
            if name.startswith("11"):
                print(f"{name}: arithmetic off by design (D-3) — lines {sum(parts):.2f} "
                      f"+ tax {tax:.2f} = {calc:.2f}, stated {stated:.2f}")
            else:
                fails.append(f"{name}: arithmetic {calc:.2f} != stated {stated:.2f}")

print()
if fails:
    print("FAILURES:")
    for f in fails:
        print("  " + f)
    raise SystemExit(1)
print(f"all {len(DIRS)} fixtures consistent: counts, labeled lines, and arithmetic")