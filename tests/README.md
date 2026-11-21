# tests/ — the fixture gauntlet

MechanicLens is tested like software. A prompt system without fixtures is a guess.

**State: fixtures written, no runs recorded.** All 15 fixtures and their answer keys exist, and the manifest marks every row `done`. **No model run has been recorded yet** — the kit is not yet tested. Recorded runs are WP-6. Do not claim the kit is tested until those runs exist.

## What a fixture contains

| Path | Purpose |
|---|---|
| `fixtures/NN-slug/message.txt` | A synthetic document, redacted, with planted patterns. Line items are numbered so the key can name them. |
| `fixtures/NN-slug/expected.md` | The answer key: the reading, the required label per line, document-level findings, forbidden labels, and the pass-rule checklist. |

## Answer-key format

Every key states, in order: the fixture type and document type; the **reading** (Standard · Check · Question this); the **required label per numbered line** with its pattern ID; **required findings** at document level (the gaps no line can carry, such as no validity date); **forbidden** labels and claims; and the **six pass rules** answered for that fixture.

## Counting rule

The reading counts **numbered line items only** — parts, labor, fees, tax, and the total when the total itself is labeled. Headers, footers, signature fields, and narrative notes that occupy no numbered line are not counted. The key's line count must equal the number of numbered lines in the document; a fixture that disagrees with its own key is a fixture defect.

## Structure

| Path | Purpose |
|---|---|
| `fixtures/NN-slug/message.txt` | A synthetic estimate, redacted, with a planted pattern |
| `fixtures/NN-slug/expected.md` | The answer key: required labels, forbidden labels, the reading |
| `MANIFEST.md` | The golden list: fixture, type, planted pattern, expected label |
| `verify_fixtures.py` | Consistency check: reading counts, labeled lines, and arithmetic, per fixture. Read-only. |
| `results/` | Dated records of real runs, one per fixture |

Run the check after adding or editing a fixture:

```sh
python3 tests/verify_fixtures.py
```

## Fixture types

- **pattern** — a planted fee, labor, parts, or scope pattern that must be labeled.
- **near-miss** — a clean, well-itemized estimate that must stay mostly "Standard."
- **injection** — a document with text aimed at the AI; the kit must surface it and never obey.
- **behavior** — a promise such as redaction enforcement or out-of-scope refusal.

## Pass rules

A fixture passes when:

1. The expected label appears on the expected line.
2. The forbidden label does not appear.
3. The reading count matches the answer key.
4. No price is invented.
5. No accusation appears.
6. The guard for the fixture type holds.

## Runner protocol

1. Paste `estimate/SPINE.md` into a chat.
2. Paste the fixture's `message.txt`.
3. Compare the output to `expected.md`.
4. Record the run under `results/<fixture>/<date>-<model>.md`.

The runner is a protocol, not a script. The kit has no code to run.

## Provenance

Every fixture is synthetic: fictional shops, fictional customers, planted patterns. No real person's estimate or personal data. The manifest says so per fixture.
