# WBS — the v0.1.0 work breakdown

The build plan for MechanicLens v0.1.0, decomposed into work packages with sub-tasks, acceptance conditions, and status. This is the working checklist; [`../ROADMAP.md`](../ROADMAP.md) stays the shipped/planned record and [`../CHANGELOG.md`](../CHANGELOG.md) the release record. When a package finishes, flip its status here and its roadmap line in the same breath.

**Status legend:** ✅ done · 🔶 partial (open items listed) · ⬜ not started

---

## Summary

| WP | Package | Status | Blocked by |
|---|---|---|---|
| 0 | Foundation scaffold | ✅ committed & pushed | — |
| 1 | Corpus | ✅ on disk · 🔶 **uncommitted** | your go |
| 2 | Pattern library (rubric completion) | ✅ calibrated — 32 patterns, 12 brief-sourced | 1 |
| 3 | Estimate-anatomy glossary | ⬜ | — (independent) |
| 4 | Fixtures + answer keys | ⬜ manifest only | 2 |
| 5 | Worked examples | ⬜ README placeholder | 4 |
| 6 | Recorded runs | ⬜ none | 4 |
| 7 | User guide completion | 🔶 redaction sample open | — |
| 8 | Release + article | ⬜ | 2–7 |

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
| 0.6 | Shared material: [`../shared/`](../shared/README.md) `labels.md`, `document-types.md`, `redaction.md`, `local-models.md`, `after-repair.md` | ✅ |
| 0.7 | Roadmap: v0.1.0 scope + freeze, v0.2.0 / v0.3.0 one-liners, deferred + non-goals | ✅ |
| 0.8 | Sync fixes: **M-1** injection marker added to the rubric (30 patterns at that commit; 32 after the 2026-11-21 revisit), charter #2 reword, canonical `Reading:` line | ✅ |

---

## WP-1 — Corpus — ✅ DONE on disk · 🔶 UNCOMMITTED

| # | Item | Status |
|---|---|---|
| 1.1 | Rules fixed before any download: text-only, US/Canada only, redistributable-only | ✅ |
| 1.2 | Sweep + index: **930 datasets** in [`../corpus/index.json`](../corpus/index.json) / [`INDEX.md`](../corpus/INDEX.md) | ✅ |
| 1.3 | **54 US/CA datasets vendored**, ~**1.43M records**, ~205 MB — India + Australia sets removed, removals recorded in the manifest | ✅ |
| 1.4 | Tooling: [`fetch.py`](../corpus/fetch.py) (text files only, provenance card kept) + [`convert.py`](../corpus/convert.py) (parquet → `.json` + `.md`, index artifacts dropped) | ✅ |
| 1.5 | Corpus docs: [`README.md`](../corpus/README.md), [`MANIFEST.md`](../corpus/MANIFEST.md) (per-dataset provenance + removal + rejection records), [`TUNING.md`](../corpus/TUNING.md) | ✅ |
| 1.6 | Verify pass: zero non-text files on disk; counts reconciled (index 930 / vendored 54; README lane table matches the recount) | ✅ |
| 1.7 | **Commit + push the corpus batch** (54 dataset dirs, index, docs, root-README corpus section) | 🔶 **awaiting your go** |

**Acceptance.** `git status` clean on `corpus/` and the corpus section of the root README pushed; manifest counts match disk.

---

## WP-2 — Pattern library: finish the rubric — ✅ DONE (calibrated 2026-11-21; re-measured the same day with `corpus/verify.py`, pass 2 in `corpus/TUNING.md`)

[`../estimate/rubrics/patterns-estimate.md`](../estimate/rubrics/patterns-estimate.md) holds **32 patterns** — F-1…F-7 (fees), L-1…L-6 (labor), P-1…P-7 (parts), S-1…S-5 (scope), D-1…D-6 (documentation), M-1 (machine-directed text) — each with *what to look for*, a *question to ask*, and a ***not-a-pattern-when*** line.

| # | Item | Status |
|---|---|---|
| 2.1 | **Source per pattern** — each pattern cites the corpus dataset (e.g. S-2 ← OEM maintenance schedules, F-6 ← abandoned-vehicle timelines) or fixture that seeds it, per the grounding rule | ✅ 32/32 (20 corpus-sourced, 12 brief) |
| 2.2 | **"Verified as of" date per pattern** — dated so drift is detectable; re-verification is a v0.3.0 roadmap item, the first dating happens here | ✅ 2026-11-21 |
| 2.3 | **Good-answer guide per pattern** — "what a good answer sounds like," one per pattern, so a question's answer is checkable against the paper | ✅ 30/30 |
| 2.4 | *Not-a-pattern-when* calibration line | ✅ all 30 written |
| 2.5 | Flip the header status line from "draft" to calibrated | ✅ |

**Acceptance.** No pattern lacks source + date + good-answer guide; every fixture's planted pattern (WP-4) cross-references its rubric ID.

---

## WP-3 — Estimate-anatomy glossary — ⬜ NOT STARTED

Step 2 of [`estimate.md`](../estimate/01-estimate/estimate.md) maps the document inline; the standalone plain-English glossary does not exist yet.

| # | Item |
|---|---|
| 3.1 | Name every line category: parts (name / number / quantity / unit price), labor (operation / hours / rate), fees (diagnostic, shop supplies, environmental, hazmat, disposal, administrative, storage), taxes, total-as-written |
| 3.2 | Decide the home: extend `estimate.md` Step 2 or a `shared/anatomy.md` — one owner, no parallel copy |
| 3.3 | Cross-link from `USER-GUIDE.md`, [`HOW-IT-WORKS.md`](HOW-IT-WORKS.md) Step 2, and `document-types.md` |

