# How this was built — the corpus, step by step

The complete build record for [`../corpus/`](../corpus/): how the 54 vendored US/Canada datasets were found, filtered, fetched, converted, and verified. Written so anyone can reproduce the sweep — and so every later addition follows the same rules.

---

## Step 0 — The boundary, before any download

Before the first fetch, three rules were fixed (all now in [`../corpus/README.md`](../corpus/README.md)):

1. **Text only.** `.csv`, `.json`, `.jsonl`, `.md`, `.tsv`. Binaries never enter as binaries — parquet converts to text first; images, model artifacts, and pickles are dropped.
2. **US/Canada only.** Other countries pollute the calibration (see [L1 in the learnings](learnings/01-corpus.md)).
3. **Redistributable licenses only.** CC0, CC-BY, Apache-2.0, MIT, ODbL, and source-terms-cited sets. An unclear license is a hard no; a gated download (401) means the set does not come in.

The kit never trains on any of it (charter: not a trained model) and never reads it during a screen. The corpus is a research and calibration library.

## Step 1 — Sweep the Hugging Face surface

A sweep script queried the Hugging Face datasets API (`/api/datasets?search=…&limit=100&full=true`) across ~100 search terms in five buckets:

| Bucket | Example queries |
|---|---|
| Auto repair | `auto repair`, `vehicle repair`, `repair invoice`, `obd`, `dtc`, `trouble code`, `nhtsa`, `collision` |
| Home — inside | `plumbing`, `hvac`, `appliance repair`, `electrical repair`, `home warranty` |
| Home — outside | `roofing`, `siding`, `gutter`, `fence`, `deck`, `landscaping`, `concrete` |
| Work orders | `work order`, `service ticket`, `repair estimate`, `maintenance request` |
| US/Canada specifics | `us vehicle`, `canada vehicle`, `us home`, `nhtsa`, `vehicle recalls`, `contractor license` |

Every result was deduplicated by dataset id and recorded into [`../corpus/index.json`](../corpus/index.json) with downloads, license tag, size category, and topic tags. Two passes ran (a first broad sweep, then a US/Canada-targeted pass): **930 unique datasets indexed**.

## Step 2 — Filter to candidates

From the index, a candidate had to clear all of:

- **Size ≥ ~1,000 rows** (`size_categories` of `1K<n<10K` or larger) — trivial sets teach nothing.
- **Text-bearing** (`modality:text` or `modality:text` + `modality:tabular`) — image-only and audio-only sets are dropped (the kit reads documents).
- **Redistributable license** — see Step 0.
- **US/Canada relevance** — checked by reading each candidate's README and a sample of rows via the datasets-server API (`/first-rows`). This is where India (property-maintenance tickets) and Australia (mining-equipment triage) were caught and excluded.

Each shortlisted candidate was inspected at the row level before download — columns and a sample row — to confirm it was repair-shaped and not, e.g., collision statistics or robotics data.

## Step 3 — Fetch

[`../corpus/fetch.py`](../corpus/fetch.py) downloads one dataset's text files as-is into `corpus/<org>__<name>/`:

```sh
python3 corpus/fetch.py <dataset-id>
```

It lists the dataset tree (`/api/datasets/<id>/tree/main?recursive=true`), skips every non-text file (printing what it skipped and why), keeps the source's own `README.md` as the provenance card, and caps individual files at 100 MB.

## Step 4 — Convert binaries to text

Some datasets ship as parquet. [`../corpus/convert.py`](../corpus/convert.py) downloads those, reads them with pandas, and writes `<stem>.json` (records) plus a `<stem>.md` 20-row preview. It drops pandas index-artifact columns (`__index_level_0__`), never keeps the parquet, and reports anything it cannot convert:

```sh
python3 corpus/convert.py <dataset-id>
```

Converted sets: the MechanicDB OBD-II sample and the NHTSA complaints parquet set.

## Step 5 — Record provenance

Three documents, one owner each:

| File | What it holds |
|---|---|
| [`../corpus/MANIFEST.md`](../corpus/MANIFEST.md) | Every vendored dataset: directory, HF id, license, rows, notes — plus the removal record and the rejected list |
| [`../corpus/INDEX.md`](../corpus/INDEX.md) | The readable surface index: category counts, per-dataset downloads/license/size, and the vendored table |
| [`../corpus/TUNING.md`](../corpus/TUNING.md) | What the corpus teaches the pattern library: pattern families, candidates, calibration findings, gaps |

## Step 6 — Verify

After all fetches: a filesystem pass confirmed **zero non-text files** in `corpus/`, and a counting pass summed **1,272,956 records across 54 datasets** (~205 MB on disk; the `Rows` column of the manifest, re-summed 2026-11-21). Row counts per dataset are recorded in the manifest.

---

## The result, at a glance

| Lane | Datasets | Records | Deepest material |
|---|---|---|---|
| Auto | 19 | ~608k | NHTSA complaints & recalls, OBD-II/DTC codes, repair procedures, maintenance schedules, body-shop directory |
| Home | 35 | ~843k | Building permits, contractor directories & licensing, plumbing/HVAC/appliance references, roofing/siding/gutter data, cost registers |

## The honest gap

The surface has **no US/Canada dataset of real repair *estimates* or *invoices* at scale** — nothing that is the actual document MechanicLens decodes. The corpus is deep on symptoms, diagnostics, costs, trades, and licensing, and silent on the document itself. That gap is recorded, not papered over: it is why the kit's fixtures are synthetic, and why the corpus is a calibration reference rather than a training set. See [L2 in the learnings](learnings/01-corpus.md).

## Reproducing the sweep

```sh
python3 corpus/fetch.py <dataset-id>        # fetch one dataset's text files
python3 corpus/convert.py <dataset-id>     # convert its parquet to text
```

The index is the catalog; the manifest is the record; this file is the method. Add a dataset only through the same steps — sweep, filter, fetch, convert, record, verify.