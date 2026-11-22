# Changelog

All notable changes to MechanicLens. Dates are ISO; the format follows Keep a Changelog.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Current release:** [v0.1.0](https://github.com/kitshelf/mechaniclens/releases/tag/v0.1.0) · [PyPI](https://pypi.org/project/mechaniclens/) (`pip install mechaniclens`)

## [0.1.0] 2026-11-22

### Added

- **Structure** — the kit scaffold: charter, conventions, shared DNA, PRD, workflow skeleton, and the documentation set.
- **The estimate workflow** — `estimate/`: the seven-step sequence (redact → anatomy → symptom check → label → question script → decision → after-repair), with `SPINE.md` as the one-paste kit.
- **Shared material** — the three labels, the line-vocabulary glossary (`shared/anatomy.md`), the document types, the redaction pass, the local-model guidance, and the after-repair branch.
- **The pattern library** — 32 patterns across fees, labor, parts, scope, documentation, and machine-directed text, each with a source, a "verified as of" date, a good-answer guide, and a not-a-pattern-when line.
- **Tests** — 15 synthetic fixtures with answer keys (9 pattern, 3 near-miss, 1 injection, 2 behavior), a pattern-to-fixture map covering all 32 patterns, and a consistency checker (`tests/verify_fixtures.py`).
- **Runner** — `tests/run_local.py`: runs the gauntlet against a local or hosted model, saves the exact input, the raw response verbatim, and a metadata block (provider, model requested and reported, version, hashes, usage). Keys come from an environment variable, never a flag.
- **Validator** — `tests/validate_results.py`: deterministic per-fixture checks against the answer keys — capture integrity, template sections, label-vs-key misses, internal consistency, compliance flags — and flags runs made against a stale kit (`spine-drift`).
- **Worked examples** — `estimate/examples/01-the-catch.md` (a planted pattern) and `02-the-not-catch.md` (a clean estimate that stays clean).
- **User guide** — `USER-GUIDE.md`: the ninety-second walkthrough, the labels, the questions, the won't-do list, the after-repair branch, and a redaction before/after sample.
- **Corpus** — 54 US/Canada datasets, 1,272,956 records, with a manifest, a tuning log, and a citation checker (`corpus/verify.py`).
- **Learnings** — `docs/learnings/`: the grounded record of what building and testing taught, L1–L45 across five files.

### Changed

- **Five kit fixes driven by the fixture gauntlet** (`estimate/SPINE.md`): removed the approve/decline rubric the charter forbids; linked the Scope check to the labels; made Standard the default so absence of information is not a finding; made redaction a gate rather than a request; restored P-1 (parts tier unstated) and gave the after-repair branch its own labelling rule. See `docs/learnings/05-local-models.md` L35–L45.

### Testing

Recorded runs: two hosted models ran the full 15-fixture gauntlet against the fixed kit.

| Model | Labels correct | Perfect fixtures | Cost |
|---|---|---|---|
| `anthropic/claude-haiku-5.5` | 73/92 (79%) | 5 | $0.029 |
| `openai/gpt-6-luna` | 74/92 (80%) | 6 | $0.016 |

Local models and `~z-ai/glm-flash-latest` were tested and dropped: too slow to be usable. The kit's structural rules — redaction gate, no approve/decline, scope findings reaching the labels, clean estimates staying clean, the after-repair branch — hold on both hosted models. Per-model validation records are in `docs/learnings/`.
