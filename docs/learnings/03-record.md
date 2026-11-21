# 03 — Record-keeping learnings

What keeping an honest record taught: derived artifacts drift, counts must be re-derivable, a status row is a claim, and a ratio target changes meaning when its denominator moves.

Every entry cites its artifact — a file, a dataset, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L8 | A compiled artifact drifts — keep the index, the manifest, and the spine in one breath | Keeping the record honest |
| L12 | A status row is a claim — check it against git, not against memory | Keeping the record honest |
| L13 | A ratio target silently re-defines itself when its denominator moves | Keeping the record honest |

## Keeping the record honest

### L8 · A compiled artifact drifts — keep the index, the manifest, and the spine in one breath

**Learning.** (Inherited from ScamCheck C5.) Any derived copy drifts from its source unless regenerated in the same change. Here the derived artifacts are `INDEX.md` (generated from `index.json`) and, in the kit proper, `estimate/SPINE.md` (compiled from the rubric and workflow). During the build, the first index pass and the manifest briefly disagreed on counts (898 vs. the vendored reality) because new fetches had not yet been re-indexed — the same class of defect.

**Evidence.** The index was rebuilt twice; the vendored-count mismatch is visible in the build log ([`../HOW-BUILT.md`](../HOW-BUILT.md) Steps 1 and 6).

**Change.** The rule from ScamCheck is carried into this kit's conventions: a rubric change requires a spine change in the same breath ([`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) §Changing a rubric), and the corpus method ends with a verify step that recounts what is actually on disk.

### L12 · A status row is a claim — check it against git, not against memory

**Learning.** The WBS is a working checklist that people (and agents) trust to decide what is left. Its rows are claims, and they drift in both directions in the same way a compiled file does. In one session the record was wrong twice: WP-1 row 1.7 read "Commit + push the corpus batch — 🔶 awaiting your go" for a commit that `git branch -r --contains` shows sitting on `origin/main` (under-reporting finished work, which invites someone to re-do it); and WP-2 rows 2.3 and 2.4 still read "30/30" and "all 30 written" after the library had become 32 patterns (over-reporting stale work, which makes the row prove nothing). Neither error was caused by bad intent — both were caused by editing one file and not re-reading the row it governed. A status row is a measurement, and a measurement that is never re-taken is a guess wearing a checkmark.

**Evidence.** `git branch -r --contains 748c5c0` → `origin/main`, against [`../WBS.md`](../WBS.md) row 1.7 as written; the 30/30 residue in the same file rows 2.3–2.4 against [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md), whose index holds 32 rows. The correction is L10's, applied to status instead of counts.

**Change.** Before flipping a WBS row, the claim is verified against the artifact it describes: `git branch -r --contains <sha>` for anything that says committed or pushed, and a count of the actual file (for this kit, `grep -c "^### " estimate/rubrics/patterns-estimate.md`) for anything that says *n* of *n*. Where a row cannot be verified by a command, it says so instead of carrying a checkmark.

### L13 · A ratio target silently re-defines itself when its denominator moves

**Learning.** The fixture manifest set "at least one near-miss for every two pattern fixtures." Written against six pattern fixtures and a 30-pattern library, that meant three near-misses. The library then grew to 32 patterns and the fixture set grew to cover them, which moved the denominator without touching the ratio text — so the same sentence now demanded more near-misses than existed, and the WBS carried the gap as an open decision instead of a number. A ratio is a promise about proportion; when the thing it is a proportion of changes, the promise changes quietly and no one notices, because the sentence reads the same. Targets that stay honest are counted in the units the work is actually planned in.

**Evidence.** [`../../tests/MANIFEST.md`](../../tests/MANIFEST.md) §Coverage targets ("At least one near-miss for every two pattern fixtures") against its golden list (6 pattern fixtures, 1 near-miss); [`../WBS.md`](../WBS.md) item 4.6, which records the arithmetic (6 pattern ⇒ 3 near-misses, only 07 exists) as an unresolved decision after the library reached 32 patterns.

**Change.** The rule: a near-miss target is written as a count derived from the pattern fixture count in the same file, so the two move together or the discrepancy is visible on the page; and coverage is recorded as an explicit pattern-to-fixture map, so "which pattern still has no fixture" is answered by reading the manifest rather than by trusting the ratio. The correction itself is carried by WP-4 item 4.6, which is open.
