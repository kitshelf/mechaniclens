# Worked examples

The kit's calibration story: one estimate that catches a pattern, and one clean estimate that must not be over-labeled.

| Example | Fixture | Reading | What it shows |
|---|---|---|---|
| [The catch](01-the-catch.md) | [`01-scope-mismatch`](../../tests/fixtures/01-scope-mismatch/message.txt) | Standard 1 · Check 2 · Question this 3 | A complaint about the rear of the car against an estimate for front brake work: the mismatch named once, the fee questioned, the tax left alone. |
| [The not-catch](02-the-not-catch.md) | [`07-clean-estimate`](../../tests/fixtures/07-clean-estimate/message.txt) | Standard 5 · Check 0 · Question this 0 | A credited diagnostic, a named OEM part with a number, book time and rate, a capped fee, a stated tax base, validity, and an authorization line — and therefore nothing to flag. |

**The not-catch is the important one.** A decoder that flags every line is not calibrated; the near-miss is how the kit proves it can leave a clean document alone. Both examples end with a "why it landed this way" section that names the pattern behind each label, including the ones that did **not** fire.

Each example is written from the same synthetic fixture its answer key governs, so the three never drift: the document in `tests/fixtures/`, the key on the expected reading, and the worked report here. They show the shape of a decode — not a recorded model run; those live in `tests/results/`.