---
license: cc-by-4.0
language:
- en
pretty_name: Florida Contractor License Types
tags:
- florida
- contractors
- licensing
- construction
- tabular
size_categories:
- n<1K
task_categories:
- table-question-answering
configs:
- config_name: default
  data_files: data.csv
---

# Florida Contractor License Types

This dataset lists the license prefixes Florida uses for construction and electrical contractors. Each row is one prefix, such as CGC or RR. It gives the license name, whether it is certified or registered, the board that issues it, a short general scope, and where it can be used. It has 27 rows and comes from the official code table published by the Florida Department of Business and Professional Regulation (DBPR) and the definitions in Chapter 489 of the Florida Statutes.

## Columns

- `prefix`: the letters at the start of a license number, for example CGC in CGC1234567
- `license_type`: the official license name
- `certified_or_registered`: `certified` or `registered`
- `board`: Construction Industry Licensing Board or Electrical Contractors' Licensing Board
- `scope_summary`: one general sentence describing the trade
- `geographic_scope`: where the license may be used

## Reading a prefix

On Construction Industry Licensing Board licenses, a prefix that starts and ends with C is a certified license. The middle letter is the trade: G for general, B for building, R for residential, C for roofing, F for plumbing, and so on. Registered licenses use R followed by the trade letter, so RG is a registered general contractor. Electrical licenses come from a separate board and use EC (certified) or ER (registered).

## Certified vs registered

A certified contractor passed the state exam and may work anywhere in Florida. A registered contractor qualified through a local competency process and may only work in the county or city where that registration applies. Both are valid licenses. With a registered contractor, check that the job falls inside their area.

## Checking a license

Go to the DBPR license search at https://www.myfloridalicense.com/wl11.asp?mode=0&SID= and search by license number or name. Make sure the name matches the person or company you are hiring, the status shows as current and active, and the prefix fits the work you need done.

## Limitations

The scope sentences are short summaries. The statutes set out the full limits, including size and height thresholds and air-conditioning classes. Alarm system, tank lining, and precision tank tester codes are not included. Statutes and board rules change over time, so check the current text. This dataset is general information, not legal advice.

## Sources

- https://www2.myfloridalicense.com/about-us/understanding-dbpr-codes/
- https://www2.myfloridalicense.com/construction-industry/
- https://www.flsenate.gov/Laws/Statutes/2025/489.105
- https://www.flsenate.gov/Laws/Statutes/2025/489.505
- https://www.myfloridalicense.com/wl11.asp?mode=0&SID=

Maintained by [Nearbia](https://nearbia.com/).
