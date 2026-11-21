# corpus/ — the US/Canada repair research library

Public **US/Canada** auto-repair and household-repair corpora, vendored under redistributable licenses, plus a full index of the Hugging Face surface. This is the material the pattern library is researched against and the calibration reference the synthetic fixtures are judged by.

## The boundary (read this first)

| Tier | Where | What it is | Used for |
|---|---|---|---|
| Synthetic fixtures | `tests/fixtures/` | Invented estimates, planted defects | The gauntlet — the kit is tested here |
| External corpora | `corpus/` (this folder) | Public US/Canada datasets, downloaded as-is, text-only | Pattern research, calibration review |
| Runtime | — | A user's pasted estimate | The decode. The kit never reads this folder during a screen |

The kit does not train on this corpus. The charter says **not a trained model**, and it stays that way.

## Geography rule

**US/Canada only.** Datasets from other countries are excluded on purpose — they pollute the calibration with different fee structures, labour rates, inspection regimes, and document formats. If a dataset is global or synthetic English with no country signal, it is excluded unless it is clearly US/Canada-shaped. The 2026-11-21 pass removed the India and Australia sets for this reason.

## What is vendored — 54 datasets

US/Canada only. Grouped by area; the full per-dataset table (id, license, rows, notes) is in [`MANIFEST.md`](MANIFEST.md).

| Area | Datasets | Records | What it covers |
|---|---|---|---|
| Auto — diagnostics & repair procedures | 4 | ~17k | OBD-II codes, DTCs, repair procedures, replacement parts, OEM maintenance schedules |
| Auto — complaints & recalls | 7 | ~1.1M | NHTSA complaints, recalls, owner reports, CPSC consumer recalls |
| Auto — shops, liens, insurance, parts | 6 | ~82k | body-shop directory, mechanic liens, insurance minimums, abandoned-vehicle rules, discontinued-part mapping |
| Home — inside the house | 8 | ~11k | plumbing, HVAC, appliance, electrical, water quality, septic |
| Home — outside the house | 12 | ~24k | roofing, siding, gutters, exterior market data, permits, foundation, deck, fence, land clearing |
| Home — contractor & licensing | 7 | ~22k | contractor directories, license thresholds, licensing stats |
| Home — repair cost registers | 10 | ~1k | chimney, well, foundation, retaining wall, insulation, bulkhead, water, septic |

The auto lane is deep on **symptoms and diagnostics** (what breaks, what codes fire, what owners complain about); the home lane is deep on **trades, licensing, permits, and cost indices**. Neither lane contains actual repair *estimates* or *invoices* at scale — that gap is why the kit's fixtures are synthetic.

Per-dataset provenance, exact ids, and the full removal record: [`MANIFEST.md`](MANIFEST.md). Every directory carries the source's own card as `README.md`.

## The full surface index

[`INDEX.md`](INDEX.md) + [`index.json`](index.json) index **930 datasets** across Hugging Face for this domain. Pull one on demand:

```sh
python3 corpus/fetch.py <dataset-id>
```

Some datasets ship as parquet. Convert those to text on fetch (`convert.py` writes `.json` + `.md`; binaries are never kept):

```sh
python3 corpus/convert.py <dataset-id>
```

## The learn-from protocol

1. **Sample** the US/Canada side of a corpus — complaints, DTCs, maintenance schedules, home-repair Q&A.
2. **Find recurring tells** — fee names, labour phrasing, parts language, scope patterns, diagnostic phrasing.
3. **Draft the candidate pattern** — name, category, tell, counter-question, and the mandatory *not-a-pattern-when* calibration line.
4. **Test it against fixtures** — a pattern enters the rubric only with a source, a calibration line, and a fixture that exercises it. Nothing auto-enters.
5. **Record the pass** in [`TUNING.md`](TUNING.md): counts, calibration findings, gaps.

## Rules for this folder

- **Text formats only.** `.csv`, `.json`, `.jsonl`, `.md`, `.tsv`. Binaries never come in as binaries — parquet converts to `.json` first (`convert.py`); model artifacts and images are dropped.
- **US/Canada only.** No other-country datasets. No global sets unless clearly US/Canada-shaped.
- **No gated datasets.** A 401 means it does not come in.
- **No mirrors.** Datasets are deduplicated by content hash before vendoring.
- Never add a corpus without license and provenance in `MANIFEST.md`. An unclear license means it does not come in.
- Never use corpus material as a fixture, and never paste corpus text into a user's report.
- Keep the manifest accurate: row counts, dates, exact Hugging Face ids.
