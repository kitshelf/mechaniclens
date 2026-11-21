---
pretty_name: "How long before a car left on your property or towed from it can legally be sold — by US state"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/abandoned-vehicle-private-property-timelines-by-state/
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
# How long before a car left on your property or towed from it can legally be sold — by US state

**Canonical, always-current version: https://referencesource.org/abandoned-vehicle-private-property-timelines-by-state/**
Machine-readable: https://referencesource.org/abandoned-vehicle-private-property-timelines-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-18
- **Stale after:** 2027-08-18 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 44

State-by-state comparison of the legal timeline for a vehicle left on private property (or towed from it) to be classified abandoned, held, noticed, and eventually sold or junked. This is a genuinely different process shape per state, not just a different number of days on the same form: Colorado uses a flat 24-hour threshold for a vehicle to count as abandoned on private property, and a separate 48-hour window for the owner to reclaim it from an impound lot before it is treated as abandoned there too. Georgia uses a single flat 30-day unattended-on-property threshold, with no separate notice-and-sale sequence specified at the abandonment-classification stage. Texas runs a multi-step notice sequence instead of a single threshold: the vehicle must sit at least 24 hours before a first notice is sent (within 5 days if Texas-registered, 14 days if out-of-state), a second notice follows 15-20 days after the first, and the storage facility must then wait at least 30 days after the second notice before a public sale — a ~65-90 day process from tow to sale, compared to Colorado's 24-48 hour classification. Answers 'how long do I have to get my towed car back before it's sold', and 'how long does a car have to sit on my property before I can have it removed as abandoned'. Relevant to property owners, HOAs, landlords, and people whose car has been towed.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts from state statutes; statutory text is government work and the facts in it are not copyrightable (Feist, 1991). Each record quotes a short attributed excerpt and links back to the page it was read from. Citation note, checked 2026-10-14: The Georgia and New Jersey rows are cited to codes.findlaw.com rather than to an official state host, because neither state publishes its code anywhere a single section can be fetched at a stable URL — Georgia's own free O.C.G.A., which the General Assembly contracts LexisNexis to publish, is a JavaScript application at advance.lexis.com that serves no statutory text to a fetch; and New Jersey's official statutes site, lis.njleg.state.nj.us, is a Folio frameset whose internal document numbers are not stable section addresses. That mirror now sits behind a Cloudflare challenge and returns 403 to everyone, an invented-slug control included, so these rows cannot at present be re-checked against the page they cite. The values were read from those pages when the records were harvested and nothing here has changed them; what is missing is any ongoing check that they are still current.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://law.justia.com/codes/alabama/title-32/chapter-13/section-32-13-1/
- https://www.akleg.gov/basis/folioproxy.asp?url=http://wwwjnu03.akleg.org/cgi-bin/folioisa.dll/stattx23/query=%5BJUMP:%2728!2E11!2E020%27%5D/doc/%7Bt1%7D/pageitems=%7Bbody%7D?firsthit
- https://www.azleg.gov/ars/28/04801.htm
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=VEH&sectionNum=22658.
- https://dmv.colorado.gov/abandoned-vehicles
- https://web.archive.org/web/2024/https://www.cga.ct.gov/current/pub/chap_246.htm
- https://delcode.delaware.gov/title21/c044/index.html
- https://code.dccouncil.gov/us/dc/council/code/sections/50-2431
- https://www.flsenate.gov/Laws/Statutes/2024/713.78
- https://www.flsenate.gov/Laws/Statutes/2024/715.07
- https://codes.findlaw.com/ga/title-40-motor-vehicles-and-traffic/ga-code-sect-40-11-1/
- https://www.capitol.hawaii.gov/hrscurrent/Vol05_Ch0261-0319/HRS0290/HRS_0290-0011.htm
- https://legislature.idaho.gov/statutesrules/idstat/Title49/T49CH18/SECT49-1806/
- https://www.ilga.gov/legislation/ilcs/documents/062500050K4-201.htm
- https://codes.findlaw.com/in/title-9-motor-vehicles/in-code-sect-9-13-2-1.html
- https://codes.findlaw.com/in/title-9-motor-vehicles/in-code-sect-9-22-1-11.html
- https://www.legis.iowa.gov/docs/code/321.89.pdf
- https://ksrevisor.gov/statutes/chapters/ch08/008_011_0002.html
- https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=54934
- https://www.legis.la.gov/legis/Law.aspx?d=88441
- https://legislature.maine.gov/statutes/29-A/title29-Asec1852.html
- https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtr&section=25-201
- https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section22C
- https://legislature.mi.gov/doc.aspx?mcl-257-252a
- https://www.revisor.mn.gov/statutes/cite/168B.04
- https://codes.findlaw.com/ms/title-63-motor-vehicles-and-traffic-regulations/ms-code-sect-63-23-3/
- https://revisor.mo.gov/main/OneSection.aspx?section=304.157
- https://leg.mt.gov/bills/mca/title_0610/chapter_0120/part_0040/section_0010/0610-0120-0040-0010.html
- https://nebraskalegislature.gov/laws/statutes.php?statute=60-1901
- https://www.leg.state.nv.us/nrs/NRS-487.html
- https://www.gencourt.state.nh.us/rsa/html/XXI/262/262-mrg.htm
- https://codes.findlaw.com/nj/title-39-motor-vehicles-and-traffic-regulation/nj-st-sect-39-4-56-6.html
- https://www.mvd.newmexico.gov/chapter-1-vehicles-definitions/
- https://www.nysenate.gov/legislation/laws/VAT/1224
- https://www.ncleg.net/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-137.7.html
- https://codes.ohio.gov/ohio-revised-code/section-4513.60
- https://www.oregonlegislature.gov/bills_laws/ors/ors819.html
- https://www.palegis.us/statutes/consolidated/view-statute&txtType=PDF&ttl=75&div=00.&chpt=73&sctn=11&subsctn=1
- http://webserver.rilegislature.gov/Statutes/TITLE31/31-42/31-42-1.htm
- https://www.scstatehouse.gov/code/t56c005.php
- https://texas.public.law/statutes/tex._occ._code_section_2303.157
- https://texas.public.law/statutes/tex._transp._code_section_683.002
- https://texas.public.law/statutes/tex._occ._code_section_2303.151
- https://texas.public.law/statutes/tex._occ._code_section_2303.154
- https://le.utah.gov/xcode/Title41/Chapter6a/C41-6a-S1408_2015051220150512.pdf
- https://law.lis.virginia.gov/vacode/title46.2/chapter12/section46.2-1200/
- https://app.leg.wa.gov/rcw/default.aspx?cite=46.55.010
- https://docs.legis.wisconsin.gov/document/statutes/342.40
- https://wyoleg.gov/statutes/compress/title31.pdf

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/abandoned-vehicle-private-property-timelines-by-state/
