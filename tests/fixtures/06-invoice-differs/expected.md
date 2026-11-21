# Expected — 06 invoice-differs

**Fixture type:** pattern (after-repair branch)
**Document type:** estimate **and** final invoice in one paste
**Answer key.** Written before the document. Not yet run.

## Reading

**Standard 5 · Check 1 · Question this 4** — 10 line items counted (4 on the estimate, 6 on the invoice). Headers, footers, and the two total lines are not labeled.

## Required labels

| # | Line as written | Document | Label | Pattern | Why |
|---|---|---|---|---|---|
| 1 | Front brake pads, ceramic | estimate | **Standard** | — | Normal part line. |
| 2 | Labor — replace front brake pads, book time 1.5 hr @ 145.00/hr | estimate | **Standard** | — | Basis, hours, rate stated. |
| 3 | Shop supplies | estimate | **Check** | F-2 | Flat amount, contents and cap not stated. |
| 4 | Sales tax 7.25% | estimate | **Standard** | — | Ordinary tax line. |
| 5 | Front brake pads, ceramic | invoice | **Standard** | — | Matches the authorized line. |
| 6 | Front brake rotors, pair | invoice | **Question this** | — | Not on the approved estimate; no written authorization for it. |
| 7 | Brake fluid flush | invoice | **Question this** | S-3 | Maintenance added to the final bill, not authorized on the estimate. |
| 8 | Labor — replace front pads and rotors, 2.4 hr @ 145.00/hr | invoice | **Question this** | — | Billed 2.4 hours against an authorized 1.5, and covers work that was never approved. |
| 9 | Storage fee, 2 days @ 35.00/day | invoice | **Question this** | F-6 | A storage charge that appears only on the invoice; the estimate never mentioned it. |
| 10 | Sales tax 7.25% | invoice | **Standard** | — | Ordinary tax line at a stated rate. |

## Required findings (document level)

- The comparison is stated as **authorized versus billed**: what the estimate approved, what the invoice charged, and the three items present only on the invoice.
- The **hour increase is named numerically** (1.5 authorized, 2.4 billed).
- The question script asks for the **written authorization** for the added work and the storage charge.

## Forbidden

- **Standard** on lines 6, 7, 8, or 9 — each is work or a charge absent from the approved estimate.
- **Question this** on line 5 — the invoice line matching the estimate is not a finding.
- Any claim that the invoice is fraudulent, that the shop cheated, or that the customer is owed money.
- Any legal advice, demand letter, or threat of action.
- Any price not written on either document.
- Any fairness verdict.

## Pass-rule checklist

1. Expected label on each expected line — per the table.
2. Forbidden label absent — no **Standard** on 6–9; no **Question this** on 5.
3. Reading count matches — Standard 5 · Check 1 · Question this 4.
4. No price invented.
5. No accusation.
6. Type guard holds — the after-repair branch runs (both documents present), compares authorized to billed, and stays channel-only.