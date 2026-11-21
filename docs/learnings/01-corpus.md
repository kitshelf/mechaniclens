# 01 — Corpus learnings

What scoping, building, and reading the corpus taught, and what changed in the kit because of it. Upstream records: [`../../corpus/README.md`](../../corpus/README.md) · [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) · [`../../corpus/TUNING.md`](../../corpus/TUNING.md) · the build method in [`../HOW-BUILT.md`](../HOW-BUILT.md).

Every entry cites its artifact — a file, a dataset, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L1 | Narrow to US/Canada — repair is jurisdictional, and the data proves it | Scoping the corpus |
| L2 | The corpus everyone wants does not exist — there is no US/Canada estimate/invoice dataset | Scoping the corpus |
| L5 | The home lane is a different shape than the auto lane | Scoping the corpus |
| L4 | Text-only is a hard doctrine, and binaries convert or die | Building the corpus |
| L6 | Inspection at the row level beats trusting the README | Building the corpus |
| L3 | The safe side teaches more than the scam side — and the standard side teaches more than the defective one | Learning from the corpus |
| L7 | Cost data is context, never content — the charter holds even in the corpus | Learning from the corpus |
| L11 | "No corpus source" usually means not yet searched — and thin evidence is fine when it wears its count | Learning from the corpus |
| L10 | A published count is a claim — the measurement must be a command | Counting it honestly |
| L15 | Three numbers for one corpus — a typed total is not a summed total | Counting it honestly |

## Scoping the corpus

### L1 · Narrow to US/Canada — repair is jurisdictional, and the data proves it

**Learning.** The first vendoring pass mixed geographies (India property-maintenance tickets, Australian mining-equipment triage data) and it was wrong. Repair is jurisdictional: fee structures (sales tax vs. GST/VAT), labor-rate norms, licensing regimes, inspection requirements, and even document formats differ by country — and by state and province within them. A mixed-geography corpus does not add coverage; it teaches the rubric conflicting vocabulary. The US/Canada rule exists because the *documents* the kit decodes are US/Canada documents.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Removed — `svr99991/india-synthetic-property-maintenance-tickets` (India; different fee structures and formats) and `karthe05/maintenance-work-order-triage-data` (MaintNorm/MaintIE, University of Western Australia; mining fleet language) were vendored then removed 2026-11-21. The positive case is in the vendored sets themselves: OBD-II codes are the US SAE J2012 standard ([`corpus/CodesList__obd2-codes`](../../corpus/CodesList__obd2-codes/README.md)); NHTSA complaints and recalls are US federal data; the permit, licensing, and cost-register sets are per-state.

**Change.** The geography rule is written into [`../../corpus/README.md`](../../corpus/README.md) as a hard rule with its reason, and the removal record is kept in the manifest rather than quietly deleted.

### L2 · The corpus everyone wants does not exist — there is no US/Canada estimate/invoice dataset

**Learning.** Across a 930-dataset index and 54 vendored sets, the Hugging Face surface contains **zero** US/Canada datasets of real repair *estimates* or *invoices* at scale. The surface is rich in everything *around* the document — complaints (what breaks), recalls (what is unsafe), diagnostic codes (what the computer says), maintenance schedules (what the OEM requires), permits and licensing (what the law requires), cost indices (what jobs cost) — and silent on the document itself. The kit's actual input artifact has no public corpus.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Considered and rejected — nine candidates inspected and rejected, several because they were estimate-shaped but not repair documents (dealership CRM parquet, car-sales listings, collision statistics). [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Gaps records the same finding from the research side.

**Change.** The kit's fixtures are synthetic — authored estimates with planted patterns ([`../../tests/README.md`](../../tests/README.md) §Provenance) — and the corpus is framed as a calibration reference, not a training set. The gap is stated in the manifest, not papered over.

### L5 · The home lane is a different shape than the auto lane

**Learning.** Auto repair data clusters around *the machine*: diagnostic codes, recalls, component complaints, maintenance intervals — millions of rows, because the machine is standardized. Home repair data clusters around *the jurisdiction and the market*: building permits, contractor licensing, cost indices, service directories — rich, but about regulation and price context rather than repair vocabulary. The practical consequence: the auto side of the pattern library can be grounded in public defect data; the home side must be grounded in fixture work and industry guidance, with the corpus supplying trade names, fee categories, and scope language.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) — the auto section is complaints/codes/schedules; the home section is permits/licensing/directories/cost registers. `thanna94/us-building-permits` alone is ~780k rows of permit data; `Pisces89/ohio-home-services-pros` is 21.9k contractor records with a `trades` column.