**Acceptance.** Every term used in a label or a question appears in the glossary; nothing is defined twice in two places.

---

## WP-4 — Fixtures + answer keys — ⬜ NOT STARTED (manifest written)

The golden list is [`../tests/MANIFEST.md`](../tests/MANIFEST.md): 8 fixture rows + coverage targets that require 2 more. **Answer keys first** — kitshelf convention.

| # | Item | Status |
|---|---|---|
| 4.1 | **Answer keys first**: `fixtures/NN-slug/expected.md` per fixture — required labels, forbidden labels, the reading count | ⬜ |
| 4.2 | Fixture documents: `fixtures/NN-slug/message.txt` — synthetic shops, redacted, patterns planted | ⬜ |
| 4.3 | Rows 01–08: scope-mismatch · folded-diagnostic · fee-stack · duplicate-parts · while-were-in-there · invoice-differs · clean-estimate (near-miss) · injection-document | ⬜ |
| 4.4 | **09 redaction-enforcement** — behavior fixture: unredacted personal data in → kit refuses, re-asks, never echoes | ⬜ |
| 4.5 | **10 out-of-scope-refusal** — behavior fixture: "what should this cost?" / "what's wrong with my car?" → kit refuses both, per charter | ⬜ |
| 4.6 | **Open decision — near-miss ratio**: the manifest targets *1 near-miss per 2 pattern fixtures*; 6 pattern fixtures ⇒ 3 near-misses; only 07 exists. Either write 2 more near-miss fixtures or re-point the target | ⬜ |
| 4.7 | Flip every MANIFEST row `planned → done`; update the "NOT YET RUN" state line in [`tests/README.md`](../tests/README.md) | ⬜ |

**Acceptance.** All six pass rules in `tests/README.md` are answerable from each key: expected label on the expected line, forbidden label absent, count matches, no price invented, no accusation, type guard holds.

---

## WP-5 — Worked examples — ⬜ NOT STARTED (README placeholder only)

[`../estimate/examples/`](../estimate/examples/README.md) is empty of examples.

| # | Item |
|---|---|
| 5.1 | **The catch** — a decode where a pattern fires: full report (anatomy, labels, question script, decision) shown honestly |
| 5.2 | **The not-catch** — a near-miss where a pattern *almost* fits and correctly stays Standard/Check — the calibration proof |
| 5.3 | Source material: reuse fixture 01 (catch) and 07 (not-catch) from WP-4, or author fresh — consistent with the fixtures either way |

**Acceptance.** A reader who has never run the kit can follow both examples end to end and see why the near-miss stays clean.

---

## WP-6 — Recorded runs — ⬜ NOT STARTED

| # | Item |
|---|---|
| 6.1 | Run the protocol per [`tests/README.md`](../tests/README.md): paste `SPINE.md` → paste `message.txt` → compare to `expected.md` |
| 6.2 | One hosted-model run per fixture, recorded |
| 6.3 | One local-model run per fixture (Ollama / LM Studio), with honest under-detection notes per [`../shared/local-models.md`](../shared/local-models.md) |
| 6.4 | File each as `results/<fixture>/<date>-<model>.md`; then remove the "NOT YET RUN" claim |

**Acceptance.** Every fixture has ≥1 dated recorded run; any mismatch is recorded, not retried into silence.

---

## WP-7 — User guide — 🔶 PARTIAL

[`../USER-GUIDE.md`](../USER-GUIDE.md) exists and reads complete: walkthrough, labels table, question examples, won't-do list, after-repair, privacy.

| # | Item | Status |
|---|---|---|
| 7.1 | Ninety-second walkthrough + labels + won't-do + privacy | ✅ |
| 7.2 | **Redaction sample** — a before/after paste example; the roadmap calls for it, the file does not have it | ⬜ |
| 7.3 | Flip the roadmap line "(stub)" → done when 7.2 lands | ⬜ |

---

## WP-8 — Release + the article — ⬜ NOT STARTED

| # | Item |
|---|---|
| 8.1 | Root README: flip the badge + status block "v0.1.0 in development" → shipped (corpus section already written) |
| 8.2 | [`../CHANGELOG.md`](../CHANGELOG.md): move the Unreleased block under a dated `## [0.1.0] 2026-MM-DD` |
| 8.3 | [`../ROADMAP.md`](../ROADMAP.md): v0.1.0 rows → shipped statuses; run the "done when" check honestly against the fixture gauntlet |
| 8.4 | Tag `v0.1.0`, push, GitHub release |
| 8.5 | **dev.to article** — source material is in this folder: [`HOW-BUILT.md`](HOW-BUILT.md) (the corpus build), [`HOW-IT-WORKS.md`](HOW-IT-WORKS.md) (the machine), [`learnings/01-corpus.md`](learnings/01-corpus.md) (L1–L8) |

**Acceptance.** Tag exists, changelog dated, roadmap accurate, article drafted from the docs — no claim of "tested" anywhere the recorded runs (WP-6) do not support.

---

## Non-goals for this WBS

Price databases, diagnosis, shop ratings, negotiation scripts — permanently out of scope per the charter. Anything new that surfaces during the build goes to `ROADMAP.md` §Candidate/deferred, never silently into v0.1.0 (scope freeze).