# Running MechanicLens on a local model

The kit is Markdown. It runs in any chat, including a local model that never touches the network. This matters when the estimate carries your name, address, or VIN.

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
