---
pretty_name: "Catalytic converter sale and possession laws by US state — who can legally buy a used converter, and what a seller must prove"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/catalytic-converter-theft-laws-by-state/
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
# Catalytic converter sale and possession laws by US state — who can legally buy a used converter, and what a seller must prove

**Canonical, always-current version: https://referencesource.org/catalytic-converter-theft-laws-by-state/**
Machine-readable: https://referencesource.org/catalytic-converter-theft-laws-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-18
- **Stale after:** 2027-08-18 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 7

State-by-state comparison of the laws passed 2021-2024 restricting who may buy, sell, or possess a detached catalytic converter, in response to a national wave of theft. Each record is one state with: whether the sale of a detached converter to anyone other than a licensed/registered recycler or core buyer is restricted or banned outright; what documentation a seller must produce (proof of ownership, vehicle title/VIN match, driver's license); whether the converter or vehicle VIN must be etched/marked or a photo/record kept by the buyer; any mandatory holding period before a purchased converter can be resold or scrapped; and the criminal penalty tier (often graduated by quantity possessed). Answers 'can I legally sell a catalytic converter I removed myself', 'what do I need to bring to sell a converter as scrap', and 'is possessing multiple detached converters a felony in my state'. This is a genuinely different regulatory design per state, not just different penalty numbers on the same form: Arizona bans sale to anyone but a licensed recycler with narrow exceptions; Georgia requires a registered recycler plus ownership documentation; Minnesota adds a mandatory marking/registration regime, a 7-day holding period, and quantity-tiered felony thresholds; Virginia makes unauthorized sale a felony unless sold to a compliant purchaser; California lists six categories of lawful seller and lets a private owner sell their own converter on a title or registration whose VIN matches the marking; Washington requires the last eight VIN digits to be stamped on the converter within 24 hours of removal and splits the penalty at seven converters; Louisiana lets an unlicensed person deal only in the converters from one vehicle they own.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts from state statutes; statutory text is government work and the facts in it are not copyrightable (Feist, 1991). Each record quotes a short attributed excerpt and links back to the page it was read from. Citation note, checked 2026-10-14: The Georgia row is cited to codes.findlaw.com rather than to an official state host, because Georgia does not publish its code anywhere a single section can be fetched at a stable URL — Georgia's own free O.C.G.A., which the General Assembly contracts LexisNexis to publish, is a JavaScript application at advance.lexis.com that serves no statutory text to a fetch. That mirror now sits behind a Cloudflare challenge and returns 403 to everyone, an invented-slug control included, so these rows cannot at present be re-checked against the page they cite. The values were read from those pages when the records were harvested and nothing here has changed them; what is missing is any ongoing check that they are still current.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.azleg.gov/ars/13/03728.htm
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=VEH&sectionNum=10852.5.
- https://codes.findlaw.com/ga/title-10-commerce-and-trade/ga-code-sect-10-1-351/
- https://www.legis.la.gov/legis/Law.aspx?d=1297004
- https://www.revisor.mn.gov/statutes/cite/325E.21
- https://law.lis.virginia.gov/vacode/title18.2/chapter5/section18.2-146.1/
- https://app.leg.wa.gov/RCW/default.aspx?cite=9A.82.180

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/catalytic-converter-theft-laws-by-state/
