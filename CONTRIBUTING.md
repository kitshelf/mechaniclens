# Contributing

MechanicLens is Markdown. Contributions are Markdown changes. Read the [charter](WHAT-THIS-IS.md) first; it overrides this file.

## The most useful contribution: a pattern

A pattern is a line-level tell in an estimate that the kit should label. A pattern enters the library only with three things:

1. **The exact wording** — a short, redacted example of the line as it appears.
2. **A not-a-pattern-when line** — the legitimate case the pattern must not fire on. This is what keeps the kit calibrated.
3. **A source** — a public reference, a repair-industry document, a consumer-protection guide, or a recorded example. Say where it comes from.

Open a [pattern submission](.github/ISSUE_TEMPLATE/pattern-submission.md). Do not paste a real estimate with personal data; redact it first.

## Rules that never change

- **No prices.** The kit never quotes, estimates, or compares market prices. A contribution that adds a price table is rejected.
- **No accusations.** The ceiling label is "Question this." A contribution that calls a shop a scam is rejected.
- **Evidence quoted.** Every label quotes the document's line.
- **Fixed labels only.** Standard / Check / Question this. No scores or percentages.
- **Offline-complete.** No step may require a network call.
- **Plain prose.** No marketing voice, no intensifiers, no filler.

## Changing a rubric or a pack

Follow [`CONVENTIONS.md`](CONVENTIONS.md) §Building a new document type. Nothing auto-enters: a pattern needs its calibration line, a source, and a fixture that exercises it. When a rubric changes, `SPINE.md` must change with it — the quick and full modes must stay in sync.

## Adding a fixture

Fixtures are synthetic. Fictional shops, fictional customers, planted patterns. Write the expected key before the document. Add the row to [`tests/MANIFEST.md`](tests/MANIFEST.md). Keep the calibration habit: for every two patterned fixtures, keep at least one near-miss clean estimate.

## Commits

One change per commit, plain message. Never commit anything from `my-files/`.
