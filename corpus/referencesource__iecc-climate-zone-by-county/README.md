---
pretty_name: "IECC/Building America climate zone by U.S. county, 2021 code cycle"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/iecc-climate-zone-by-county/
language:
- en
tags:
- reference-data
- provenance
- referencesource-org
configs:
- config_name: default
  data_files:
  - split: train
    path: data/records.jsonl
---
# IECC/Building America climate zone by U.S. county, 2021 code cycle

**Canonical, always-current version: https://referencesource.org/iecc-climate-zone-by-county/**
Machine-readable: https://referencesource.org/iecc-climate-zone-by-county/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-09-30
- **Stale after:** 2028-09-29 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 3134

Which IECC climate zone (1-8, with A/B/C moisture regime) and which DOE Building America climate zone each U.S. county falls in under the 2021 code cycle, and whether that county's designation changed from the pre-2021 (2018 IECC) map. Answers 'what climate zone is my county in for insulation R-value and HVAC-sizing purposes' and 'did my county's zone change in the 2021 code' -- both load-bearing for code-compliance software, HVAC equipment sizing, and DOE Zero Energy Ready Home certification, and both wrong if answered from a pre-2021 map or a general knowledge cutoff. Source is a single DOE/Pacific Northwest National Laboratory report (PNNL-33270, Sept 2022) that prints one table row per county -- the free public proxy for ASHRAE Standard 169 Table B-1, which is paywalled. No free site was found that republishes PNNL's full, current, cited county table as clean HTML; the closest match (a GitHub gist CSV) carries no source citation or edition statement.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

US government work (DOE / Pacific Northwest National Laboratory, operated by Battelle for DOE under contract DE-AC05-76RL01830) -- public domain. Facts taken with short attributed quotes linking back to the published report.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.osti.gov/servlets/purl/1893981
- https://basc.pnnl.gov/sites/default/files/ClimateZoneDataFiles.zip

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/iecc-climate-zone-by-county/
