---
pretty_name: "Electrician licence reciprocity by state: which states accept which licences, in which direction, on what conditions"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/electrician-licence-reciprocity-by-state/
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
# Electrician licence reciprocity by state: which states accept which licences, in which direction, on what conditions

**Canonical, always-current version: https://referencesource.org/electrician-licence-reciprocity-by-state/**
Machine-readable: https://referencesource.org/electrician-licence-reciprocity-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-15
- **Stale after:** 2027-04-13 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 16

Which states will licence an electrician on the strength of another state's licence, per licensing board, with the direction and the conditions kept — the two things every aggregator flattens. Reciprocity agreements are directional and class-specific: Texas accepts journeyman licences from ten states (Alabama, Alaska, Arkansas, Idaho, Iowa, Nebraska, New Mexico, Oklahoma, South Dakota, Wyoming) but master licences from a different seven, and requires the licence held at least one year and gained by that state's own exam. The data churns: Texas added Arkansas (Dec 2025), Iowa (Feb 2026), Alabama (Mar 2026) and Ohio (Jun 2026) under a 2025 state law directing agencies to pursue agreements — every content-mill list found predates at least one of these. Answers 'which states does Texas have journeyman electrician reciprocity with?', 'can I use my Idaho journeyman licence in Oregon?', 'does my master electrician licence transfer to another state?'

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Sources are state licensing board pages (state government publications). We take facts plus short attributed quotes linking back.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.tdlr.texas.gov/electricians/out-of-state.htm

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/electrician-licence-reciprocity-by-state/
