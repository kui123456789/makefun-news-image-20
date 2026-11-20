#!/usr/bin/env python3
"""Draw the front page for 20 November 2026.

Renders a 1024x1024 newspaper front page -- masthead, a photo band and
six short stories -- and saves it as entry.png next to this file.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONTS = Path("/usr/share/fonts/truetype/noto")

PAGE = 1024
MARGIN = 32
CONTENT_W = PAGE - 2 * MARGIN

PAPER = (248, 244, 232)
INK = (24, 24, 24)
ACCENT = (140, 29, 24)
MUTED = (96, 89, 76)
HAIRLINE = (178, 170, 150)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


SERIF = "NotoSerif-Bold.ttf"
SERIF_IT = "NotoSerif-Italic.ttf"
SANS = "NotoSans-Regular.ttf"
SANS_BOLD = "NotoSans-Bold.ttf"


def wrap_lines(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines = []
    current = ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered(draw, y, text, fnt, fill):
    draw.text((PAGE // 2, y), text, font=fnt, fill=fill, anchor="ma")


def photo_band():
    """Crop the hero shot to the wide band the page needs."""
    hero = Image.open(HERE / "hero.png").convert("RGB")
    band_w, band_h = CONTENT_W, 296
    crop_h = int(hero.width * band_h / band_w)
    top = (hero.height - crop_h) // 2
    crop = hero.crop((0, top, hero.width, top + crop_h))
    return crop.resize((band_w, band_h), Image.LANCZOS)


STORIES = [
    (
        "WASHINGTON",
        "Trump puts Iran decision off to 2027",
        "The president says new strikes are \u201cnot urgent\u201d and will "
        "wait until \u201cafter January 1\u201d. The Senate votes 51\u201348 "
        "against limiting his war powers.",
    ),
    (
        "INDIA",
        "Cyclone Akvan bears down on east India",
        "Landfall is expected at noon on Friday between Narsapur and Puri, "
        "with winds of 90\u2013100 km/h. Odisha has moved more than 100,000 "
        "people to shelters.",
    ),
    (
        "KYIV",
        "Strikes damage two EU embassies in Kyiv",
        "Russian strikes hit the Austrian and Dutch embassies and a "
        "cathedral, killing one person. The EU will summon Russia\u2019s envoy.",
    ),
    (
        "BASEBALL",
        "Trump pardons baseball\u2019s Pete Rose",
        "A posthumous pardon for the late hits leader (4,256 hits) over a "
        "1990 tax offence. It does not affect his Hall of Fame vote.",
    ),
    (
        "CRICKET",
        "Phillips ton lifts New Zealand to 317\u20136",
        "In the first Test against India, Phillips makes 118 and Nicholls "
        "is 146 not out at lunch on day two.",
    ),
    (
        "CLIMATE",
        "COP31 draft drops fossil fuels",
        "The Antalya draft removes all fossil-fuel wording and concedes "
        "warming will pass 1.5\u00b0C.",
    ),
]


def main():
    page = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(page)

    # --- Masthead ---
    draw_centered(draw, 26, "THE WORLD TODAY", font(SERIF, 66), INK)
    draw_centered(
        draw, 108, "FRIDAY, 20 NOVEMBER 2026", font(SANS_BOLD, 21), ACCENT
    )
    draw.line([(MARGIN, 142), (PAGE - MARGIN, 142)], fill=INK, width=3)
    draw.line([(MARGIN, 148), (PAGE - MARGIN, 148)], fill=HAIRLINE, width=1)

    # --- Photo band ---
    photo = photo_band()
    page.paste(photo, (MARGIN, 160))
    draw.rectangle(
        [(MARGIN, 160), (PAGE - MARGIN - 1, 160 + 296 - 1)],
        outline=INK,
        width=1,
    )
    draw.text(
        (MARGIN, 462),
        "A carrier strike group at dusk, as Washington weighs its next move on Iran.",
        font=font(SERIF_IT, 17),
        fill=MUTED,
    )
    draw.line([(MARGIN, 490), (PAGE - MARGIN, 490)], fill=INK, width=2)

    # --- Six stories, two columns by three rows ---
    col_w = (CONTENT_W - 28) // 2
    row_h = 156
    grid_top = 506
    head_fnt = font(SERIF, 25)
    body_fnt = font(SANS, 17)
    kick_fnt = font(SANS_BOLD, 15)

    for index, (kicker, headline, summary) in enumerate(STORIES):
        col = index % 2
        row = index // 2
        x = MARGIN + col * (col_w + 28)
        y = grid_top + row * row_h

        draw.text((x, y), kicker, font=kick_fnt, fill=ACCENT)
        head_lines = wrap_lines(draw, headline, head_fnt, col_w)
        hy = y + 22
        for line in head_lines:
            draw.text((x, hy), line, font=head_fnt, fill=INK)
            hy += 29
        body_lines = wrap_lines(draw, summary, body_fnt, col_w)
        by = hy + 3
        for line in body_lines:
            draw.text((x, by), line, font=body_fnt, fill=(52, 50, 44))
            by += 21
        if by > y + row_h - 6:
            raise SystemExit(f"story {index + 1} overflows its cell")

    # --- Footer ---
    foot_y = grid_top + 3 * row_h + 8
    draw.line([(MARGIN, foot_y), (PAGE - MARGIN, foot_y)], fill=HAIRLINE, width=1)
    draw_centered(
        draw,
        foot_y + 10,
        "Sources: Reuters \u00b7 AP \u00b7 CNN \u00b7 AFP \u00b7 The Hindu \u00b7 "
        "Euronews \u00b7 UN News \u2014 full list in README",
        font(SANS, 15),
        MUTED,
    )

    out = HERE / "entry.png"
    page.save(out, format="PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
