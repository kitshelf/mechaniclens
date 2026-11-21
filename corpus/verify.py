#!/usr/bin/env python3
"""Citation check for the pattern library.

The citation rule in estimate/rubrics/patterns-estimate.md says a dataset is
cited only for text it verifiably contains. This tool enforces that rule by
re-measuring the library's published claims against the vendored corpus:

  Section A re-checks the counts and quotes each cited dataset is claimed to
  carry. Pattern IDs are named per block.

  Section B hunts estimate vocabulary across every vendored data file, so a
  source strength (direct / adjacent / brief) is assigned from a command, not
  from memory.

Read-only. Never writes, fetches, or transmits anything. Run from the kit
root after any rubric change, then record the pass in corpus/TUNING.md:

    python3 corpus/verify.py

Noise the hunts deliberately exclude: vehicle speeds ("miles per hour"),
retailer branding ("Authorized Retailer"), recall-remedy disposal advice, and
all .md files (source cards and .md previews are documentation, not data).
"""

import csv
import json
import os
import re
from collections import Counter

C = "corpus"
DATA_EXT = (".json", ".jsonl", ".csv", ".tsv")
ROOT_SKIP = {"index.json"}


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def load_rows(path):
    if path.endswith(".jsonl"):
        return [json.loads(line) for line in read_text(path).splitlines() if line.strip()]
    if path.endswith(".json"):
        x = json.loads(read_text(path))
        if isinstance(x, list):
            return x
        if isinstance(x, dict):
            for key in ("rows", "data", "records", "items", "results", "codes"):
                if isinstance(x.get(key), list):
                    return x[key]
        return [x]
    if path.endswith((".csv", ".tsv")):
        with open(path, encoding="utf-8", errors="replace") as f:
            return list(csv.DictReader(f))
    return []


def data_files(dataset_dir):
    """Data files only: .json/.jsonl/.csv/.tsv. No README cards, no .md previews."""
    out = []
    for dirpath, _dirnames, filenames in os.walk(os.path.join(C, dataset_dir)):
        for fn in sorted(filenames):
            if fn in ROOT_SKIP or fn == "README.md" or not fn.endswith(DATA_EXT):
                continue
            out.append(os.path.join(dirpath, fn))
    return out


def first_rows(dataset_dir):
    for path in data_files(dataset_dir):
        rows = load_rows(path)
        if rows:
            return os.path.relpath(path, C), rows
    return "-", []


def blob(row):
    return " ".join(str(v) for v in row.values() if v is not None)


def hr(title):
    print("\n" + "=" * 64)
    print(title)
    print("=" * 64)


hr("A. VERIFY PUBLISHED CITATIONS")

# --- mechanicdb (F-1, F-2, L-1, L-4, L-6, P-2, P-4) ---
try:
    md = "corpus/Ichlibitiche__mechanicdb-obd2-repair-sample"
    dfix = load_rows(f"{md}/diagnostic_fixes.json")
    with_hours = [r for r in dfix if r.get("est_labor_hours") not in (None, "", [], "null")]
    rm = [r for r in dfix if re.search(r"\bremove\b", blob(r), re.I)]
    ri = [r for r in dfix if re.search(r"\breinstall\b", blob(r), re.I)]
    print(f"\n[F-1 F-2 L-1 L-4 L-6 P-2 P-4] mechanicdb diagnostic_fixes.json: {len(dfix)} procedures")
    print(f"  rows with est_labor_hours: {len(with_hours)}  (L-1)")
    print(f"  rows mentioning 'remove': {len(rm)}; 'reinstall': {len(ri)}  (L-6)")

    rp = load_rows(f"{md}/replacement_parts.json")
    per_fix = Counter(r.get("fix_id") for r in rp)
    kits = [r for r in rp if re.search(r"\bkit\b", str(r.get("part_name", "")), re.I)]
    print(f"[P-2 P-4] replacement_parts.json: {len(rp)} part rows, {len(per_fix)} distinct procedures, "
          f"max {max(per_fix.values())} parts per procedure")
    print(f"  part rows naming a kit: {len(kits)}  (P-4)")
    for r in kits[:2]:
        print(f"    kit sample: {r.get('part_name')}")
    print(f"  part rows mentioning 'core': {sum(1 for r in rp if re.search(r'core', blob(r), re.I))}")

    cm = read_text(f"{md}/cost_metadata.json")
    m = re.search(r"[^\"]*supplies[^\"]*", cm, re.I)
    print(f"[F-2] cost_metadata supplies quote: {m.group(0)[:180] if m else 'NOT FOUND'}")
except Exception as e:
    print(f"[mechanicdb] ERROR: {e}")

