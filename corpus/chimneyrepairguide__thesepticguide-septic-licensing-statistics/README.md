---
license: cc-by-4.0
pretty_name: "Septic Contractor Licensing Statistics by State (U.S., 2026)"
language:
- en
tags:
- septic
- contractor-licensing
- united-states
- open-data
size_categories:
- 1K<n<10K
configs:
- config_name: septic-providers-by-state
  data_files: septic-providers-by-state.csv
  default: true
- config_name: license-types-by-issuer
  data_files: license-types-by-issuer.csv
- config_name: septic-providers-by-county
  data_files: septic-providers-by-county.csv
- config_name: state-licensing-rules
  data_files: state-licensing-rules.csv
---
# Septic Contractor Licensing Statistics by State (U.S., 2026)

**Creator:** The Septic Guide (https://thesepticguide.com/)
**DOI (all versions, cite this):** [10.5281/zenodo.23550642](https://doi.org/10.5281/zenodo.23550642)
**This version (1.0.1):** [10.5281/zenodo.23643824](https://doi.org/10.5281/zenodo.23643824) · [Zenodo record](https://zenodo.org/records/23643824)
**Data page:** https://thesepticguide.com/septic-data/

This Hugging Face copy mirrors the Zenodo record (version 1.0.1). Version 1.0.1 corrects the LICENSE file and adds the match-rate caveat; the data files are unchanged from 1.0.0.

## Citation
The Septic Guide (2026). *Septic Contractor Licensing Statistics by State (U.S., 2026)* (Version 1.0.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23550642

Compiled by **The Septic Guide** (https://thesepticguide.com/). License: CC BY 4.0.

Aggregate counts of septic service providers in The Septic Guide directory, how many are matched to an official state license or certification list, the agencies and license types behind those matches, and each state's licensing rules (state vs. local licensing, whether a public roster exists). **No row-level contractor records** (names, phones, addresses, websites, license numbers) are included.

| File | Rows | What |
|---|---|---|
| septic-providers-by-state.csv | 45 | Providers, license-matched, match rate, phone/website counts, services, licensing level |
| septic-providers-by-county.csv | 1,828 | Providers and license-matched by county/parish |
| license-types-by-issuer.csv | 421 | Providers holding each license type, by issuing agency |
| state-licensing-rules.csv | 51 | 50 states + DC: who licenses septic work, credentials, roster availability |
| summary.json | – | National totals |

Headline: 28,546 providers listed in 44 states + DC; 27,065 (94.8%) matched to license/certification lists from 26 state agencies. Snapshot as of Oct 21, 2026.

**Match rate is not a compliance rate:** it reflects how the directory was sourced from state license rosters, not the share of septic businesses that are licensed.

Rebuild: `python3 src/build.py /path/to/thesepticguide.com`. See METHODS.md, DATA-DICTIONARY.md, FINDINGS.md.
Suggested citation: The Septic Guide (2026). Septic Contractor Licensing Statistics by State. https://thesepticguide.com/septic-data/
