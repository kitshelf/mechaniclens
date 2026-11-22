# The estimate workflow

The kit's one workflow: read a repair estimate the way a careful friend would — line by line, in plain English, labeled Standard / Check / Question this, with the questions to ask at the counter. It never quotes a price and never accuses a shop.

Who it is for: anyone holding a repair estimate they are about to approve or decline.

## Files

| Path | What it is |
|---|---|
| `SPINE.md` | The compiled kit: the whole workflow in one paste |
| `START.md` | The chat-user front desk |
| `AGENTS.md` | The agent entry point |
| `00-principles.md` | The workflow's constitution |
| `01-estimate/estimate.md` | The full workflow: steps, output template, self-check |
| `rubrics/patterns-estimate.md` | The estimate pattern library and question scripts |
| `examples/` | Worked examples, when written |

Shared material: `../shared/labels.md`, `../shared/anatomy.md`, `../shared/document-types.md`, `../shared/redaction.md`, `../shared/after-repair.md`, `../shared/local-models.md`.

## How to use it

**Paste mode:** open any chat, paste `SPINE.md`, then paste the redacted estimate and the symptom story. Two pastes.

**File mode:** an agent reads `AGENTS.md`, then `00-principles.md`, then `01-estimate/estimate.md` with the rubric.

## Status

**Shipped in v0.1.0.** The workflow is written, the pattern library is calibrated (32 patterns, all exercised by the fixtures), and the 15 fixtures with answer keys are in place. Two hosted models ran the full gauntlet against this kit — see [`../docs/learnings/CONCLUSION.md`](../docs/learnings/CONCLUSION.md). Release: [`v0.1.0`](https://github.com/kitshelf/mechaniclens/releases/tag/v0.1.0) · [`PyPI`](https://pypi.org/project/mechaniclens/) (`pip install mechaniclens`).
