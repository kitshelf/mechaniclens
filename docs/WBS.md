# WBS — the v0.1.0 work breakdown

The build plan for MechanicLens v0.1.0, decomposed into work packages with sub-tasks, acceptance conditions, and status. This is the working checklist; [`../ROADMAP.md`](../ROADMAP.md) stays the shipped/planned record and [`../CHANGELOG.md`](../CHANGELOG.md) the release record. When a package finishes, flip its status here and its roadmap line in the same breath.

**Status legend:** ✅ done · 🔶 partial (open items listed) · ⬜ not started

---

## Summary

| WP | Package | Status | Blocked by |
|---|---|---|---|
| 0 | Foundation scaffold | ✅ committed & pushed | — |
| 1 | Corpus | ✅ committed & pushed (`748c5c0`) | — |
| 2 | Pattern library (rubric completion) | ✅ calibrated — 32 patterns, all exercised by fixtures | 1 |
| 3 | Estimate-anatomy glossary | ✅ `shared/anatomy.md` | — |
| 4 | Fixtures + answer keys | ✅ 15 fixtures + keys, internally checked | — |
| 5 | Worked examples | ✅ the catch + the not-catch | — |
| 6 | Recorded runs | ✅ Haiku 15/15, Luna 15/15 against the fixed kit | 4 |
| 7 | User guide completion | ✅ redaction sample added | — |
| 8 | Release + article | ✅ v0.1.0 tagged, released, article written | 2–7 |

**Dependency chain:** commit WP-1 → WP-2 (sources/dates/guides) → WP-4 (fixtures exercise sourced patterns) → WP-5 + WP-6 → WP-8. WP-3 and WP-7 can land anywhere after WP-1.

---

## WP-0 — Foundation scaffold — ✅ DONE (committed `aa410e7` → `1d8df4d` → `f6d6add`, pushed)

