# 01 — Corpus learnings

What building the corpus taught, and what changed in the kit because of it. Format follows the kit's grounding rule: every learning cites its artifact — a dataset, a count, a file. Nothing is asserted from memory. Learnings are appended, never rewritten.

Upstream records: [`../../corpus/README.md`](../../corpus/README.md) · [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) · [`../../corpus/TUNING.md`](../../corpus/TUNING.md) · the build method in [`../HOW-BUILT.md`](../HOW-BUILT.md).

## L1 · Narrow to US/Canada — repair is jurisdictional, and the data proves it

**Learning.** The first vendoring pass mixed geographies (India property-maintenance tickets, Australian mining-equipment triage data) and it was wrong. Repair is jurisdictional: fee structures (sales tax vs. GST/VAT), labor-rate norms, licensing regimes, inspection requirements, and even document formats differ by country — and by state and province within them. A mixed-geography corpus does not add coverage; it teaches the rubric conflicting vocabulary. The US/Canada rule exists because the *documents* the kit decodes are US/Canada documents.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Removed — `svr99991/india-synthetic-property-maintenance-tickets` (India; different fee structures and formats) and `karthe05/maintenance-work-order-triage-data` (MaintNorm/MaintIE, University of Western Australia; mining fleet language) were vendored then removed 2026-11-21. The positive case is in the vendored sets themselves: OBD-II codes are the US SAE J2012 standard ([`corpus/CodesList__obd2-codes`](../../corpus/CodesList__obd2-codes/README.md)); NHTSA complaints and recalls are US federal data; the permit, licensing, and cost-register sets are per-state.

**Change.** The geography rule is written into [`../../corpus/README.md`](../../corpus/README.md) as a hard rule with its reason, and the removal record is kept in the manifest rather than quietly deleted.

---

## L2 · The corpus everyone wants does not exist — there is no US/Canada estimate/invoice dataset

**Learning.** Across a 930-dataset index and 54 vendored sets, the Hugging Face surface contains **zero** US/Canada datasets of real repair *estimates* or *invoices* at scale. The surface is rich in everything *around* the document — complaints (what breaks), recalls (what is unsafe), diagnostic codes (what the computer says), maintenance schedules (what the OEM requires), permits and licensing (what the law requires), cost indices (what jobs cost) — and silent on the document itself. The kit's actual input artifact has no public corpus.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Considered and rejected — nine candidates inspected and rejected, several because they were estimate-shaped but not repair documents (dealership CRM parquet, car-sales listings, collision statistics). [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Gaps records the same finding from the research side.

**Change.** The kit's fixtures are synthetic — authored estimates with planted patterns ([`../../tests/README.md`](../../tests/README.md) §Provenance) — and the corpus is framed as a calibration reference, not a training set. The gap is stated in the manifest, not papered over.

---

## L3 · The safe side teaches more than the scam side — and the standard side teaches more than the defective one

**Learning.** (Inherited from ScamCheck C1, confirmed here.) The corpus's most useful material is not the defect data — it is the vocabulary of *normal* repair. OEM maintenance schedules are the strongest single source precisely because they are the manufacturer's own idea of routine: they anchor every "per manufacturer" pattern and every *not-a-pattern-when* line. The NHTSA complaint narratives teach the symptom side — owners describe noises and sensations, not parts — which is why the kit's symptom-vs-scope step (Step 3) leads with the user's own words.

**Evidence.** [`corpus/referencesource__oem-vehicle-maintenance-schedule-by-model/data/records.jsonl`](../../corpus/referencesource__oem-vehicle-maintenance-schedule-by-model/README.md) — 6,111 OEM schedule rows, each carrying a `source_quote` from the manufacturer's PDF; complaint component distribution in [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §What the corpus supports.

**Change.** The maintenance-schedule set is first in the manifest's auto-diagnostics section; the TUNING record names it "the calibration anchor for 'per manufacturer' lines."

---

## L4 · Text-only is a hard doctrine, and binaries convert or die

**Learning.** The useful payloads arrive as parquet; the rest of the surface arrives as images, PDFs, audio, and model artifacts. None of those enter as-is. Parquet converts to `.json` + a `.md` preview; anything unreadable as text is dropped and reported, never kept "just in case." The kit reads documents — its corpus should be documents.

