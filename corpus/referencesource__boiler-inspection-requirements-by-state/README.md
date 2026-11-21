---
pretty_name: "US boiler and pressure vessel inspection requirements by state"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/boiler-inspection-requirements-by-state/
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
# US boiler and pressure vessel inspection requirements by state

**Canonical, always-current version: https://referencesource.org/boiler-inspection-requirements-by-state/**
Machine-readable: https://referencesource.org/boiler-inspection-requirements-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-05
- **Stale after:** 2027-08-05 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 55

State-by-state boiler and pressure vessel inspection requirements for all 50 US states plus DC, Puerto Rico, New York City and Chicago, drawn primarily from the National Board Synopsis (NB-370), with a second record from Chardon Labs for 15 jurisdictions where both sources speak. Each record is one jurisdiction as described by one source: inspection intervals by boiler type (power, low-pressure steam, hot water, unfired pressure vessel), accepted inspector qualifications (state, insurance, owner-user), residential and size/pressure exemptions, governing statute citation, and administering agency. Answers 'how often does Ohio require boiler inspections', 'which states accept insurance company inspections in lieu of state inspections', and 'are residential boilers exempt in my state'.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts extracted from state statutes (government works) and industry reference (National Board Synopsis, freely published). Inspection intervals and exemptions are regulatory facts, not copyrightable.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.nationalboard.org/PrintAllSynopsis.aspx?Jurisdiction=Select
- https://www.chardonlabs.com/resources/commercial-boiler-inspection-regulations-by-state/

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/boiler-inspection-requirements-by-state/
