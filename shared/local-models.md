# Running MechanicLens on a local model

The kit is Markdown and runs in any chat. Local models were tested during v0.1.0 and **dropped as too slow to be usable** — a 4B Instruct took ~21 s per fixture and labeled weakly; a reasoning 4B spent its entire token budget thinking and never answered. Both findings are recorded in [`docs/learnings/05-local-models.md`](../docs/learnings/05-local-models.md) (L25–L34).

The kit itself runs anywhere a long paste is accepted. What does not work today is the *local* path being practical: the models that fit on a laptop are too small to label well, and the ones that label well take too long. Use a hosted model (Claude Haiku 5.5 or GPT-6 Luna, both under $0.01 per decode) until faster local hardware or smaller capable models change this.

The rest of this file documents the local path for anyone who wants to try it anyway or who has faster hardware than was tested.

## Which runtimes work

Any local runtime that accepts a long paste works: Ollama, LM Studio, llama.cpp, OMLX/MLX, and similar. The kit does not depend on tool calls, function definitions, or provider-specific syntax.

## The honest model floor

Small local models under-detect. They may miss a fee-stacking pattern, misread a labor line, or flatten a "Question this" into "Standard." The kit's guidance is the same as the shelf's: if the model cannot quote the line it is labeling, do not trust the label. Re-run the decode on a stronger model, or use the kit as a reading aid and verify each question yourself.

The kit does not certify a model. A clean decode is not a guarantee that the estimate is complete or fair.

## How to run it

1. Open the local model's chat.
2. Paste `estimate/SPINE.md`.
3. Paste the redacted estimate text and your symptom story.
4. Read the reading, the labels, and the question script.

No network call is required at any step. If a runtime tries to fetch a link, stop; the kit never asks it to.
