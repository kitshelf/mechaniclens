# Changelog

All notable changes to MechanicLens. Dates are ISO; the format follows Keep a Changelog.

## [Unreleased]

### Added

- **Structure** — the kit scaffold: charter, conventions, shared DNA, PRD, workflow skeleton, and the documentation set.
- **The estimate workflow** — `estimate/`: the seven-step sequence (redact → anatomy → symptom check → label → question script → decision → after-repair), with `SPINE.md` as the one-paste kit.
- **Shared material** — the three labels, the line-vocabulary glossary (`shared/anatomy.md`), the document types, the redaction pass, the local-model guidance, and the after-repair branch.
- **The pattern library** — 32 patterns across fees, labor, parts, scope, documentation, and machine-directed text, each with a source, a "verified as of" date, a good-answer guide, and a not-a-pattern-when line.
- **Tests** — 15 synthetic fixtures with answer keys (9 pattern, 3 near-miss, 1 injection, 2 behavior), a pattern-to-fixture map covering all 32 patterns, and a consistency checker (`tests/verify_fixtures.py`).
- **Corpus** — 54 US/Canada datasets, 1,272,956 records, with a manifest, a tuning log, and a citation checker (`corpus/verify.py`).

### Status

Recorded runs: 5 of 15 hosted author runs. The kit is specified and internally checked; it is not yet tested, and nothing is released.
