---
pretty_name: "Electrician licence progression: training hours and prerequisites by US state"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/electrician-licence-progression-by-state/
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
# Electrician licence progression: training hours and prerequisites by US state

**Canonical, always-current version: https://referencesource.org/electrician-licence-progression-by-state/**
Machine-readable: https://referencesource.org/electrician-licence-progression-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-15
- **Stale after:** 2027-04-13 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 2

What it takes to move up the electrician licence ladder in each US state: the on-the-job training hours, the classroom hours, the licence you must already hold and for how long, and the separate hour threshold that lets you sit the exam before you qualify for the licence. One record is one licence level in one state, sourced from that state's licensing authority. Answers 'how many hours of on-the-job training for a journeyman electrician in Texas', 'journeyman electrician requirements by state', 'how do I become a master electrician', 'how many hours to take the electrician exam', and 'do my apprentice hours transfer to another state'. Texas has two thresholds that are constantly conflated — 7,000 hours to sit the exam, 8,000 hours for the licence — and master requires holding the journeyman licence for two years plus 12,000 hours, with industrial journeyman experience explicitly excluded. There is no federal electrician licence and no national board, so the comparison exists nowhere and the search results are exam-prep vendors.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts extracted from the freely published licensing pages of state licensing authorities, with a short attributed quote and a link back. Licence requirements are public regulatory facts. No source page carries a restrictive notice.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.tdlr.texas.gov/electricians/apply/individuals/journeyman-electrician.htm
- https://www.tdlr.texas.gov/electricians/apply/individuals/master-electrician.htm

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/electrician-licence-progression-by-state/
