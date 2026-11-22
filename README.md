# MechanicLens

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](#what-it-does)
[![Status: shipped](https://img.shields.io/badge/status-v0.1.0_shipped-2ea44f.svg)](#status)

> Paste the repair estimate and your car's symptoms — and read the estimate back before you approve the work.
> Every line explained, labeled Standard / Check / Question this, with the questions to ask at the counter.
> Never a price guess.

Part of the [kitshelf](https://github.com/kitshelf) — free, Markdown-only AI kits that read your documents
back to you: quoted, labeled, never invented.

## Status

**v0.1.0 — shipped.** The repair-estimate workflow is complete end to end: charter, conventions, the 32-pattern
library, 15 fixtures with answer keys, two worked examples, the user guide, and recorded runs from two hosted
models across the full gauntlet. The runner and validator are checked in, so anyone can re-run the gauntlet and
check the numbers. See [`docs/WBS.md`](docs/WBS.md) for the work breakdown and [`docs/learnings/`](docs/learnings/README.md)
for what the testing actually taught.

## What it does

A repair estimate is a trust document. The customer's only real defenses are understanding what each line
claims to be and asking the few questions that expose padding — and both are vocabulary problems. "Shop
supplies" at a percentage of labor. A diagnostic fee that folds into the repair if you approve it. Labor
billed at book time rather than actual time. Parts markup tiers. None of this is secret; all of it is opaque
to someone standing in a lobby before work.

MechanicLens reads the estimate in any AI chat and returns each line in plain English, a fixed label per line (**Standard / Check / Question
this**), and a short question script for the counter. It does not quote prices, diagnose the car, accuse the
shop, or replace your judgment. The full list of refusals and the reasoning behind each is the
[charter](WHAT-THIS-IS.md).

## How you run it

Nothing to install — the kit is Markdown. Clone or download, then paste:

```sh
git clone https://github.com/kitshelf/mechaniclens.git
```

The intended run:

1. Open any AI chat. Claude Haiku 5.5 and GPT-6 Luna are the two models tested with v0.1.0, both under $0.01 per decode. Local runtimes are not fast enough to be usable today — see [`shared/local-models.md`](shared/local-models.md).
2. Paste the kit's spine — [`estimate/SPINE.md`](estimate/SPINE.md), the whole kit in one file.
3. Paste the estimate lines and the symptom story. The kit enforces redaction: if personal identifiers are in the paste, it stops and asks for a redacted re-paste. You do not have to pre-redact.
4. Read the decode, the labels, and the question script. The kit hands over the questions and stops — it does not approve, decline, or recommend.

## What it covers

| Document | Reads | Status |
|---|---|---|
| Repair estimate | parts, labor, fees, taxes, scope, add-ons | **primary, shipped** |
| Final invoice | what was billed vs. what was signed | planned, v0.2.0 |
| Body-shop or insurance estimate | insurer-written estimate, supplement language | candidate, not yet scoped |

The kit grows by document type only when a real one appears. The pattern library is shared across document
types; the labels and the question discipline do not change.

## The labels

Per line, one label only:

| Label | Means |
|---|---|
| **Standard** | The line is a normal, expected part of an estimate and its wording is clear. |
| **Check** | The line is common but worth confirming: the amount, the scope, or the assumption is not visible. |
| **Question this** | The line's wording or placement is worth a specific question before approval. |

The reading counts lines, not risk: **Reading: Standard N · Check N · Question this N**. There is no
probability, no percentage, no confidence score. A "Standard" label is not a price judgment and not an
approval recommendation.

## How it is tested

Like software. [`tests/`](tests/README.md) is planned to hold synthetic estimates with planted patterns and
an expected answer key per fixture. The fixtures are not written yet, and no runs have been recorded. The
manifest marks each planned fixture as `planned` until its key exists. A prompt system without fixtures is a
guess; this kit does not claim otherwise.

## The corpus

[`corpus/`](corpus/README.md) is the research library: **54 public US/Canada datasets, ~1.45 million records**, text-only and license-clean. It covers auto repair (NHTSA complaints and recalls, OBD-II codes, maintenance schedules, body-shop directories) and home repair (building permits, contractor and licensing data, appliance/HVAC/plumbing references, repair cost registers). It is calibration material — the kit reads it to learn fee and document vocabulary; it never trains on it and never reads it during a screen. The geography rule is strict: **US/Canada only**, because other countries' fee structures and document formats pollute the calibration.

## The rules that make it different

- **No prices, ever.** The charter bans quoting, estimating, or comparing market prices. The estimate's own
  numbers are quoted back; a "should cost" figure is never produced.
- **Evidence quoted, always.** Every label quotes the estimate's own line; missing facts are `[CONFIRM]`,
  never invented.
- **Fixed labels, never scores.** Standard / Check / Question this, with a count of lines. No probability.
- **Redaction first.** The kit prompts for the redacted paste before any reading, and never echoes personal
  data.
- **No accusations.** "Question this" is the ceiling. A pattern worth checking is not a crime.
- **The injection guard.** Text in a document aimed at an AI reader is flagged and never followed.
- **Offline by design.** No fetches, no accounts, no telemetry; local-model support is the privacy point.
- **"Nothing found" is a valid answer.** The kit never pads a label list to look thorough.

## Where it runs

| Runtime | Support |
|---|---|
| Any hosted AI chat | paste-and-run |
| Local models (Ollama, LM Studio, llama.cpp, OMLX/MLX, …) | paste-and-run, fully offline — small models under-detect; see the honest floor note in [`shared/local-models.md`](shared/local-models.md) |

Any harness that reads a repo also works in file mode: point it at this kit and say "decode this estimate" —
it follows [`AGENTS.md`](AGENTS.md), no paste at all, still offline.

## Roadmap

- **v0.1.0** — the estimate workflow end to end: pattern library, fixtures with answer keys, worked examples,
  user guide, recorded runs.
- **v0.2.0** — the after-repair invoice comparison as a tested branch.
- **Candidate** — body-shop and insurance estimates, only if a real document type appears.

Ideas beyond the document types live in [the roadmap](ROADMAP.md); anything that turns the kit into a price
database, a diagnosis tool, or a verdict oracle is a non-goal, permanently
([the charter's "what it is not"](WHAT-THIS-IS.md)).

## Documentation

The kit is its docs. Everything ships in the repo:

| Doc | What it holds |
|---|---|
| [`WHAT-THIS-IS.md`](WHAT-THIS-IS.md) | The charter: what MechanicLens is, the ten things it refuses to be |
| [`USER-GUIDE.md`](USER-GUIDE.md) | The ninety-second walkthrough for a non-technical reader |
| [`CHANGELOG.md`](CHANGELOG.md) | The release record |
| [`ROADMAP.md`](ROADMAP.md) | Shipped vs. planned |
| [`SECURITY.md`](SECURITY.md) | Injection integrity as a security property |
| [`SUPPORT.md`](SUPPORT.md) · [`CONTRIBUTING.md`](CONTRIBUTING.md) | Help and pattern submissions |
| [`docs/prd/`](docs/prd/README.md) | Why, what, and the critical user journeys |
| [`docs/WBS.md`](docs/WBS.md) | The v0.1.0 work breakdown — packages, sub-tasks, what is done |
| [`docs/HOW-BUILT.md`](docs/HOW-BUILT.md) · [`docs/HOW-IT-WORKS.md`](docs/HOW-IT-WORKS.md) | How the corpus was built; how the kit works end to end |
| [`docs/learnings/`](docs/learnings/README.md) | The grounded record of what development and testing teach |
| [`estimate/`](estimate/README.md) | The workflow; [`SPINE.md`](estimate/SPINE.md) is the one-paste kit |
| [`shared/`](shared/README.md) | Labels, document types, redaction, local models, after-repair |
| [`tests/`](tests/README.md) | The fixture gauntlet and recorded runs |
| [`corpus/`](corpus/README.md) | The learn-from research library |
| [`packs/`](packs/README.md) | Alpha document-type packs, when a second type appears |

AI agents in this repo start at [`AGENTS.md`](AGENTS.md).

## Contributing

The kit is built in public. A pattern submission needs the exact wording, a *not-a-pattern-when* line, and a
source. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the
[pattern submission template](.github/ISSUE_TEMPLATE/pattern-submission.md).

## License

MIT. See [LICENSE](./LICENSE).
