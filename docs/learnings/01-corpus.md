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

---

## L9 · The rubric's axis is line anatomy, not domain — home is a document type, not a subcategory

**Learning.** The question "should the pattern library split into auto / home / other rubrics?" was weighed on 2026-11-21 and answered no. A rubric's categories come from the document's own line anatomy — fees, labor, parts, scope, documentation, machine-directed text — because the decoder reads lines, not trades. A domain split would fork each pattern into per-domain copies (an auto F-1 and a home F-1), the parallel-copy drift the one-owner rule exists to prevent. Domain coverage enters one level up, at the document type: one rubric file per type, built when a real document appears — the path the invoice pack (v0.2.0) and the body-shop/insurance estimates (deferred) already follow. The corpus settled the timing as much as the charter did: the home lane cannot ground a home rubric yet, so a split today would ship patterns that cannot earn a source.

**Evidence.** L5 — the home lane clusters on jurisdiction and market, not repair vocabulary; [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Gaps — no US/Canada estimate or invoice corpus in either lane; §Candidate patterns — the home candidates H-04 "per square" and H-05 "per linear foot" are recorded and parked, not rubricized; the citation review in [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md) — the home lane's one fee-level citation attempt, a garbage-disposal appliance read as a waste-disposal fee, did not hold and was downgraded to brief; [`../../CONVENTIONS.md`](../../CONVENTIONS.md) — one owner per file, no parallel copies, and §Building a new document type step 1: document types are built when a real one appears, never for completeness; [`../../shared/document-types.md`](../../shared/document-types.md) — the type guard: an unsupported document type is named as unsupported and offered a general anatomy pass, not decoded with the wrong rubric.

**Change.** The estimate rubric stays one file organized by line anatomy; no domain subcategories. A home-repair (contractor) estimate is parked in [`../../ROADMAP.md`](../../ROADMAP.md) §Candidate/deferred with its trigger — a real home estimate from a real user — and enters, if ever, as its own document type under the CONVENTIONS sequence: charter lines in `shared/document-types.md`, its own rubric file, fixtures including a near-miss, ROADMAP listing. The home candidates stay in the tuning log until then.

---

## L10 · A published count is a claim — the measurement must be a command

**Learning.** The first calibration published S-1 (symptom mismatch) as "176 of 1,000 rows carry the symptom vocabulary." Re-measured with a defined search — the five families noise, rattle, pull, shake, grind, case-insensitive, across all columns — the count is 163. Nothing was wrong with the dataset; the number was prose. It carried no definition of the vocabulary and no command behind it, so no one could re-check it, including us. This is L8's drift class applied to numbers: a count embedded in prose drifts exactly like a compiled file, and a citation that cannot be re-measured is indistinguishable from an invented one.

**Evidence.** `corpus/verify.py` section A output, 2026-11-21: claritystorm `sample_1000.csv` — 1,000 rows, 163 matches. The corrected source line in [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md) (S-1). The tool is committed kit tooling (commit `66ad28b`), documented in [`../../corpus/README.md`](../../corpus/README.md) §Citation check; the correction is recorded in [`../../corpus/TUNING.md`](../../corpus/TUNING.md) pass 2.

**Change.** Every count in every pattern's source line is now the tool's output, and the rubric's *Using the library* rule 7 requires running `python3 corpus/verify.py` after any rubric change and recording the pass in the tuning log. The tool lives in the repo beside `fetch.py` and `convert.py` — verification tooling that is not checked in is verification that did not happen.

---

## L11 · "No corpus source" usually means not yet searched — and thin evidence is fine when it wears its count

**Learning.** Before the revisit, 16 patterns were graded brief, most on a bare "design brief. No corpus source." The vocabulary hunt split that label into two different truths. Four sources had been sitting in the corpus unsearched: `cost_metadata.json` had said "hours only, no labor rate" (L-2) all along, 80 of 449 part rows name a kit (P-4), and the recall remedies carry the regulated disposal practice the fee patterns name (F-3, F-4). The rest gained a stated negative check — what was searched and what was found — so "brief" became an auditable state instead of a shrug. The upgrade does not reverse the earlier downgrade of recall-data citations: the downgraded claims said the dataset held fee complaints (it does not); the upgraded claims say it holds hazardous-waste procedure language (105 rows, and it does). The claim must match the text, not stretch it. And thin evidence can ground a pattern when it is labeled with its own count: P-7 core charge rests on one narrative of 12,534; D-6 per TSB on 3 of 1,063.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) pass 2 — the grading table (F-3, F-4, L-2, P-4 brief → adjacent; P-7 and D-6 entered; S-1 corrected; P-2 precision fix) and the negative-check list (zero administrative-fee vocabulary corpus-wide; zero verbal-authorization language; "misc" only as home cost-register shorthand; the corpus's only "unauthorized" text is recall hazard language). Every number is `corpus/verify.py` output.

**Change.** Every brief-sourced pattern in the estimate rubric now names its negative check, and the source-strength definition says the corpus has been searched. Final grading: 32 patterns — 4 direct · 16 adjacent · 12 brief. The 12 brief patterns now differ from the corpus-sourced ones by evidence, not by effort.

---

## L12 · A status row is a claim — check it against git, not against memory

**Learning.** The WBS is a working checklist that people (and agents) trust to decide what is left. Its rows are claims, and they drift in both directions in the same way a compiled file does. In one session the record was wrong twice: WP-1 row 1.7 read "Commit + push the corpus batch — 🔶 awaiting your go" for a commit that `git branch -r --contains` shows sitting on `origin/main` (under-reporting finished work, which invites someone to re-do it); and WP-2 rows 2.3 and 2.4 still read "30/30" and "all 30 written" after the library had become 32 patterns (over-reporting stale work, which makes the row prove nothing). Neither error was caused by bad intent — both were caused by editing one file and not re-reading the row it governed. A status row is a measurement, and a measurement that is never re-taken is a guess wearing a checkmark.

**Evidence.** `git branch -r --contains 748c5c0` → `origin/main`, against [`../WBS.md`](../WBS.md) row 1.7 as written; the 30/30 residue in the same file rows 2.3–2.4 against [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md), whose index holds 32 rows. The correction is L10's, applied to status instead of counts.

**Change.** Before flipping a WBS row, the claim is verified against the artifact it describes: `git branch -r --contains <sha>` for anything that says committed or pushed, and a count of the actual file (for this kit, `grep -c "^### " estimate/rubrics/patterns-estimate.md`) for anything that says *n* of *n*. Where a row cannot be verified by a command, it says so instead of carrying a checkmark.

---

## L13 · A ratio target silently re-defines itself when its denominator moves

**Learning.** The fixture manifest set "at least one near-miss for every two pattern fixtures." Written against six pattern fixtures and a 30-pattern library, that meant three near-misses. The library then grew to 32 patterns and the fixture set grew to cover them, which moved the denominator without touching the ratio text — so the same sentence now demanded more near-misses than existed, and the WBS carried the gap as an open decision instead of a number. A ratio is a promise about proportion; when the thing it is a proportion of changes, the promise changes quietly and no one notices, because the sentence reads the same. Targets that stay honest are counted in the units the work is actually planned in.

**Evidence.** [`../../tests/MANIFEST.md`](../../tests/MANIFEST.md) §Coverage targets ("At least one near-miss for every two pattern fixtures") against its golden list (6 pattern fixtures, 1 near-miss); [`../WBS.md`](../WBS.md) item 4.6, which records the arithmetic (6 pattern ⇒ 3 near-misses, only 07 exists) as an unresolved decision after the library reached 32 patterns.

**Change.** The rule: a near-miss target is written as a count derived from the pattern fixture count in the same file, so the two move together or the discrepancy is visible on the page; and coverage is recorded as an explicit pattern-to-fixture map, so "which pattern still has no fixture" is answered by reading the manifest rather than by trusting the ratio. The correction itself is carried by WP-4 item 4.6, which is open.