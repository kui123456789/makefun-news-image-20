[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kui123456789/makefun-news-image-20/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kui123456789/makefun-news-image-20/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — 20 November 2026

A one-page newspaper front page summing up Friday 20 November 2026 in a
single image. The masthead names the day, a dusk photograph of a carrier
strike group leads the page, and six short stories below it cover the
day's most consequential news — from Washington, India, Kyiv, the
baseball world, the cricket field and the COP31 talks in Antalya.

## The six stories

1. **Trump puts Iran decision off to 2027** — The president says new
   strikes on Iran are "not urgent" and will wait until "after January 1";
   the Senate votes 51–48 against a war-powers limit.
2. **Cyclone Akvan bears down on east India** — Landfall is expected at
   noon on Friday between Narsapur and Puri, with winds of 90–100 km/h;
   Odisha has moved more than 100,000 people to shelters.
3. **Strikes damage two EU embassies in Kyiv** — Russian strikes damage
   the Austrian and Dutch embassies and a cathedral, killing one person;
   the EU will summon Russia's envoy.
4. **Trump pardons baseball's Pete Rose** — A posthumous pardon for the
   late hits leader (4,256 hits) over a 1990 tax offence; it does not
   affect his Hall of Fame vote.
5. **Phillips ton lifts New Zealand to 317–6** — In the first Test against
   India, Phillips makes 118 and Nicholls is 146 not out at lunch on
   day two.
6. **COP31 draft drops fossil fuels** — The Antalya draft removes all
   fossil-fuel wording and concedes warming will pass 1.5°C.

## Sources

- Reuters — Iran decision, Pete Rose pardon, Phillips century,
  COP31 draft
- New York Post, The News, BusinessWorld — Iran decision
- The Hindu, The Hindu BusinessLine / PTI, TBS News, IMD — Cyclone Akvan
- Euronews, AFP, Kyiv24 — Kyiv embassy strikes
- CNN, AP, USA Today — Pete Rose pardon
- Sportskeeda — Phillips century
- UN News, Business Day — COP31 draft

## How it works

`draw.py` renders the front page with Pillow: it crops the supplied
`hero.png` photograph into a wide band under the masthead, then lays out
the six stories in a two-column grid with a headline and a short summary
each. The result is saved as `entry.png` (1024×1024, under 1 MiB).
`main.py` — standard library only — copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR` (default `/output`).

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
