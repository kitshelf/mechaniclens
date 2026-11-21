---
pretty_name: "Home Energy Rebates — is my state's programme open, and what does it still pay for?"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/home-energy-rebate-program-status-by-state/
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
# Home Energy Rebates — is my state's programme open, and what does it still pay for?

**Canonical, always-current version: https://referencesource.org/home-energy-rebate-program-status-by-state/**
Machine-readable: https://referencesource.org/home-energy-rebate-program-status-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-05
- **Stale after:** 2026-11-04 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 47

With the federal 25C and 25D tax credits gone for anything placed in service after 31 December 2025, the Inflation Reduction Act's Home Energy Rebates are the main money left for a US home energy upgrade — but they are run by each state's energy office, not by the federal government, and most states have not opened theirs. DOE's own page says only 'Home Energy Rebates are now available in select states' and tells you to contact your State Energy Office; its state-by-state progress tracker now returns 404. Each record is one state or territory, carrying what that state calls its programmes, whether the electrification (HEEHR/HEAR) and efficiency (HOMES/HER) halves are open, closed, waitlisted or not yet launched, the date the state's own page gives for that status, the rebate cap, the income band, what the new appliance is allowed to replace, and how you apply. Answers 'can I get the $8,000 heat pump rebate in my state right now', 'is Colorado's HEAR programme still taking applications', 'which states have actually launched', and 'does the rebate still cover swapping out my gas furnace'.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

US federal and state government pages — facts not copyrightable (Feist, 1991). Each record quotes a short passage from the state energy office page it cites and links back to it. No compilation is reproduced. Aggregator and advocacy trackers (Rewiring America, Atlas Buildings Hub, Building Performance Association, National Housing Trust, DSIRE) are listed in sources.txt as finding aids only and must never be the source of a value.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://adeca.alabama.gov/ira-rebates/
- https://www.ahfc.us/efficiency/programs-for-homeowners/alaska-residential-energy-rebates
- https://efficiencyarizona.com/
- https://adeq.state.ar.us/energy/assistance/home-energy-rebates.aspx
- https://www.energy.ca.gov/programs-and-topics/programs/inflation-reduction-act-residential-energy-rebate-programs
- https://energyoffice.colorado.gov/home-energy-rebates
- https://portal.ct.gov/deep/energy/inflation-reduction-act-home-energy-rebate-programs
- https://dnrec.delaware.gov/climate-coastal-energy/energy-office/ira/home-energy-rebates/
- https://doee.dc.gov/service/federal-home-energy-rebates-and-healthy-homes-act-2024
- https://floridaenergysaverprogram.fdacs.gov/en-US/heehr-program/
- https://energyrebates.georgia.gov/hear-program-updates
- https://oemr.idaho.gov/financial-information/incentives/
- https://epa.illinois.gov/topics/energy/residential/energy-rebates.html
- https://www.in.gov/oed/grants-and-funding-opportunities/homeowner-incentives/
- https://opportunityiowa.gov/community/energy/grants-funding/residential-energy-efficiency-programs
- https://kshomerebates.gov/
- https://energyrebates.ky.gov/
- https://www.denr.louisiana.gov/page/home-energy-rebates-programs
- https://www.efficiencymaine.com/ira-home-energy-rebates/
- https://energy.maryland.gov/Pages/IRArebates.aspx
- https://www.masssave.com/frequently-asked-questions
- https://www.michigan.gov/egle/about/organization/materials-management/energy/rfps-loans/home-energy-rebate-programs
- https://mississippi.org/community-resources/office-of-energy/
- https://dnr.mo.gov/energy/what-were-doing/inflation-reduction-act-home-energy-rebates-programs
- https://deq.mt.gov/energy/Programs/efficiency
- https://dwee.nebraska.gov/nebraska-state-energy-program-iijabil-ira-formula-funding-opportunities
- https://www.energy.nv.gov/resources/home-energy-rebates-program/
- https://cleanenergy.nj.gov/programs/energy-efficiency/inflation-reduction-act-home-energy-rebates-in-new-jersey
- https://clean.energy.nm.gov/programs/hear/
- https://www.nyserda.ny.gov/All-Programs/EmPower-New-York-Program
- https://www.deq.nc.gov/energy-climate/state-energy-office/energy-saver-north-carolina
- https://www.commerce.nd.gov/community-services/energy-efficiency-office/home-energy-rebates-program
- https://development.ohio.gov/individual/energy-assistance/energy-savings
- https://www.okcommerce.gov/community-development/local-governments-edos/oklahoma-state-energy-office/
- https://www.homeenergyrebates.oregon.gov/hear
- https://www.pa.gov/agencies/dep/residents/saving-energy/inflation-reduction-act
- https://energy.ri.gov/incentives/home-energy-rebate-programs
- https://energy.sc.gov/rebates
- https://www.tn.gov/environment/program-areas/energy/state-energy-office/programs-projects/inflation-reduction-act/energy-rebate.html
- https://comptroller.texas.gov/programs/seco/funding/ira/
- https://energy.utah.gov/homepage/programs/utah-home-energy-rebate-programs/
- https://publicservice.vermont.gov/efficiency/inflation-reduction-act-bolster-vermont-weatherization-and-electrification-efforts
- https://www.energy.virginia.gov/energy-efficiency/HomeEnergyRebatesFrequentlyAskedQuestions.shtml
- https://www.commerce.wa.gov/energy/clean-buildings/energy-incentives/ira-home-energy-rebates/
- https://energywv.org/funding-opportunities/home-energy-rebate-programs/
- https://psc.wi.gov/Pages/ServiceType/OEI/FederalFunding.aspx
- https://wyoenergy.org/home-energy-savings-program/

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/home-energy-rebate-program-status-by-state/