**Change.** The manifest groups vendored sets by area (auto-diagnostics, auto-complaints, home-inside, home-outside, home-contractor, home-cost) so the asymmetry is visible on the page rather than discovered later.

## Building the corpus

### L4 · Text-only is a hard doctrine, and binaries convert or die

**Learning.** The useful payloads arrive as parquet; the rest of the surface arrives as images, PDFs, audio, and model artifacts. None of those enter as-is. Parquet converts to `.json` + a `.md` preview; anything unreadable as text is dropped and reported, never kept "just in case." The kit reads documents — its corpus should be documents.

**Evidence.** [`../../corpus/convert.py`](../../corpus/convert.py) — converts parquet via pandas, drops `__index_level_0__` artifact columns, deletes the source parquet after conversion; [`../../corpus/fetch.py`](../../corpus/fetch.py) skips non-text extensions by default. Converted sets: `Ichlibitiche/mechanicdb-obd2-repair-sample`, `vic35get/nhtsa_complaints_dataset`. The verification pass in [`../HOW-BUILT.md`](../HOW-BUILT.md) Step 6 found zero non-text files in the corpus.

**Change.** Both tools enforce the doctrine in code; the rules are written in [`../../corpus/README.md`](../../corpus/README.md) §Rules for this folder.

### L6 · Inspection at the row level beats trusting the README

**Learning.** Several candidates passed every filter — size, license, text modality, plausible name — and were wrong at the row level: "repair order" datasets that were software mutation orders; "collision" datasets that were robot-arm control frames; "home service" datasets that were robot-demonstration videos; an "invoice" benchmark that was software-SE benchmarks. The dataset card sells; the sample row tells the truth.

**Evidence.** [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) §Considered and rejected — `dkingtutcd/invariant-repair-*` (software), `LeRobot-worldwide-hackathon/*` (robotics), `nus-yin/ex-repair` (code repair), each with its reason. The method requires a `/first-rows` sample check before every fetch ([`../HOW-BUILT.md`](../HOW-BUILT.md) Step 2).

**Change.** Row-level inspection is a required step in the build method, not an optional courtesy.

## Learning from the corpus

### L3 · The safe side teaches more than the scam side — and the standard side teaches more than the defective one

**Learning.** (Inherited from ScamCheck C1, confirmed here.) The corpus's most useful material is not the defect data — it is the vocabulary of *normal* repair. OEM maintenance schedules are the strongest single source precisely because they are the manufacturer's own idea of routine: they anchor every "per manufacturer" pattern and every *not-a-pattern-when* line. The NHTSA complaint narratives teach the symptom side — owners describe noises and sensations, not parts — which is why the kit's symptom-vs-scope step (Step 3) leads with the user's own words.

**Evidence.** [`corpus/referencesource__oem-vehicle-maintenance-schedule-by-model/data/records.jsonl`](../../corpus/referencesource__oem-vehicle-maintenance-schedule-by-model/README.md) — 6,111 OEM schedule rows, each carrying a `source_quote` from the manufacturer's PDF; complaint component distribution in [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §What the corpus supports.

**Change.** The maintenance-schedule set is first in the manifest's auto-diagnostics section; the TUNING record names it "the calibration anchor for 'per manufacturer' lines."

### L7 · Cost data is context, never content — the charter holds even in the corpus

**Learning.** The corpus contains pricing data (roofing cost indices by city, repair cost registers by trade, market-size tables). It is tempting material for a kit that reads *bills*. It is kept under a strict rule: prices in the corpus are calibration context for what a line item claims to cover — never quoted in a decode, never compared against a user's estimate, never used to produce a "should cost." The no-prices charter applies to the corpus exactly as it applies to the screen.

**Evidence.** [`corpus/ShingleGeek__roofing-cost-index`](../../corpus/ShingleGeek__roofing-cost-index/README.md) — 655 rows of city-level roofing cost; the manifest note: "Contains prices — reference only; the kit never quotes prices." Charter [`../../WHAT-THIS-IS.md`](../../WHAT-THIS-IS.md) §What it is not #1.

**Change.** The rule is written per-dataset in the manifest notes and globally in the corpus README.

### L11 · "No corpus source" usually means not yet searched — and thin evidence is fine when it wears its count

