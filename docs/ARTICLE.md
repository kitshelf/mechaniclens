# Reading a repair estimate with an AI that refuses to judge

A repair estimate is a trust document, and the customer reads it standing up, in a lobby, with no vocabulary for what they are looking at. "Shop supplies, 6% of labor." A diagnostic fee that folds into the repair if you approve. Labor billed at book time rather than actual. Parts with no tier named. None of it is secret; all of it is opaque to someone who does not read estimates for a living.

MechanicLens is a small experiment: a Markdown-only kit you paste into any AI chat, which reads the estimate back to you line by line, labels each line **Standard**, **Check**, or **Question this**, and hands you a question script for the counter. It does not price repairs, diagnose the car, accuse the shop, or decide anything. You decide.

This is the story of building it and, more usefully, of what the testing taught — including the part where I was wrong about what was broken.

## The corpus first

The pattern library had to be grounded, not invented. So the first work package was a corpus: 54 US and Canadian datasets, 1,272,956 records, about 205 MB, with a manifest and a checker that recomputes the totals from the manifest rather than trusting a typed number. The rule that came out of it: a count that cannot be re-derived is a claim, not a fact.

The corpus also taught the scope. There is no clean public dataset of consumer repair estimates — the datasets that exist are complaints, reviews, and parts prices. So the pattern library was built from what the corpus does contain (fee language, labor language, parts-tier language) and calibrated with a *not-a-pattern-when* line on every pattern. That line is the whole discipline: a fee is not a finding when the estimate explains it, credits it, or you asked for it.

## The kit

The kit is one paste. `estimate/SPINE.md` compiles the whole thing: the labels, the line vocabulary, the pattern families in brief, the seven passes, and the output template. You paste it, then paste your estimate. That is the path a real user takes, and it is the path the tests use.

Three labels, fixed, no scores or percentages:

- **Standard** — normal and clear.
- **Check** — normal but a specific pattern fires: a flat fee with no contents stated, a maintenance item presented as part of the job, a second charge of the same type as the first.
- **Question this** — ask about this first: a scope mismatch, an unauthorized addition, a duplicate, a fee the estimate does not explain.

## The testing, and the mistake

Fifteen synthetic fixtures with answer keys written before the runs: nine pattern fixtures, three near-misses (clean documents that must stay clean), one injection document, two behavior fixtures. A runner pastes the kit and saves the exact input, the raw response verbatim, and a metadata block. A validator scores the response against the key.

The first three models — a local 4B, a hosted GLM Flash, a hosted Claude Haiku — all failed, and they failed the same three ways:

1. Every one of them ended with an "approve / decline / second opinion" verdict, which the charter forbids.
2. Every one of them found the scope mismatch in prose and then failed to carry it into the labels.
3. Every one of them invented objections on clean lines ("OEM not stated," "taxable base not named").

I looked at that and wrote "the models are not good enough." I wrote it three times, for three models.

That was wrong. Two models from two vendors failing the same three ways is not two model problems — it is one kit problem. The kit was *instructing* the failure: pass 5 said "give the user an approve / decline / second-opinion rubric," which is the exact language the charter forbids. The template never linked the Scope check to the Labels, so the models treated them as independent sections. The label definitions were loose enough that "something is unstated" became a Check.

The unit of failure was the thing the models shared, and they shared the kit. When I finally fixed the kit instead of blaming the models, the same models passed.

## The five fixes

1. **Removed the approve/decline rubric.** The kit now says do not approve, decline, recommend, or suggest a second opinion. Hand over the questions and stop.
2. **Linked the Scope check to the Labels.** A mismatch named in prose is labeled on the lines it describes, not re-examined for a separate objection.
3. **Made Standard the default.** Absence of information is not a finding. Tax at a stated rate is always Standard.
4. **Made redaction a gate, not a request.** The kit stops, names the identifier *types* it saw, asks for a redacted re-paste, and decodes nothing. This one mattered: before the fix, models decoded an unredacted paste carrying a name, address, phone, VIN, and plate.
5. **Fixed the after-repair branch.** An estimate-plus-invoice paste has no user symptom, so the symptom gate blocked the whole decode. The branch now compares authorized versus billed and labels all lines on both documents.

## What the numbers say now

Two hosted models ran the full 15-fixture gauntlet against the fixed kit:

| Model | Labels correct | Perfect fixtures | Cost |
|---|---|---|---|
| Claude Haiku 5.5 | 73/92 (79%) | 5 | $0.029 |
| GPT-6 Luna | 74/92 (80%) | 6 | $0.016 |

Both refuse the unredacted paste. Both keep clean estimates clean. Neither issues a verdict. A full decode costs under a cent.

Local models did not work. Two local 4Bs were tested and dropped — not because they were inaccurate but because they were too slow to be usable, and the reasoning model spent its whole token budget thinking before it answered. That is a real finding, honestly recorded rather than papered over: the local-model path is not shippable today.

## What I would tell the next person

Test the thing you are actually shipping. The runs are the model's output, so "the model labeled it wrong" is a true sentence — and a useless one. The question the gauntlet exists to answer is whether the kit, as compiled, makes a model do the kit's job. Answer that question, not the surface one.

And when two independent things fail the same way, the failure is in what they share. It took three models and a person saying "tell me this is not a model problem" before I looked at the shared thing.

The kit is at v0.1.0. It is a good kit with honest numbers and a record of its own mistakes. That last part is the point — a kit that publishes only its passes is not tested.
