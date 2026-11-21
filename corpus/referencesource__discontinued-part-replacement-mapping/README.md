---
pretty_name: "Discontinued electronic component replacement mapping"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/discontinued-part-replacement-mapping/
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
# Discontinued electronic component replacement mapping

**Canonical, always-current version: https://referencesource.org/discontinued-part-replacement-mapping/**
Machine-readable: https://referencesource.org/discontinued-part-replacement-mapping/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-11-01
- **Stale after:** 2027-01-30 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 28

Discontinued electronic components and their manufacturer-suggested replacements, with last-time-buy and last-ship dates where published. Covers EOL notices from TI, NXP, Renesas, Infineon, onsemi, ST, Microchip, Cirrus Logic and commonly sought legacy parts. Answers 'what replaced [part number]' and '[part] superseded by what' — the supersession lookup assistants get wrong on obscure components.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Fair use (factual product discontinuation data aggregated from manufacturer notices)

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.dasenic.com/blog/knowledgeHub/obsolete-components-in-2026-eol-list-shortage-statistics-what-to-do-about-it

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/discontinued-part-replacement-mapping/
