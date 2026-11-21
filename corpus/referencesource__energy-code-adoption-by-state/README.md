---
pretty_name: "Which energy code each US state enforces for new homes: the IECC edition (or state equivalent) actually in force, with effective dates and amendments, from the state rules themselves"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/energy-code-adoption-by-state/
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
# Which energy code each US state enforces for new homes: the IECC edition (or state equivalent) actually in force, with effective dates and amendments, from the state rules themselves

**Canonical, always-current version: https://referencesource.org/energy-code-adoption-by-state/**
Machine-readable: https://referencesource.org/energy-code-adoption-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-15
- **Stale after:** 2027-04-13 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 9

Which residential energy code is actually in force in a state, taken from the state's own rule or building-code authority, with the effective date and — where the rule states them — the state's amendments to it. Coverage is 9 states so far (California, Colorado, Florida, Georgia, New Jersey, Oregon, Pennsylvania, Texas, Washington), deliberately chosen to span the situations that break a one-size-fits-all answer, not the easy ones; the remaining states are listed as work to do in the asset's source notes rather than guessed at. What the pilot found: Georgia still runs the 2015 IECC with Georgia Supplements and Amendments even though it moved its other I-codes to the 2024 editions; Texas never adopted the IECC for homes at all, enforcing Chapter 11 of the 2015 International Residential Code since Sept. 1, 2016; New Jersey moved to the 2024 IECC on August 17, 2026, so anything still showing 2021 for New Jersey is out of date; Pennsylvania adopts the 2021 IECC but amends the residential envelope requirements in its own regulation; California, Florida and Oregon run state-written codes rather than adopting the IECC by name; and Colorado has no single statewide code, requiring local jurisdictions to adopt the state Model Low Energy and Carbon Code when they update any other building code. Answers 'which IECC edition does my state enforce?', 'what energy code applies to new residential construction in my state?', 'does my state amend the IECC or adopt it as written?', 'which states are still on the 2015 IECC?'

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Sources are US state government pages (public records). We take facts plus short attributed quotes linking back. Facts about code adoption are not copyrightable (Feist, 1991). The ICC codes themselves are copyrighted; we quote only the state's statement of which edition it adopts, not the code text.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards
- https://energyoffice.colorado.gov/building-energy-codes
- https://www.floridabuilding.org/c/default.aspx
- https://dca.georgia.gov/community-assistance/construction-codes/current-state-minimum-codes-construction
- https://www.nj.gov/dca/codes/codreg/current.shtml
- https://www.oregon.gov/bcd/codes-stand/Pages/energy-residential-compliance.aspx
- https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/034/chapter403/s403.21.html
- https://comptroller.texas.gov/programs/seco/code/single-family.php
- https://apps.leg.wa.gov/wac/default.aspx?cite=51-11R

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/energy-code-adoption-by-state/
