# tests/ — the fixture gauntlet

MechanicLens is tested like software. A prompt system without fixtures is a guess.

**State: NOT YET RUN.** The fixtures and answer keys are planned but not written. The manifest marks every row `planned`. Do not claim the kit is tested until the runs exist.

## Structure

| Path | Purpose |
|---|---|
| `fixtures/NN-slug/message.txt` | A synthetic estimate, redacted, with a planted pattern |
| `fixtures/NN-slug/expected.md` | The answer key: required labels, forbidden labels, the reading |
| `MANIFEST.md` | The golden list: fixture, type, planted pattern, expected label |
| `results/` | Dated records of real runs, one per fixture |

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
