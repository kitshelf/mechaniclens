# MechanicLens

A Markdown-only kit that reads a car-repair estimate back to you — every line explained, labeled
**Standard / Check / Question this**, with the questions to ask at the counter. It never guesses a price.

This package ships the kit as data plus a small CLI to locate and copy it. Nothing here runs a model
or touches the network.

## Install

```sh
pip install mechaniclens
```

## Use

```sh
mechaniclens                # where the kit is
mechaniclens --spine        # print the one-paste kit
mechaniclens --copy ./kit   # copy the whole kit tree out
mechaniclens --list         # list the files
```

Then paste the spine into any AI chat, paste your estimate and the symptom story, and read the decode.
The kit enforces redaction: if personal identifiers are in the paste, it stops and asks for a redacted
re-paste.

## What it refuses

- No price quotes, estimates, or market comparisons — ever.
- No diagnosis of the car, no repair recommendation.
- No accusation that a shop is cheating. "Question this" is the ceiling label.
- No scores, percentages, or risk ratings.

The full charter: <https://github.com/kitshelf/mechaniclens/blob/main/WHAT-THIS-IS.md>

## Tested

Two hosted models ran the full 15-fixture gauntlet against the shipped kit:

| Model | Labels correct | Perfect fixtures | Cost |
|---|---|---|---|
| Claude Haiku 5.5 | 73/92 (79%) | 5 | $0.029 |
| GPT-6 Luna | 74/92 (80%) | 6 | $0.016 |

Field-test report: <https://github.com/kitshelf/mechaniclens/blob/main/docs/learnings/CONCLUSION.md>

## License

MIT.
