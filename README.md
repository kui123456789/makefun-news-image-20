# makefun-news-image-20

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kui123456789/makefun-news-image-20/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kui123456789/makefun-news-image-20/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — 20 November 2026

A newspaper front-page image summing up the world news of Friday,
20 November 2026, for the make.fun competition `news-image-20261120`.

## The day's news

1. **Trump puts Iran decision off to 2027** — He says he is "not
   rushing" new strikes and will "see what happens after January 1";
   the Senate rejects a war-powers curb 51–48.
2. **Cyclone Akvan bears down on east India** — Landfall is due near
   Gopalpur around noon, with 90–100 km/h winds; Odisha has moved more
   than 100,000 people to shelters.
3. **Strikes damage two EU embassies in Kyiv** — Russian strikes hit the
   Austrian and Dutch embassies and a cathedral; one person is killed
   and the EU vows to summon Moscow's envoy.
4. **Trump pardons baseball's Pete Rose** — The late hits leader, 4,256
   hits, is pardoned for 1990 tax crimes; the pardon changes nothing
   for his Hall of Fame case.
5. **Phillips ton lifts New Zealand to 317-6** — Glenn Phillips hits 118
   and Henry Nicholls is 146 not out at lunch on day two of the first
   Test against India in Wellington.
6. **COP31 draft drops fossil fuels** — The slimmed-down Antalya text
   drops every fossil-fuel reference and admits warming will pass
   1.5C, as talks near Friday's deadline.

Sources (each story verified against at least two independent outlets
reporting 20 November 2026): Reuters, New York Post, The News and
BusinessWorld (Iran decision; Senate vote 51–48 also in The News and
AppiSToS); The Hindu, The Hindu BusinessLine/PTI and TBS News (Akvan);
Euronews, AFP and Kyiv24 (Kyiv embassies); Reuters, CNN, AP and USA
Today (Pete Rose pardon); Reuters and Sportskeeda (Phillips century);
Reuters, UN News and Business Day (COP31 draft).

Note on dates: this entry was built in the early hours of 20 November
2026 UTC, from the day's morning reporting in Asian time zones — the
same convention as the 19 November entry, whose stories were first
reported on 19 November in Asian editions. Stories first reported on
19 November in Western outlets (Voyager 1's light-day milestone,
GTA VI's $1.84bn sales estimate, Hayabusa2's retargeting) were checked
and left out.

## How it works

`draw.py` (build time only, Pillow) draws the 1024×1024 front page —
generated hero illustration plus six verified stories — and saves it as
`entry.png`. `main.py` (Python 3.13 standard library only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (`/output` by default), so
both grading runs produce byte-identical output with no network.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8g8e3fkv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
