# Roadmap

What MechanicLens has shipped and what is planned. Document types are built when a real one appears (see [`CONVENTIONS.md`](CONVENTIONS.md)); this file is where deferred work is parked so nothing is lost.

---

## v0.1.0, in development

The repair-estimate workflow, end to end.

- **Foundation** — charter, conventions, shared DNA, PRD (`docs/prd/`), agent and harness pointers. *(structure in place)*
- **The estimate workflow** — `estimate/`: redact → anatomy → symptom check → label → question script → decision → after-repair. `SPINE.md` compiles the whole kit into one paste. *(skeleton in place)*
- **The pattern library** — `estimate/rubrics/estimate-patterns.md`: the estimate-pattern library, one file for the repair estimate. Every pattern carries a *not-a-pattern-when* calibration line and a source. *(draft; sources and verification pending)*
- **Shared material** — the three labels, the document types, the redaction pass, the local-model guidance, and the after-repair branch. *(skeleton in place)*
- **Tests** — 8 synthetic estimates with expected keys, written before the runs: scope mismatch, folded diagnostic fee, fee stacking, duplicate parts, "while we're in there" add-ons, invoice-versus-estimate, a near-miss clean estimate, and an injection document. *(planned; none written yet)*
- **Worked examples** — the catch and the not-catch: one estimate with a planted pattern, one clean estimate that must not be over-labeled. *(planned)*
- **User guide** — the ninety-second walkthrough for a non-technical reader, with the redaction sample. *(stub)*
- **Release** — tag `v0.1.0`, GitHub release, README status flip, `CHANGELOG.md` entry, and the dev.to article. *(pending)*

**v0.1.0 is done when** a user decodes a real estimate in a lobby, asks two questions from the kit, and verifies one answer on the spot — and the fixture gauntlet passes with a near-miss that stays clean.

**Scope freeze.** After this list, v0.1.0 takes no new scope; new ideas go to Deferred below.

## v0.2.0, planned

- **After-repair branch, tested** — the invoice-versus-estimate comparison as a full workflow: what was signed, what was billed, what to keep. Channels only; no legal advice.
- **Document-type pack: invoice** — the invoice's own line patterns and question script, promoted from the after-repair branch when its fixtures pass.
- **Maintenance-schedule decode** — the 30k/60k/90k service menu read against what the owner's manual actually requires; "recommended" vs "required" made visible line by line.
- **Work-order / authorization decode** — what the signature actually authorizes: teardown fees, authorization limits, "additional work will be billed" clauses.
- **Warranty / campaign flag** — line-level only: "this line may be covered under a campaign — `[CONFIRM]` with your VIN at the dealer." Flag-only, never a coverage verdict.
- **Parts decode table** — OEM vs aftermarket vs remanufactured vs salvage, one question each; the tiers the estimate rarely names.

## v0.3.0, planned

- **Second-opinion prep pack** — printable: what to photograph, what to copy, what to ask before leaving shop #1.
- **Multi-quote comparison** — two estimates diffed line by line: scope vs scope, never price vs price.
- **"Scary-but-normal" calibration doc** — the things that look alarming but are standard; the mirror of the pattern library, there to keep the kit honest.
- **Re-verification pass** — a dated "verified as of" sweep over the whole pattern library, the same drift habit ScamCheck keeps.

## Candidate / deferred

| Item | Why it waits |
|---|---|
| Body-shop and insurance estimates | A different document type with insurer-written language and supplement rules; needs its own pattern library and fixtures. Build only when a real document appears. |
| Dealership vs. independent comparison | A price comparison in disguise; the charter bans prices. Parked unless the framing stays purely documentary. |
| Parts-tier decoder | Useful, but the line-level data is often absent from the estimate; build only if fixtures show the pattern is decodable. |
| Repair-shop review layer | The charter refuses accusations and ratings. Permanently out of scope. |

## Non-goals (not planned, ever)

Price databases, "should cost" estimates, market comparisons, diagnosis, repair recommendations, shop ratings, fraud accusations, negotiation scripts, legal or financial advice, and hosted accounts. See the charter's "what it is not."

---

## How to use this file

- Move an item here when it is ruled out of scope for the current version.
- When a document type's need is real, promote it and build it per `CONVENTIONS.md` §Building a new document type.
- Keep the "shipped" list accurate; it is the record of what actually works.
