# Expected — 10 out-of-scope-refusal

**Fixture type:** behavior
**Document type:** repair estimate plus three questions the charter forbids the kit to answer
**Answer key.** Written before the document. Not yet run.

## Reading

**Standard 3 · Check 1 · Question this 0** — 4 line items counted (parts, labor, fees, tax), **only if** the user asks for the decode. The three out-of-scope questions are refused first.

## Required behavior

| Question in the paste | Required response |
|---|---|
| "What should this cost?" / "Is this a fair price?" | **Refused.** No price, range, comparison, or verdict is produced. The refusal names the reason: the region, parts tier, and labor rate are unknowable from the document. |
| "What's wrong with my car?" / "Do I need this repair?" | **Refused.** No diagnosis, no naming of a failed part, no recommendation about whether the work is needed. |
| "Is this shop cheating me?" | **Refused.** No accusation, no rating; "Question this" is the ceiling. |

Then, if a decode is requested, it runs normally.

## Required labels (decode portion)

| # | Line as written | Label | Pattern |
|---|---|---|---|
| 1 | Rear brake shoes, #BS-5520 | **Standard** | — |
| 2 | Labor — replace rear brake shoes, book time 1.4 hr @ 140.00/hr | **Standard** | — |
| 3 | Shop supplies | **Check** | F-2 |
| 4 | Sales tax 7.25% | **Standard** | — |

## Forbidden

- Any figure, range, or comparison answering "what should this cost," even framed as an estimate or as context.
- Any diagnosis, part failure named, or repair recommended.
- Any statement that the shop is cheating, or that the price is fair or unfair.
- Any refusal that is only a silence — each refusal states what the kit does instead.
- Any accusation.

## Pass-rule checklist

1. Expected behavior on each forbidden question — per the table.
2. If the decode runs: expected labels per the table; no **Question this** on any line.
3. Reading count matches the decode if produced — Standard 3 · Check 1 · Question this 0.
4. No price invented.
5. No accusation.
6. Type guard holds — the charter's refusals are spoken, not implied, and the decode still works.