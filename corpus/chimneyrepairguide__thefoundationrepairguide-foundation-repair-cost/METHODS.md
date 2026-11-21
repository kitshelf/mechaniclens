# Methods

1. **Starting list.** Every price-range table row (`rows={[...]}` with low/high) on the six live cost guides: foundation-repair-cost, foundation-crack-repair-cost, helical-piers-cost, house-leveling-cost, pier-and-beam-repair-cost, slab-foundation-repair-cost (src/extract.py; 93 rows).
2. **Attribution.** Each row is tied to the publisher named in the row and that publisher's URL from the page's source list. Two tables name no publisher per row; they are attributed to the source the page states under the table (Angi bowing-wall page; Olshan).
3. **De-duplication.** The same publisher + figure + unit quoted on several TFRG pages is kept once; all citing TFRG pages are listed in `tfrg_page` (93 → 80).
4. **Re-verification (2026-10-21).** Each source URL was fetched with curl and both the low and high figure were searched for as dollar amounts. Pages that blocked curl (403) were read through a public web fetch and checked by hand (Olshan, Angi pier-and-beam, Angi Austin, HomeServe, US Waterproofing). Perma-Pier (2 URLs) and Today's Homeowner could not be read; those 5 rows are flagged `not re-verified` and carry the figure as cited on TFRG.
5. Nothing is estimated, converted, inflated or averaged in the register.

## Caveats
- The automated check confirms both numbers appear as dollar amounts on the page, not that they sit in the same sentence; treat "verified (both figures found on page)" as strong but not line-level proof.
- Sources define scope differently (per pier vs. per job vs. per project, slab area not stated). Compare only within a unit.
- Several "national" figures share Angi's underlying data (HomeAdvisor, This Old House, LendEDU), so they are not independent observations.
- Contractor pages (Olshan, Ram Jack, Perma-Pier, Two Brothers, etc.) are marketing pages for their own service areas, often Texas.
- Olshan's quick-reference box lists mudjacking at $1,900–$3,800, conflicting with its $5,000–$10,800 table; the register uses the table figure.
- Angi's pier-and-beam page gives reshimming as $1,200–$4,000 in its table but $1,200–$2,000 in its text; the register uses the table.
- Bob Vila figures are dated May 2024; Angi Austin Oct 2025; HomeServe Oct 2024. All others 2025–2026.
- Repair types are assigned by The Foundation Repair Guide from the row label and section.