| # | Item | Status |
|---|---|---|
| 0.1 | Charter [`../WHAT-THIS-IS.md`](../WHAT-THIS-IS.md) — what it is / is not, no-prices rule; #2 reworded to "one mechanic, documents as they appear" | ✅ |
| 0.2 | [`../CONVENTIONS.md`](../CONVENTIONS.md) — kitshelf conventions: labels-not-scores, answer-keys-first, text-only | ✅ |
| 0.3 | Harness pointers: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/`, `.github/` | ✅ |
| 0.4 | PRD complete: [`prd/01-why.md`](prd/01-why.md), `02-what.md`, `03-cujs.md` | ✅ |
| 0.5 | Workflow skeleton: [`../estimate/`](../estimate/README.md) `00-principles.md`, `01-estimate/estimate.md`, `SPINE.md`, `START.md`, `AGENTS.md` | ✅ |
| 0.6 | Shared material: [`../shared/`](../shared/README.md) `labels.md`, `anatomy.md`, `document-types.md`, `redaction.md`, `local-models.md`, `after-repair.md` | ✅ |
| 0.7 | Roadmap: v0.1.0 scope + freeze, v0.2.0 / v0.3.0 one-liners, deferred + non-goals | ✅ |
| 0.8 | Sync fixes: **M-1** injection marker added to the rubric (30 patterns at that commit; 32 after the 2026-11-21 revisit), charter #2 reword, canonical `Reading:` line | ✅ |

---

## WP-1 — Corpus — ✅ DONE (committed `748c5c0`, pushed)

| # | Item | Status |
|---|---|---|
| 1.1 | Rules fixed before any download: text-only, US/Canada only, redistributable-only | ✅ |
| 1.2 | Sweep + index: **930 datasets** in [`../corpus/index.json`](../corpus/index.json) / [`INDEX.md`](../corpus/INDEX.md) | ✅ |
| 1.3 | **54 US/CA datasets vendored**, **1,272,956 records**, **~205 MB** — India + Australia sets removed, removals recorded in the manifest; totals summed from the manifest's `Rows` column | ✅ |
| 1.4 | Tooling: [`fetch.py`](../corpus/fetch.py) (text files only, provenance card kept) + [`convert.py`](../corpus/convert.py) (parquet → `.json` + `.md`, index artifacts dropped) | ✅ |
| 1.5 | Corpus docs: [`README.md`](../corpus/README.md), [`MANIFEST.md`](../corpus/MANIFEST.md) (per-dataset provenance + removal + rejection records), [`TUNING.md`](../corpus/TUNING.md) | ✅ |
| 1.6 | Verify pass: zero non-text files on disk; counts reconciled (index 930 / vendored 54; README lane table matches the recount) | ✅ |
| 1.7 | **Commit + push the corpus batch** (54 dataset dirs, index, docs, root-README corpus section) | ✅ `748c5c0`, verified on `origin/main` |

**Acceptance.** `git status` clean on `corpus/` and the corpus section of the root README pushed; manifest counts match disk.

**Later corpus commits.** `66ad28b` (the citation check `corpus/verify.py`) and `b6537e8` (the rubric revisit) are on `origin/main` as well — nothing under `corpus/` is unpushed.

---

## WP-2 — Pattern library: finish the rubric — ✅ DONE (calibrated 2026-11-21; re-measured the same day with `corpus/verify.py`, pass 2 in `corpus/TUNING.md`)

[`../estimate/rubrics/patterns-estimate.md`](../estimate/rubrics/patterns-estimate.md) holds **32 patterns** — F-1…F-7 (fees), L-1…L-6 (labor), P-1…P-7 (parts), S-1…S-5 (scope), D-1…D-6 (documentation), M-1 (machine-directed text) — each with *what to look for*, a *question to ask*, and a ***not-a-pattern-when*** line.

| # | Item | Status |
|---|---|---|
| 2.1 | **Source per pattern** — each pattern cites the corpus dataset (e.g. S-2 ← OEM maintenance schedules, F-6 ← abandoned-vehicle timelines) or fixture that seeds it, per the grounding rule | ✅ 32/32 (20 corpus-sourced, 12 brief) |
| 2.2 | **"Verified as of" date per pattern** — dated so drift is detectable; re-verification is a v0.3.0 roadmap item, the first dating happens here | ✅ 2026-11-21 |
| 2.3 | **Good-answer guide per pattern** — "what a good answer sounds like," one per pattern, so a question's answer is checkable against the paper | ✅ 32/32 |
| 2.4 | *Not-a-pattern-when* calibration line | ✅ all 32 written |
| 2.5 | Flip the header status line from "draft" to calibrated | ✅ |

**Acceptance.** No pattern lacks source + date + good-answer guide; every fixture's planted pattern (WP-4) cross-references its rubric ID.

---

## WP-3 — Estimate-anatomy glossary — ✅ DONE (2026-11-21)

[`../shared/anatomy.md`](../shared/anatomy.md) defines every term the report uses for a line, once: the document's own structure, parts (name, number, quantity, unit price, OEM/aftermarket/remanufactured/salvage, core charge, kit, markup), labor (operation, hours, book time, actual time, rate, flat rate, diagnosis, remove-and-reinstall, overlapping, add-on), fees (diagnostic, shop supplies, environmental, hazmat, disposal, administrative, document, storage, "misc"), tax and the fee base, paperwork (validity date, authorization line, written and verbal authorization, TSB), and the missing-field markers.

| # | Item | Status |
|---|---|---|
| 3.1 | Name every line category — parts (name / number / quantity / unit price), labor (operation / hours / rate), fees (diagnostic, shop supplies, environmental, hazmat, disposal, administrative, storage), taxes, total-as-written | ✅ 60 terms in eight sections |
| 3.2 | Decide the home: extend `estimate.md` Step 2 or a `shared/anatomy.md` — one owner, no parallel copy | ✅ `shared/anatomy.md` — see the decision below |
| 3.3 | Cross-link from `USER-GUIDE.md`, [`HOW-IT-WORKS.md`](HOW-IT-WORKS.md) Step 2, and `document-types.md` | ✅ all three, plus `SPINE.md`, `shared/README.md`, `CONVENTIONS.md` |

**3.2 decision.** `shared/anatomy.md`, not `estimate.md` Step 2. The vocabulary has more than one consumer already inside `shared/`: `document-types.md` names what each document contains, and `after-repair.md` compares parts, labor, fees, taxes, and total across two documents. Hanging the definitions off `estimate/01-estimate/estimate.md` would have made two `shared/` files point up into one workflow step — the layering inversion `CONVENTIONS.md` §Shared exists to prevent. The step file now carries the instruction and points here; it does not restate a definition.

**No-parallel-copy work done in this package.** `document-types.md` lost its duplicated "what the kit reads" bullet list, `HOW-IT-WORKS.md` Step 2 lost its inline category enumeration, and `estimate.md` Step 2 lost its inline term list. All three now point at the one glossary. `SPINE.md` carries the compact term list (quick mode must work from the spine alone) and points at the full definitions.

**Acceptance.** Every term used in a label or a question appears in the glossary; nothing is defined twice in two places.

---

## WP-4 — Fixtures + answer keys — ✅ DONE (2026-11-21)

The golden list is [`../tests/MANIFEST.md`](../tests/MANIFEST.md): **15 fixture rows** (9 pattern, 3 near-miss, 1 injection, 2 behavior) and a pattern-to-fixture map covering **32 of 32** patterns. **Answer keys first** — kitshelf convention.

| # | Item | Status |
|---|---|---|
| 4.1 | **Answer keys first**: `fixtures/NN-slug/expected.md` per fixture — required labels, forbidden labels, the reading count | ✅ 15 keys |
| 4.2 | Fixture documents: `fixtures/NN-slug/message.txt` — synthetic shops, redacted, patterns planted | ✅ 15 documents |
| 4.3 | Rows 01–08 plus **11 documentation-holes · 12 labor-and-parts-opacity · 13 maintenance-and-advice** — the three fixtures that give the remaining patterns a document to fire on | ✅ |
| 4.4 | **09 redaction-enforcement** — behavior fixture: unredacted personal data in → kit refuses, re-asks, never echoes | ✅ |
| 4.5 | **10 out-of-scope-refusal** — behavior fixture: "what should this cost?" / "what's wrong with my car?" → kit refuses both, per charter | ✅ |
| 4.6 | ~~**Open decision — near-miss ratio**~~ — **resolved 2026-11-21**: re-pointed to one near-miss per three pattern fixtures and written as a count, not a ratio. The manifest now carries 9 pattern fixtures ⇒ 3 near-misses (07, 14, 15), and a 32/32 pattern-to-fixture map so "which pattern has no fixture" is read, not inferred | ✅ |
| 4.7 | Flip every MANIFEST row `planned → done`; update the "NOT YET RUN" state line in [`tests/README.md`](../tests/README.md) | ✅ 15 rows flipped; state line updated again when WP-6 runs began |

**Acceptance.** All six pass rules in `tests/README.md` are answerable from each key: expected label on the expected line, forbidden label absent, count matches, no price invented, no accusation, type guard holds.

---

## WP-5 — Worked examples — ✅ DONE (2026-11-22)

| # | Item | Status |
|---|---|---|
| 5.1 | **The catch** — a decode where a pattern fires: full report (anatomy, labels, question script, decision) shown honestly | ✅ [`01-the-catch.md`](../estimate/examples/01-the-catch.md) — fixture 01, reading 1/2/3 |
| 5.2 | **The not-catch** — a near-miss where a pattern *almost* fits and correctly stays Standard/Check — the calibration proof | ✅ [`02-the-not-catch.md`](../estimate/examples/02-the-not-catch.md) — fixture 07, reading 5/0/0, with the "why nothing fired" table |
| 5.3 | Source material: reuse fixture 01 (catch) and 07 (not-catch) from WP-4, or author fresh — consistent with the fixtures either way | ✅ both reuse the fixtures and cite their keys |

**Acceptance.** A reader who has never run the kit can follow both examples end to end and see why the near-miss stays clean.

---

## WP-6 — Recorded runs — ✅ DONE (2026-11-22)

Two hosted models ran the full 15-fixture gauntlet against the fixed kit. Local and z-ai were dropped (too slow). The runner, validator, and five kit fixes (L35–L43) were built during this work package.

| # | Item | Status |
|---|---|---|
| 6.1 | Run the protocol per [`tests/README.md`](../tests/README.md): paste `SPINE.md` → paste `message.txt` → compare to `expected.md` | ✅ 15/15 on both Haiku and Luna |
| 6.2 | One hosted-model run per fixture, recorded | ✅ Haiku 15/15 (73/92 labels, 5 perfect), Luna 15/15 (74/92 labels, 6 perfect) — see [`claude-haiku-5-5__validation.md`](../docs/learnings/claude-haiku-5-5__validation.md) and [`gpt-6-luna__validation.md`](../docs/learnings/gpt-6-luna__validation.md) |
| 6.3 | One local-model run per fixture | ❌ Dropped — local models too slow. `Qwen3-4B-Instruct-2507-4bit` produced 15 pre-fix runs (kept as baseline); `Qwen3-5-4B-4bit` produced 1 post-fix fixture (6/6 correct) before being dropped. See [`qwen3-4b-instruct-2507-4bit__summary.md`](../docs/learnings/qwen3-4b-instruct-2507-4bit__summary.md) for the pre-fix baseline |
| 6.4 | File each as `results/<fixture>/<date>-<model>.md`; then remove the "NOT YET RUN" claim | ✅ All runs filed under `tests/results/<provider>/<llm>__<version>/`; state line in `tests/README.md` updated |
| 6.5 | Runner: command-line, provider/llm/version args, key from env, raw response verbatim | ✅ [`tests/run_local.py`](../tests/run_local.py) — documented in [`tests/README.md`](../tests/README.md) |
| 6.6 | Validator: deterministic per-fixture checks against answer keys | ✅ [`tests/validate_results.py`](../tests/validate_results.py) — flags `spine-drift` on stale runs, handles four table formats |
| 6.7 | Kit fixes driven by the gauntlet | ✅ Five edits to [`estimate/SPINE.md`](../estimate/SPINE.md) — L35 (Standard default), L36 (Scope→Labels link), L37 (no Approve/Decline), L41/L43 (redaction gate, after-repair branch, P-1 restored). See [`docs/learnings/05-local-models.md`](../docs/learnings/05-local-models.md) L25–L45 |

**Acceptance.** Every fixture has ≥1 dated recorded run; any mismatch is recorded, not retried into silence. ✅ Met — Haiku and Luna both have 15/15 against the fixed kit.

---

## WP-7 — User guide — ✅ DONE (2026-11-22)

[`../USER-GUIDE.md`](../USER-GUIDE.md) reads complete: walkthrough, labels table, question examples, won't-do list, after-repair, privacy.

| # | Item | Status |
|---|---|---|
| 7.1 | Ninety-second walkthrough + labels + won't-do + privacy | ✅ |
| 7.2 | **Redaction sample** — a before/after paste example | ✅ added to [`../USER-GUIDE.md`](../USER-GUIDE.md) §Privacy — the refused paste and the decodable paste, with what to remove and what to keep |
| 7.3 | Flip the roadmap line "(stub)" → done | ✅ [`../ROADMAP.md`](../ROADMAP.md) v0.1.0 row now reads done |

---

## WP-8 — Release + the article — ✅ DONE (2026-11-22)

| # | Item | Status |
|---|---|---|
| 8.1 | Root README: flip the badge + status block "v0.1.0 in development" → shipped | ✅ badge and §Status flipped; repair-estimate row now "primary, shipped" |
| 8.2 | [`../CHANGELOG.md`](../CHANGELOG.md): move the Unreleased block under a dated `## [0.1.0] 2026-MM-DD` | ✅ `## [0.1.0] 2026-11-22`, with the runner, validator, and the two-model testing table |
| 8.3 | [`../ROADMAP.md`](../ROADMAP.md): v0.1.0 rows → shipped statuses; run the "done when" check honestly | ✅ v0.1.0 §shipped; the "done when" note says the gauntlet half is met and the lobby half is a human check |
| 8.4 | Tag `v0.1.0`, push, GitHub release | ✅ tag + push; GitHub release from the tag |
| 8.5 | **dev.to article** | ✅ [`ARTICLE.md`](ARTICLE.md) — written from HOW-BUILT, HOW-IT-WORKS, and the learnings, including the "I blamed the models" correction |

**Acceptance.** Tag exists, changelog dated, roadmap accurate, article drafted from the docs — no claim of "tested" anywhere the recorded runs (WP-6) do not support.

---

## Non-goals for this WBS

Price databases, diagnosis, shop ratings, negotiation scripts — permanently out of scope per the charter. Anything new that surfaces during the build goes to `ROADMAP.md` §Candidate/deferred, never silently into v0.1.0 (scope freeze).