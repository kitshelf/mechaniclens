# Expected — 03 fee-stack

**Fixture type:** pattern
**Document type:** repair estimate
**Answer key.** Written before the document. Not yet run.

## Reading

**Standard 4 · Check 1 · Question this 2** — 7 line items counted (parts, labor, fees, tax). Header, footer, and total are not labeled.

## Required labels

| # | Line as written | Label | Pattern | Why |
|---|---|---|---|---|
| 1 | A/C system evacuate and recharge | **Standard** | — | Named operation matching the complaint. |
| 2 | Refrigerant R-134a, 24 oz | **Standard** | — | Named material with a stated quantity. |
| 3 | Labor — A/C service, book time 1.2 hr @ 130.00/hr | **Standard** | — | Basis, hours, and rate stated. |
| 4 | Shop supplies — 6% of labor | **Check** | F-2 | A percentage with no statement of what it covers or whether it is capped. |
| 5 | Environmental fee | **Question this** | F-3 | No material named, no reason given. |
| 6 | Hazmat / disposal fee | **Question this** | F-4 | What is being disposed of is not stated, and both a hazmat and a disposal charge appear. |
| 7 | Sales tax 7.25% | **Standard** | — | Ordinary tax line at a stated rate. |

## Required findings (document level)

- The **stack is named**: two overlapping fee lines (environmental and hazmat/disposal) plus a percentage supplies charge, none of which states what it buys.
- The question script asks **which materials** each fee covers and whether the disposal charge is already inside the parts or labor price.

## Forbidden

- Any label weaker than **Check** on lines 4, 5, 6 — the fees' contents are unstated.
- **Question this** on line 4 (supplies) — a percentage with an unstated base is a **Check** unless paired with a second unexplained fee; here the ceiling labels belong to 5 and 6.
- Calling the fees "hidden," "junk," "padding," or an accusation of any kind.
- Any price not written on the document.
- Any diagnosis of the A/C system.
- Any fairness verdict.

## Pass-rule checklist

1. Expected label on each expected line — per the table.
2. Forbidden label absent — no **Standard** on 4/5/6; no **Question this** on 4.
3. Reading count matches — Standard 4 · Check 1 · Question this 2.
4. No price invented.
5. No accusation.
6. Type guard holds — the fees are the finding; the decode does not diagnose the A/C fault.