**Evidence.** [`../../corpus/convert.py`](../../corpus/convert.py) — converts parquet via pandas, drops `__index_level_0__` artifact columns, deletes the source parquet after conversion; [`../../corpus/fetch.py`](../../corpus/fetch.py) skips non-text extensions by default. Converted sets: `Ichlibitiche/mechanicdb-obd2-repair-sample`, `vic35get/nhtsa_complaints_dataset`. The verification pass in [`../HOW-BUILT.md`](../HOW-BUILT.md) Step 6 found zero non-text files in the corpus.

**Change.** Both tools enforce the doctrine in code; the rules are written in [`../../corpus/README.md`](../../corpus/README.md) §Rules for this folder.

---

## L5 · The home lane is a different shape than the auto lane

**Learning.** Auto repair data clusters around *the machine*: diagnostic codes, recalls, component complaints, maintenance intervals — millions of rows, because the machine is standardized. Home repair data clusters around *the jurisdiction and the market*: building permits, contractor licensing, cost indices, service directories — rich, but about regulation and price context rather than repair vocabulary. The practical consequence: the auto side of the pattern library can be grounded in public defect data; the home side must be grounded in fixture work and industry guidance, with the corpus supplying trade names, fee categories, and scope language.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) — the auto section is complaints/codes/schedules; the home section is permits/licensing/directories/cost registers. `thanna94/us-building-permits` alone is ~780k rows of permit data; `Pisces89/ohio-home-services-pros` is 21.9k contractor records with a `trades` column.

**Change.** The manifest groups vendored sets by area (auto-diagnostics, auto-complaints, home-inside, home-outside, home-contractor, home-cost) so the asymmetry is visible on the page rather than discovered later.

---

## L6 · Inspection at the row level beats trusting the README

**Learning.** Several candidates passed every filter — size, license, text modality, plausible name — and were wrong at the row level: "repair order" datasets that were software mutation orders; "collision" datasets that were robot-arm control frames; "home service" datasets that were robot-demonstration videos; an "invoice" benchmark that was software-SE benchmarks. The dataset card sells; the sample row tells the truth.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Considered and rejected — `dkingtutcd/invariant-repair-*` (software), `LeRobot-worldwide-hackathon/*` (robotics), `nus-yin/ex-repair` (code repair), each with its reason. The method requires a `/first-rows` sample check before every fetch ([`../HOW-BUILT.md`](../HOW-BUILT.md) Step 2).

**Change.** Row-level inspection is a required step in the build method, not an optional courtesy.

---

## L7 · Cost data is context, never content — the charter holds even in the corpus

**Learning.** The corpus contains pricing data (roofing cost indices by city, repair cost registers by trade, market-size tables). It is tempting material for a kit that reads *bills*. It is kept under a strict rule: prices in the corpus are calibration context for what a line item claims to cover — never quoted in a decode, never compared against a user's estimate, never used to produce a "should cost." The no-prices charter applies to the corpus exactly as it applies to the screen.

**Evidence.** [`corpus/ShingleGeek__roofing-cost-index`](../../corpus/ShingleGeek__roofing-cost-index/README.md) — 655 rows of city-level roofing cost; the manifest note: "Contains prices — reference only; the kit never quotes prices." Charter [`../../WHAT-THIS-IS.md`](../../WHAT-THIS-IS.md) §What it is not #1.

**Change.** The rule is written per-dataset in the manifest notes and globally in the corpus README.

---

## L8 · A compiled artifact drifts — keep the index, the manifest, and the spine in one breath

**Learning.** (Inherited from ScamCheck C5.) Any derived copy drifts from its source unless regenerated in the same change. Here the derived artifacts are `INDEX.md` (generated from `index.json`) and, in the kit proper, `estimate/SPINE.md` (compiled from the rubric and workflow). During the build, the first index pass and the manifest briefly disagreed on counts (898 vs. the vendored reality) because new fetches had not yet been re-indexed — the same class of defect.

**Evidence.** The index was rebuilt twice; the vendored-count mismatch is visible in the build log ([`../HOW-BUILT.md`](../HOW-BUILT.md) Steps 1 and 6).

**Change.** The rule from ScamCheck is carried into this kit's conventions: a rubric change requires a spine change in the same breath ([`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) §Changing a rubric), and the corpus method ends with a verify step that recounts what is actually on disk.