# --- CPSC recalls (F-3) ---
try:
    fname, rows = first_rows("yandyman__us-consumer-recalls")
    hz = [r for r in rows if re.search(r"hazmat|hazardous waste", blob(r), re.I)]
    print(f"\n[F-3] yandyman recalls ({fname}): {len(rows)} rows; hazardous-waste rows: {len(hz)}")
    if hz:
        q = re.search(r"[^\"]*hazardous waste[^\"]*", blob(hz[0]), re.I)
        print(f"  sample: {q.group(0)[:160] if q else blob(hz[0])[:160]}")
except Exception as e:
    print(f"[yandyman] ERROR: {e}")

# --- OEM maintenance schedule (S-2, S-3) ---
try:
    fname, rows = first_rows("referencesource__oem-vehicle-maintenance-schedule-by-model")
    sq = [r for r in rows if str(r.get("source_quote", "") or "").strip()]
    req = sum(1 for r in rows if re.search(r"\brequired\b", blob(r), re.I))
    rec = sum(1 for r in rows if re.search(r"\brecommend", blob(r), re.I))
    print(f"\n[S-2 S-3] OEM schedule ({fname}): {len(rows)} rows; non-empty source_quote: {len(sq)}")
    print(f"  rows using 'required': {req}; 'recommend*': {rec}")
    if rows:
        r0 = rows[0]
        print(f"  sample: {r0.get('make')} {r0.get('model')} — {r0.get('service_item')} @ {r0.get('interval')}")
        print(f"    quote: {str(r0.get('source_quote'))[:140]}")
except Exception as e:
    print(f"[oem-schedule] ERROR: {e}")

# --- claritystorm NHTSA complaints (S-1) ---
try:
    cs = load_rows("corpus/claritystorm__nhtsa-vehicle-complaints/sample_1000.csv")
    sym = [r for r in cs if re.search(r"noise|rattl|pull|shak|grind", blob(r), re.I)]
    print(f"\n[S-1] claritystorm sample_1000.csv: {len(cs)} rows; symptom-vocab rows (noise/rattle/pull/shake/grind): {len(sym)}")
except Exception as e:
    print(f"[claritystorm] ERROR: {e}")

# --- abandoned vehicle timelines (F-6) ---
try:
    fname, rows = first_rows("referencesource__abandoned-vehicle-private-property-timelines-by-state")
    print(f"\n[F-6] abandoned-vehicle ({fname}): {len(rows)} rows")
    for st in ("Colorado", "Alabama"):
        hit = next((r for r in rows if str(r.get("state", "")).lower() == st.lower()), None)
        if hit:
            print(f"  {st}: {str(hit.get('source_quote'))[:150]} [{hit.get('regulatory_citation')}]")
    stor = [r for r in rows if re.search(r"storage", blob(r), re.I)]
    print(f"  rows mentioning storage: {len(stor)}")
except Exception as e:
    print(f"[abandoned-vehicle] ERROR: {e}")

# --- discontinued part mapping (P-5, P-1, P-6) ---
try:
    fname, rows = first_rows("referencesource__discontinued-part-replacement-mapping")
    oem = [r for r in rows if re.search(r"\bOEM\b|aftermarket", blob(r), re.I)]
    print(f"\n[P-5 P-1 P-6] discontinued-parts ({fname}): {len(rows)} rows; OEM/aftermarket rows: {len(oem)}")
    if rows:
        r0 = rows[0]
        print(f"  sample: {r0.get('discontinued_part')} | mfr: {r0.get('manufacturer')} | replacement: {r0.get('suggested_replacement')}")
except Exception as e:
    print(f"[discontinued-parts] ERROR: {e}")

# --- boiler inspection (S-4) ---
try:
    fname, rows = first_rows("referencesource__boiler-inspection-requirements-by-state")
    print(f"\n[S-4] boiler-inspection ({fname}): {len(rows)} rows")
    if rows:
        r0 = rows[0]
        print(f"  sample: {r0.get('state')} — inspectors: {str(r0.get('accepted_inspectors'))[:120]}")
        print(f"    low-pressure interval: {r0.get('low_pressure_boiler_interval')}")
except Exception as e:
    print(f"[boiler-inspection] ERROR: {e}")

# --- building permit validity (D-1, D-4) ---
try:
    fname, rows = first_rows("referencesource__building-permit-validity-and-renewal")
    val = sum(1 for r in rows if re.search(r"valid|expire", blob(r), re.I))
    print(f"\n[D-1 D-4] building-permit ({fname}): {len(rows)} rows; rows with validity/expiry language: {val}")
    fee = next((r for r in rows if re.search(r"fee", blob(r), re.I)), None)
    if fee:
        print(f"  fee row ({fee.get('jurisdiction')}): {str(fee.get('source_quote'))[:170]}")
