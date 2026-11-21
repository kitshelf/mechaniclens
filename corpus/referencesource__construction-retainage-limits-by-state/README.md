---
pretty_name: "Construction retainage limits by US state — maximum withholding percentages, release deadlines, escrow requirements, and public vs private distinctions with statutory citations"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/construction-retainage-limits-by-state/
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
# Construction retainage limits by US state — maximum withholding percentages, release deadlines, escrow requirements, and public vs private distinctions with statutory citations

**Canonical, always-current version: https://referencesource.org/construction-retainage-limits-by-state/**
Machine-readable: https://referencesource.org/construction-retainage-limits-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-16
- **Stale after:** 2027-08-16 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 30

State-by-state comparison of the statutory rules governing retainage (retention) on construction contracts. Each record is one state with the maximum retainage percentage for public and private projects, the deadline for releasing retained funds after substantial completion, whether retainage must be held in an interest-bearing escrow account, whether the cap is reduced after a completion milestone (e.g. 50% complete), and the statutory citation. Caps range from 0% (New Mexico) to 10%, with a strong trend toward 5%. Answers 'how much retainage can be withheld on my project in [state]', 'when must retainage be released', and 'does my state require retainage escrow'.

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

- https://www.azleg.gov/ars/41/02576.htm
- https://www.azleg.gov/ars/32/01182.htm
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=10261.&lawCode=PCC
- https://california.public.law/codes/civil_code_section_8811
- https://colorado.public.law/statutes/crs_38-46-103
- https://www.cga.ct.gov/current/pub/chap_742b.htm
- https://www.cga.ct.gov/current/pub/chap_847.htm
- http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0200-0299/0255/Sections/0255.078.html
- http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0715/Sections/0715.12.html
- https://codes.findlaw.com/ga/title-13-contracts/ga-code-sect-13-10-80.html
- https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=081506030K20
- https://codes.findlaw.com/in/title-5-state-and-local-administration/in-code-sect-5-16-5-5-3.html
- https://www.legis.iowa.gov/docs/code/573.12.pdf
- https://www.legis.iowa.gov/docs/code/573.14.pdf
- https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=35259
- https://www.legis.la.gov/legis/Law.aspx?d=94968
- https://www.legis.la.gov/legis/Law.aspx?d=94969
- https://www.legis.la.gov/legis/Law.aspx?d=1147489
- https://www.legis.la.gov/legis/Law.aspx?d=1147491
- https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=grp&section=9-304&enactments=false
- https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gsf&section=13-225&enactments=false
- https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter149/Section29F
- https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIII/Chapter30/Section39K
- https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-125-1563
- https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-125-1561
- https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-125-1562
- https://www.revisor.mn.gov/statutes/cite/337.10
- https://revisor.mo.gov/main/OneSection.aspx?bid=905&hl=&section=34.057
- https://revisor.mo.gov/main/OneSection.aspx?section=436.303
- https://revisor.mo.gov/main/OneSection.aspx?section=436.336
- https://nebraskalegislature.gov/laws/statutes.php?statute=45-1204
- https://nebraskalegislature.gov/laws/statutes.php?statute=45-1203
- https://nebraskalegislature.gov/laws/statutes.php?statute=45-1202
- https://www.leg.state.nv.us/nrs/nrs-338.html
- https://www.leg.state.nv.us/nrs/nrs-624.html
- https://www.nmlegis.gov/sessions/07%20regular/final/SB0604.html
- https://www.nmlegis.gov/Legislation/Legislation?chamber=S&legType=B&legNo=604&year=07
- https://newyork.public.law/laws/n.y._general_business_law_section_756-c
- https://newyork.public.law/laws/n.y._general_municipal_law_section_106-b
- https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_143/GS_143-134.1.html
- https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_22C.html
- https://codes.ohio.gov/ohio-revised-code/section-153.12
- https://codes.ohio.gov/ohio-revised-code/section-153.13
- https://codes.ohio.gov/ohio-revised-code/section-153.63
- https://codes.ohio.gov/ohio-revised-code/section-4113.61
- https://oregon.public.law/statutes/ors_701.420
- https://legis.state.pa.us/WU01/LI/LI/US/HTM/1994/0/0007..HTM?1=
- https://www.palegis.us/statutes/consolidated/view-statute?txtType=PDF&ttl=62&div=00.&chpt=039.&sctn=021.&subsctn=000.
- https://www.scstatehouse.gov/code/t29c006.php
- https://www.scstatehouse.gov/code/t11c035.php
- https://law.justia.com/codes/tennessee/title-66/chapter-34/part-1/section-66-34-103/
- https://tcss.legis.texas.gov/resources/GV/htm/GV.2252.htm
- https://tcss.legis.texas.gov/resources/PR/htm/PR.53.htm
- https://law.lis.virginia.gov/vacode/2.2-4333/
- https://law.lis.virginia.gov/vacode/11-4.6/
- https://app.leg.wa.gov/rcw/default.aspx?cite=60.28.011
- https://app.leg.wa.gov/rcw/default.aspx?cite=60.30.010
- https://docs.legis.wisconsin.gov/document/statutes/66.0901

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/construction-retainage-limits-by-state/
