# docs/learnings/ — what building MechanicLens taught

The grounded record of what development, corpus research, and model testing actually taught — and what changed in the product as a result. Learnings are appended, never rewritten: a superseded learning is marked, not deleted.

## The grounding rule

Every learning here cites its artifact — a file, a fixture, a recorded run, a corpus count. Nothing is asserted from memory. If the evidence is not in the kit, it is not a learning; it is an opinion, and it does not belong here.

## Entry format

| Field | What it holds |
|---|---|
| **Learning** | One or two sentences: what was learned |
| Evidence | The artifacts that ground it — paths, fixtures, runs, counts |
| Change | What changed in the product, and in which file — or "candidate," honestly, if nothing changed yet |

## Read in this order

| Doc | What it captures |
|---|---|
| [`01-corpus.md`](01-corpus.md) | **Scoping, building, and reading the corpus** — the US/Canada rule, the missing estimate/invoice dataset, the home/auto asymmetry, text-only as doctrine, row-level inspection, the safe side as the stronger teacher, prices as context, and what searching honestly does to a "no source" claim (L1–L7, L10, L11, L15) |
| [`02-kit-design.md`](02-kit-design.md) | **The shape of the kit** — the rubric's axis is line anatomy not domain, home is a document type rather than a subcategory, one owner per vocabulary, and how far a one-owner rule actually reaches (L9, L14, L16) |
| [`03-record.md`](03-record.md) | **Keeping the record honest** — derived artifacts drift, a count must be re-derivable, a status row is a claim, and a ratio target moves when its denominator does (L8, L12, L13) |
| [`04-fixtures.md`](04-fixtures.md) | **Building the fixture gauntlet, recording the runs** — a reading is derived not typed, a line-label table cannot carry document-level patterns, a behavior fixture is not a document fixture with the labels removed, a green checker is the floor, a fixture plants every pattern its wording supports, and a run by the key's author is a satisfiability check, not a validation (L17–L22) |
| [`05-local-models.md`](05-local-models.md) | **Running the gauntlet on a local model** — the 4B transcribes perfectly and judges weakly, the ceiling label is where it collapses, it labels per line and never across the document, it invents reasonableness Checks, and (full set) it breaks the redaction gate, over-flags clean documents, issues Approve/Decline verdicts in every run, and its Reading line disagrees with its own label table in 10 of 15 runs (L25–L33); plus a reasoning model exhausts `max_tokens` in `reasoning_content` before it answers, which gates the 9B run (L34) |

### Per-model record files

Model-specific validation records live alongside the learnings, named with the model id so the LLM identity is preserved in the filename. The raw run artifacts (`.md`, `.prompt.txt`, `.response.json`, `.meta.json` per fixture) stay under `tests/results/<provider>/<llm>__<version>/` and are not duplicated here. The validator flags pre-fix runs as `spine-drift` when the run's recorded `system_sha256` does not match the current `estimate/SPINE.md`. Authored summaries were removed in favor of L40 in `05-local-models.md`, which records the post-fix confirmation in one place.

| File | Model | Status | What it holds |
|---|---|---|---|
| [`claude-haiku-5-5__validation.md`](claude-haiku-5-5__validation.md) | `anthropic/claude-haiku-5.5` (OpenRouter) | **current** | 15 fixtures post-fix. 09 refuses the unredacted paste (gate holds). Near-miss 14 all-Standard; 07/15 have one real finding each, not invented |
| [`gpt-6-luna__validation.md`](gpt-6-luna__validation.md) | `openai/gpt-6-luna` (OpenRouter) | **current** | 15 fixtures post-fix. 09 refuses (gate holds). All three near-miss fixtures (07/14/15) all-Standard — over-flagging fixed. 06 produced no report (real model miss) |
| [`qwen3-4b-instruct-2507-4bit__validation.md`](qwen3-4b-instruct-2507-4bit__validation.md) | `Qwen3-4B-Instruct-2507-4bit` (oMLX, 4bit) | **dropped — too slow** | Pre-fix 15 fixtures, 0/15 pass. Historical baseline |
| [`qwen3-4b-instruct-2507-4bit__summary.md`](qwen3-4b-instruct-2507-4bit__summary.md) | `Qwen3-4B-Instruct-2507-4bit` (oMLX, 4bit) | dropped — too slow | Pre-fix authored verdict. Kept as baseline |
| [`glm-flash-latest__validation.md`](glm-flash-latest__validation.md) | `~z-ai/glm-flash-latest` → `z-ai/glm-5.3-flash` (OpenRouter) | **dropped — too slow** | Pre-fix 4 + post-fix 1. Historical only |

Companion documents in [`../`](../README.md): [`../HOW-BUILT.md`](../HOW-BUILT.md) (the corpus build, step by step) and [`../HOW-IT-WORKS.md`](../HOW-IT-WORKS.md) (the kit, end to end).

## Status

Living record. New learnings append with the next number in their file, filed under the section of work they belong to; each file's entries are numbered (L#, D#) so other documents can cite them. The `L` numbers are the append order and never renumber — the sections group them by subject, so the file reads both as an index and as a history.