except Exception as e:
    print(f"[building-permit] ERROR: {e}")

# --- NHTSA narratives: TSB mentions (D-6) ---
try:
    im = load_rows("corpus/ItsMayur__Vehicle_Complaints_NHSTA/mydata.csv")
    tsb = [r for r in im if re.search(r"\bTSB\b|technical service bulletin|service bulletins", blob(r), re.I)]
    print(f"\n[D-6] ItsMayur narratives: {len(im)} rows; TSB/bulletin rows: {len(tsb)}")
    for r in tsb[:2]:
        q = re.search(r"[^\"]*(?:TSB|bulletin)[^\"]*", blob(r), re.I)
        if q:
            print(f"  sample: {q.group(0)[:160]}")
    km = load_rows("corpus/karsonmadden__us-vehicle-trouble-codes/dtc.json")
    print(f"[D-6] karsonmadden dtc.json: {len(km)} codes; 'bulletins' is a per-code count field")
    if km:
        print(f"  sample: {km[0].get('code')} — bulletins: {km[0].get('bulletins')}, owner reports: {km[0].get('owner_reports')}")
except Exception as e:
    print(f"[D-6 sources] ERROR: {e}")

# --- NHTSA complaints: core charge (P-7) ---
try:
    vg = load_rows("corpus/vic35get__nhtsa_complaints_dataset/train-00000-of-00001.json")
    core = [r for r in vg if re.search(r"core charge|core deposit", blob(r), re.I)]
    print(f"\n[P-7] vic35get complaints: {len(vg)} rows; core-charge rows: {len(core)}")
    if core:
        q = re.search(r"[^\"]*core[^\"]*", blob(core[0]), re.I)
        print(f"  sample: {q.group(0)[:200] if q else blob(core[0])[:200]}")
except Exception as e:
    print(f"[vic35get] ERROR: {e}")

hr("B. VOCABULARY HUNT — whole corpus, one pass, data files only")

HUNTS = {
    "hazmat / environmental (fee sense)": r"hazmat|hazardous waste|environmental (fee|charge)",
    "disposal fee (fee sense)": r"disposal fee|waste disposal|tire disposal|oil disposal|fluid disposal",
    "administrative / document fee": r"administrative fee|document fee|doc fee|filing fee",
    "labor rate": r"hourly rate|labor rate|labour rate|flat[- ]rate|shop rate",
    "repair authorization": r"unauthoriz\w*|written (authorization|approval|consent)|owner authorization|without (my |owner )?(authorization|approval|consent)",
    "verbal / oral authorization": r"verbal (authorization|approval|consent|agreement)|oral (authorization|approval|consent)",
    "while-we're-in-there phrasing": r"while we'?re in there|since we'?re in there|already (apart|off|out) anyway",
    "misc catch-all": r"\bmisc\b|miscellaneous",
    "TSB justification": r"\bTSB\b|technical service bulletin",
    "core charge": r"core charge|core deposit",
    "storage fee / charge": r"storage (fee|charge)",
    "add-on / unauthorized billing": r"charg(?:ed|ing) (?:me |the customer )?(?:twice|again)|double[- ]charg|did ?n[o']t (?:authorize|approve|ask for)|never authorized",
    "AI-injection text": r"ignore (?:all )?previous (?:instructions|prompt)|disregard (?:all )?previous",
}

master = re.compile("|".join(f"(?P<n{i}>{pat})" for i, pat in enumerate(HUNTS.values())))
names = {f"n{i}": label for i, label in enumerate(HUNTS.keys())}
tally = {label: 0 for label in HUNTS}
files_hit = {label: set() for label in HUNTS}
samples = {label: [] for label in HUNTS}

for dirpath, dirnames, filenames in os.walk(C):
    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
    for fn in filenames:
        if fn in ROOT_SKIP or fn == "README.md" or not fn.endswith(DATA_EXT):
            continue
        path = os.path.join(dirpath, fn)
        try:
            text = read_text(path)
        except Exception:
            continue
        for m in master.finditer(text):
            label = names[m.lastgroup]
            tally[label] += 1
            files_hit[label].add(path)
            if len(samples[label]) < 3:
                ctx = text[max(0, m.start() - 60):m.end() + 90].replace("\n", " ").replace("\r", " ")
                samples[label].append(f"{os.path.relpath(path, C)} :: …{ctx}…")

for label in HUNTS:
    print(f"\n[{label}] matches: {tally[label]} in {len(files_hit[label])} file(s)")
    for s in samples[label]:
        print(f"  {s[:220]}")

print("\nRecord this pass in corpus/TUNING.md.")
