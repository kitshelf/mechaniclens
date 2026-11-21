---
license: cc-by-4.0
language:
  - en
pretty_name: US vehicle diagnostic trouble codes, linked to manufacturer bulletins and owner reports
size_categories:
  - 1K<n<10K
task_categories:
  - tabular-classification
  - text-retrieval
tags:
  - automotive
  - vehicle-safety
  - obd-ii
  - diagnostic-trouble-codes
  - nhtsa
  - recalls
  - technical-service-bulletins
  - open-government-data
configs:
  - config_name: default
    data_files: dtc.csv
---

# US vehicle diagnostic trouble codes, linked to manufacturer bulletins and owner reports

**1,142 OBD-II diagnostic trouble codes** as they actually appear in US manufacturer service bulletins and NHTSA
owner-complaint filings — with the model years, vehicle components and source documents each code shows up in.

Derived from public NHTSA filings. Regenerated nightly.

**DOI: [10.5281/zenodo.22891283](https://doi.org/10.5281/zenodo.22891283)** — archived on Zenodo. That is the
*concept* DOI: it always resolves to the newest version, which is the correct one to cite for a file that is
rebuilt every night.

## What this is, and what it is not

Code-definition dictionaries already exist, and most of them are copies of one another. **This is the opposite
direction.** It does not tell you what P0420 means in the abstract; it tells you *which real vehicles, which
manufacturer bulletins and how many owner complaints that code actually turns up in.*

Be clear about the limitation before you use it: **only 119 of the 1,142 codes (10.4%) carry a plain-English
meaning.** If a definition lookup is what you need, this is the wrong dataset. The linkage is the value, and that
linkage does not exist elsewhere as an open file.

## Composition

| code family | codes |
|---|---|
| P — powertrain | 778 |
| U — network / communication | 147 |
| B — body | 131 |
| C — chassis | 86 |
| **total** | **1,142** |

Across the corpus those codes reference **128,336 bulletin occurrences** and **5,434 owner reports**.

## Columns

| column | meaning |
|---|---|
| `code` | the diagnostic trouble code, e.g. `P0300` |
| `defined_by` | `standard` where the code is SAE-standard, otherwise manufacturer-specific |
| `meaning` | plain-English definition where one is established — empty for ~90% of rows, see above |
| `bulletins` | number of manufacturer service-bulletin occurrences referencing this code |
| `owner_reports` | number of NHTSA owner complaints referencing this code |
| `documents` | number of distinct source documents |
| `model_years` | number of distinct model years the code appears against |
| `components` | pipe-separated NHTSA component categories, e.g. `Engine And Engine Cooling\|Power Train` |
| `page` | canonical URL for the code on whichtrim.com |

## Files

- `dtc.csv` — 1,142 rows, 162 KB
- `dtc.json` — the same data with provenance: `{generated_at, source, codes}`

## Provenance

Compiled from NHTSA's public bulk files (recall campaigns, manufacturer communications, owner complaints) by
[WhichTrim](https://whichtrim.com). Nothing is hand-edited; the files are regenerated nightly from the sources, so
`generated_at` in the JSON is the authoritative timestamp for any given copy.

Live files, always current:
- https://whichtrim.com/data/dtc.csv
- https://whichtrim.com/data/dtc.json
- Landing page with schema.org `Dataset` markup: https://whichtrim.com/dtc/
- Permanent archive: https://doi.org/10.5281/zenodo.22891283

## Licence

**CC BY 4.0** — https://creativecommons.org/licenses/by/4.0/

Use it commercially, redistribute it, build on it. Attribution required.

## Citation

```bibtex
@dataset{whichtrim_dtc_2026,
  title     = {US vehicle diagnostic trouble codes linked to manufacturer bulletins and owner reports},
  author    = {{WhichTrim}},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22891283},
  url       = {https://doi.org/10.5281/zenodo.22891283},
  note      = {Derived from NHTSA public filings. CC BY 4.0. Regenerated nightly; this is the concept DOI and
               resolves to the current version.}
}
```

Plain text:

> WhichTrim (2026). *US vehicle diagnostic trouble codes linked to manufacturer bulletins and owner reports.*
> https://doi.org/10.5281/zenodo.22891283

## Related

The same project publishes a fuller vehicle record — recalls joined to severity and completion rates, owner
complaints, NCAP crash ratings, driver-assist crash reports, EPA fuel economy and trim specifications — at
[whichtrim.com](https://whichtrim.com) and through an MCP server registered as `com.whichtrim/vehicle-records`.

Three of those datasets are also CC BY 4.0 and can be used the same way as this one:

- the two files on this page, `dtc.csv` and `dtc.json`;
- **driver-assist crash reports** — every crash reported to NHTSA under Standing General Order 2021-01 with a
  Level 2 or automated-driving system engaged, joined to the model year it names:
  [`sgo.csv`](https://whichtrim.com/data/sgo.csv) · [`sgo.json`](https://whichtrim.com/data/sgo.json) ·
  [landing page](https://whichtrim.com/driver-assist-crashes/);
- **the quarterly reports** — a dated, frozen snapshot of a model year's federal recall record:
  [`/reports/`](https://whichtrim.com/reports/), `data.csv` and `data.json` under each quarter.

Everything else — the full vehicle compilation, the per-vehicle JSON, the search index, the API and Recall
Watch — is **not** CC BY. See [the carve-out in the terms](https://whichtrim.com/terms/#ccby).
