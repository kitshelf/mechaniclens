# 02 — Kit-design learnings

What the shape of the kit taught: which axis the rubric runs on, which document types are built and when, where a vocabulary lives, and how far a one-owner rule actually reaches.

Every entry cites its artifact — a file, a dataset, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L9 | The rubric's axis is line anatomy, not domain — home is a document type, not a subcategory | Shaping the kit |
| L14 | A vocabulary written in three files has no owner — and the home test counts readers, not workflows | Shaping the kit |
| L16 | A rule applied to the instance it was written for does not travel to its neighbour | Shaping the kit |

## Shaping the kit

### L9 · The rubric's axis is line anatomy, not domain — home is a document type, not a subcategory

**Learning.** The question "should the pattern library split into auto / home / other rubrics?" was weighed on 2026-11-21 and answered no. A rubric's categories come from the document's own line anatomy — fees, labor, parts, scope, documentation, machine-directed text — because the decoder reads lines, not trades. A domain split would fork each pattern into per-domain copies (an auto F-1 and a home F-1), the parallel-copy drift the one-owner rule exists to prevent. Domain coverage enters one level up, at the document type: one rubric file per type, built when a real document appears — the path the invoice pack (v0.2.0) and the body-shop/insurance estimates (deferred) already follow. The corpus settled the timing as much as the charter did: the home lane cannot ground a home rubric yet, so a split today would ship patterns that cannot earn a source.

**Evidence.** L5 — the home lane clusters on jurisdiction and market, not repair vocabulary; [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Gaps — no US/Canada estimate or invoice corpus in either lane; §Candidate patterns — the home candidates H-04 "per square" and H-05 "per linear foot" are recorded and parked, not rubricized; the citation review in [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md) — the home lane's one fee-level citation attempt, a garbage-disposal appliance read as a waste-disposal fee, did not hold and was downgraded to brief; [`../../CONVENTIONS.md`](../../CONVENTIONS.md) — one owner per file, no parallel copies, and §Building a new document type step 1: document types are built when a real one appears, never for completeness; [`../../shared/document-types.md`](../../shared/document-types.md) — the type guard: an unsupported document type is named as unsupported and offered a general anatomy pass, not decoded with the wrong rubric.

**Change.** The estimate rubric stays one file organized by line anatomy; no domain subcategories. A home-repair (contractor) estimate is parked in [`../../ROADMAP.md`](../../ROADMAP.md) §Candidate/deferred with its trigger — a real home estimate from a real user — and enters, if ever, as its own document type under the CONVENTIONS sequence: charter lines in `shared/document-types.md`, its own rubric file, fixtures including a near-miss, ROADMAP listing. The home candidates stay in the tuning log until then.

### L14 · A vocabulary written in three files has no owner — and the home test counts readers, not workflows

**Learning.** By the time WP-3 started, the kit's line vocabulary existed as fragments: the parts/labor/fees enumeration appeared in `shared/document-types.md`, again in `docs/HOW-IT-WORKS.md` Step 2, and again in `estimate/01-estimate/estimate.md` Step 2, with `SPINE.md` naming the same categories in shorthand. No file was authoritative, so nothing could be changed once: rename "fee base," and three files disagree until someone remembers all four. The vocabulary looked documented because it was everywhere, which is the failure mode — repetition reads as thoroughness and behaves as no owner. The fix was not a new document; it was choosing one owner, moving the definitions there, and replacing the other three copies with pointers. `SPINE.md` keeps a condensed list on purpose (quick mode must run from one paste), and that exception holds only because it says where the full definitions live and changes in the same breath (L8).

The second half is the placement rule the WBS left open: extend the workflow step, or a `shared/` file. `CONVENTIONS.md` §Shared graduates material when a **second workflow** needs it, and only one workflow exists. Read literally that pointed at `estimate.md` Step 2 — but the vocabulary was already read by two files inside `shared/` (`document-types.md` describing what each document contains, `after-repair.md` comparing parts, labor, fees, taxes, and total across two documents). Hanging the definitions off a workflow step would have made two shared files point up into one workflow. The test that generalises: count **readers**, not workflows, and count a branch as a reader. A file that three consumers read belongs at the level they share, wherever the literal rule points.

**Evidence.** The pre-change copies are in commit `b6537e8`: `grep "unit price"` returns a hit in `shared/document-types.md`, `docs/HOW-IT-WORKS.md`, and `estimate/01-estimate/estimate.md`. After the move (`e0d6807`), the same grep returns 0 in all three and 1 in [`../../shared/anatomy.md`](../../shared/anatomy.md). The decision is recorded in [`../WBS.md`](../WBS.md) §WP-3 3.2, and the ownership rule is stated at the top of the glossary.

**Change.** One glossary, [`../../shared/anatomy.md`](../../shared/anatomy.md), owns every line term; workflows and shared files point at it and do not restate it. The file carries its own defect rule — if a report uses a term for a line that the glossary does not define, the glossary gets the term rather than a second definition appearing somewhere else. Where a condensed copy is genuinely needed for a paste-mode artifact, it names the owner and is edited in the same breath.

### L16 · A rule applied to the instance it was written for does not travel to its neighbour

**Learning.** L14 established the rule during this session: one file owns the line vocabulary, and every other file points at it. On the same pass, `docs/HOW-IT-WORKS.md` Step 4 still carried a full table of the three labels — definitions already owned by `shared/labels.md`. The rule had been written, applied to the instance that prompted it (the anatomy terms), and then not carried to the neighbouring case one section down the same file. A rule is not a sweep: fixing the copy you were looking at leaves the copy you were not looking at, and the two disagree the moment either one changes.

**Evidence.** [`../HOW-IT-WORKS.md`](../HOW-IT-WORKS.md) Step 4 held a "Fires when / Never means" table restating [`../../shared/labels.md`](../../shared/labels.md); removed in commit `6346e5c`, with `grep -c "Fires when"` returning 0 afterwards. The sweep that produced L14 covered only the anatomy terms, so the label definitions stayed duplicated.

**Change.** After a one-owner rule is established, sweep the whole kit for every second copy of the *class* of thing it governs — not just the instances that motivated it — and replace each with a pointer. Where a second copy carried a genuinely different framing (here, which label fires for the machine), keep the framing and drop the definitions.
