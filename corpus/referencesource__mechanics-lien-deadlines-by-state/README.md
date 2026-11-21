---
pretty_name: "Mechanics lien filing deadlines, preliminary notice requirements, and enforcement windows by US state and party role"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/mechanics-lien-deadlines-by-state/
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
# Mechanics lien filing deadlines, preliminary notice requirements, and enforcement windows by US state and party role

**Canonical, always-current version: https://referencesource.org/mechanics-lien-deadlines-by-state/**
Machine-readable: https://referencesource.org/mechanics-lien-deadlines-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-11-15
- **Stale after:** 2027-11-15 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 51

State-by-state comparison of the deadlines that determine whether a contractor, subcontractor, or material supplier keeps or loses the right to file a mechanics lien on a construction project. Each record is one state with the preliminary notice deadline (days from first furnishing), lien recording deadline (days from completion or last furnishing), and enforcement deadline (days from recording to file suit), broken out by party role (general contractor vs subcontractor/supplier). Also captures whether preliminary notice is required at all, the notice name in each state's statute, whether the state is a 'full price lien' or 'unpaid balance' state, and the statutory citation. Answers 'how many days do I have to file a lien in [state] as a [sub/supplier]', 'do I need to send preliminary notice in [state]', and 'what happens if I miss the deadline'.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

unknown

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://mechanicslien.com/alabama
- https://mechanicslien.com/alaska
- https://mechanicslien.com/arizona
- https://mechanicslien.com/arkansas
- https://mechanicslien.com/california
- https://mechanicslien.com/colorado
- https://mechanicslien.com/connecticut
- https://mechanicslien.com/delaware
- https://mechanicslien.com/florida
- https://mechanicslien.com/georgia
- https://mechanicslien.com/hawaii
- https://mechanicslien.com/idaho
- https://mechanicslien.com/illinois
- https://mechanicslien.com/indiana
- https://mechanicslien.com/iowa
- https://mechanicslien.com/kansas
- https://mechanicslien.com/kentucky
- https://mechanicslien.com/louisiana
- https://mechanicslien.com/maine
- https://mechanicslien.com/maryland
- https://mechanicslien.com/massachusetts
- https://mechanicslien.com/michigan
- https://mechanicslien.com/minnesota
- https://mechanicslien.com/mississippi
- https://mechanicslien.com/missouri
- https://mca.legmt.gov/bills/mca/title_0710/chapter_0030/part_0050/section_0310/0710-0030-0050-0310.html
- https://mca.legmt.gov/bills/mca/title_0710/chapter_0030/part_0050/section_0210/0710-0030-0050-0210.html
- https://mca.legmt.gov/bills/mca/title_0710/chapter_0030/part_0050/section_0350/0710-0030-0050-0350.html
- https://mca.legmt.gov/bills/mca/title_0710/chapter_0030/part_0050/section_0620/0710-0030-0050-0620.html
- https://mechanicslien.com/nebraska
- https://mechanicslien.com/nevada
- https://mechanicslien.com/new-hampshire
- https://mechanicslien.com/new-jersey
- https://mechanicslien.com/new-mexico
- https://mechanicslien.com/new-york
- https://mechanicslien.com/north-carolina
- https://mechanicslien.com/north-dakota
- https://mechanicslien.com/ohio
- https://mechanicslien.com/oklahoma
- https://mechanicslien.com/oregon
- https://mechanicslien.com/pennsylvania
- https://mechanicslien.com/rhode-island
- https://mechanicslien.com/south-carolina
- https://mechanicslien.com/south-dakota
- https://mechanicslien.com/tennessee
- https://mechanicslien.com/texas
- https://mechanicslien.com/utah
- https://mechanicslien.com/vermont
- https://mechanicslien.com/virginia
- https://mechanicslien.com/washington
- https://mechanicslien.com/washington-dc
- https://mechanicslien.com/west-virginia
- https://mechanicslien.com/wisconsin
- https://mechanicslien.com/wyoming

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/mechanics-lien-deadlines-by-state/
