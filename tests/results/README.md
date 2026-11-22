# Results

Dated records of real runs against the synthetic fixtures. **One folder per model, then one per fixture:**

```
results/<model-slug>/<fixture>/<date>-<mode>.md
```

For example `results/qwen3-5-9b-mlx-4bit/01-scope-mismatch/2026-11-22-quick.md`.

The model is in the directory name so a model's whole record sits in one tree: its pass rate, its failures, and its drift over time are readable without opening files. The file name carries the date and the mode (`quick` = SPINE only, `full` = the workflow files + rubric).

Each file holds the model's full report, a `## Run` block (model requested and model reported, endpoint, mode, temperature, runner, date, input hashes), and an authored `## Self-assessment` block. Record failures too — a kit that publishes only its passes is not tested.

## What a captured run contains

A run is captured, not summarised. Each run owns three files:

| File | Holds |
|---|---|
| `<date>-<mode>.md` | the model's **verbatim** response, the `## Run` block, and the authored `## Self-assessment` |
| `<date>-<mode>.prompt.txt` | the **exact input**: the system text sent and the fixture message, delimited `=== SYSTEM ===` / `=== USER ===` |
| `<date>-<mode>.meta.json` | sha256 of the system and user text, the model id the server **reported**, temperature, max_tokens, endpoint, usage, finish reason, runner |

A file with no `.prompt.txt` and no `.meta.json` is a **summary**, not evidence: it says what someone concluded, not what the model was given or said. The five `glm-openrouter` files predate capture and are marked as summaries in their own headers.

## Recorded so far

| Model | Type | Runs |
|---|---|---|
| `glm-openrouter` | hosted author runs | 5 of 15 (fixtures 01–05) |
| `qwen3-5-9b-mlx-4bit` | local, oMLX | none saved yet |
| `qwen3-5-4b-4bit` | local, oMLX | none saved yet |
| an OpenRouter model | hosted, independent | **blocked — no API key in the environment** |