**Learning.** Before the revisit, 16 patterns were graded brief, most on a bare "design brief. No corpus source." The vocabulary hunt split that label into two different truths. Four sources had been sitting in the corpus unsearched: `cost_metadata.json` had said "hours only, no labor rate" (L-2) all along, 80 of 449 part rows name a kit (P-4), and the recall remedies carry the regulated disposal practice the fee patterns name (F-3, F-4). The rest gained a stated negative check — what was searched and what was found — so "brief" became an auditable state instead of a shrug. The upgrade does not reverse the earlier downgrade of recall-data citations: the downgraded claims said the dataset held fee complaints (it does not); the upgraded claims say it holds hazardous-waste procedure language (105 rows, and it does). The claim must match the text, not stretch it. And thin evidence can ground a pattern when it is labeled with its own count: P-7 core charge rests on one narrative of 12,534; D-6 per TSB on 3 of 1,063.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) pass 2 — the grading table (F-3, F-4, L-2, P-4 brief → adjacent; P-7 and D-6 entered; S-1 corrected; P-2 precision fix) and the negative-check list (zero administrative-fee vocabulary corpus-wide; zero verbal-authorization language; "misc" only as home cost-register shorthand; the corpus's only "unauthorized" text is recall hazard language). Every number is `corpus/verify.py` output.

**Change.** Every brief-sourced pattern in the estimate rubric now names its negative check, and the source-strength definition says the corpus has been searched. Final grading: 32 patterns — 4 direct · 16 adjacent · 12 brief. The 12 brief patterns now differ from the corpus-sourced ones by evidence, not by effort.

## Counting it honestly

### L10 · A published count is a claim — the measurement must be a command

**Learning.** The first calibration published S-1 (symptom mismatch) as "176 of 1,000 rows carry the symptom vocabulary." Re-measured with a defined search — the five families noise, rattle, pull, shake, grind, case-insensitive, across all columns — the count is 163. Nothing was wrong with the dataset; the number was prose. It carried no definition of the vocabulary and no command behind it, so no one could re-check it, including us. This is L8's drift class applied to numbers: a count embedded in prose drifts exactly like a compiled file, and a citation that cannot be re-measured is indistinguishable from an invented one.

**Evidence.** `corpus/verify.py` section A output, 2026-11-21: claritystorm `sample_1000.csv` — 1,000 rows, 163 matches. The corrected source line in [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md) (S-1). The tool is committed kit tooling (commit `66ad28b`), documented in [`../../corpus/README.md`](../../corpus/README.md) §Citation check; the correction is recorded in [`../../corpus/TUNING.md`](../../corpus/TUNING.md) pass 2.

**Change.** Every count in every pattern's source line is now the tool's output, and the rubric's *Using the library* rule 7 requires running `python3 corpus/verify.py` after any rubric change and recording the pass in the tuning log. The tool lives in the repo beside `fetch.py` and `convert.py` — verification tooling that is not checked in is verification that did not happen.

### L15 · Three numbers for one corpus — a typed total is not a summed total

**Learning.** The corpus carried three different record counts at once, and each looked like a measurement. Five files restated "~1.43M"; the manifest's Totals block declared "~1,451,000"; a file-level recount of the data files returned 1,281,272; and the manifest's own `Rows` column, summed, is **1,272,956**. None of the typed figures stated what it counted — records or files, table rows or dataset-card metadata — so none could be checked against the others. The disk-size line had drifted the same way: "~230 MB" was the size of the whole repository, not `corpus/`, which is 205 MB. An aggregate that is typed is not an aggregate that was summed: it is a memory of a number, and it survives every change to the rows beneath it.

**Evidence.** Summing the `Rows` column of [`../../corpus/MANIFEST.md`](../../corpus/MANIFEST.md) gives 1,272,956 across 54 datasets; `du -sh corpus` gives 205M. The file-level recount exceeded the table for exactly four datasets — `mechanicdb`, `karsonmadden`, `yandyman`, `ShingleGeek` — because each ships the same records twice as `.json` and `.md`/`.csv`, so counting files counts mirrors. The lane table in [`../../corpus/README.md`](../../corpus/README.md) was wrong per group as well: 7 complaint datasets at "~1.1M" were 9 at 333,679; 12 outside-house datasets at "~24k" were 16 at 808,310; 10 cost registers at "~1k" were 4 at 618.

**Change.** Totals are derived, not typed: the manifest states 1,272,956 as "the sum of the `Rows` column above", the README lane table carries counted per-lane numbers that sum exactly to it, and every file that quotes a total names the manifest as its owner. Rule: an aggregate is re-derivable from the table it summarises, and a measurement states its unit and its source or it does not go in the record.
