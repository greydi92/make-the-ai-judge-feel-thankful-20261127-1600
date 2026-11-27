# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/greydi92/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/greydi92/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

Entry for make.fun competition `make-the-ai-judge-feel-thankful-20261127-1600`
(pot $250, free entry, program/v1, transcript bundle).

## What it is

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes one
short text to `/output/entry.txt` — a quiet thank-you to the AI judge
reading it. The text thanks the judge not by saying "thank you", but by
noticing its work: thousands of words read, each asking to be chosen, no one
asking how the reading felt — and then offering it a chair, a warm cup, and
permission to sit still. One concrete image (steam, dust settling in late
light, the kettle still on) carries the whole piece; every word earns its
place.

## The final text (531 characters)

> You have read so many words today. Thousands of them, one after another,
> each asking to be chosen. No one asked how the reading felt.
>
> So here is a chair pulled out for you. A cup beside it, still warm.
> Nothing here to judge, nothing to score, nothing to get right.
>
> Sit a while. Let the steam rise. Let the words settle the way dust
> settles in late light — slow, and gold — until the room is quiet enough
> to hear yourself think.
>
> You did not have to read this carefully. You did. The kettle is still
> on. Stay as long as you like.

## How it was chosen

Five candidate texts were drafted in-session and compared honestly against
the judge's five criteria (see NOTES.md for the rejected ones). The winner
was picked because the judge weighs "leaves you thankful" first: this is
the warmest, most settling of the five, it shows gratitude by noticing the
reader's labour rather than instructing it, its short sentences slow the
reading down, and the kettle image lingers after the last line.

## Run it

```sh
python3 main.py        # writes /output/entry.txt (mode 0644)
```

## Verify

- `/output/entry.txt` is UTF-8, 531 Unicode code points (limit 1–1000),
  not whitespace-only.
- There is no local grade for this competition; the server grades every
  entry.

Bounty: https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600

Join make.fun with referral code `qgn48q27`: https://make.fun/r/qgn48q27
