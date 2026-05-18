#!/usr/bin/env python3
"""Generates a Nextdoor-friendly promotional post image for Redline Aerial."""

from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
OUT = os.path.join(os.path.dirname(__file__), "..", "public", "nextdoor-post.png")
LOGO = os.path.join(os.path.dirname(__file__), "..", "public", "logo-main.png")

RED = (204, 0, 0)
RED_LIGHT = (230, 40, 40)
WHITE = (255, 255, 255)
OFF_WHITE = (220, 220, 225)
GRAY = (160, 160, 170)
BG_DARK = (14, 14, 16)
BG_MID = (22, 22, 26)
CARD_BG = (28, 28, 34, 210)


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def centered_text(draw, y, text, font, color, width=W):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (width - tw) // 2
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]  # height


def draw_rounded_rect(draw, xy, radius, fill, outline=None, outline_width=2):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill,
                            outline=outline, width=outline_width)


def draw_checkmark_item(draw, x, y, text, font, color=OFF_WHITE, dot_color=RED):
    draw.ellipse([x, y + 6, x + 18, y + 24], fill=dot_color)
    draw.text((x + 28, y), text, font=font, fill=color)
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


# ── Canvas ──────────────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H), BG_DARK)
draw = ImageDraw.Draw(img)

# Vertical gradient background
for y in range(H):
    t = y / H
    r = int(14 + t * 12)
    g = int(14 + t * 6)
    b = int(16 + t * 14)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Subtle radial vignette from top center (no hard rings)
vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(vignette)
for i in range(30):
    alpha = int(22 * (1 - i / 30))
    r = 320 + i * 14
    cx, cy = W // 2, 0
    vd.ellipse([cx - r, cy - r // 2, cx + r, cy + r // 2], fill=(204, 0, 0, alpha))
img = Image.alpha_composite(img.convert("RGBA"), vignette).convert("RGB")

# Top accent bar
draw.rectangle([0, 0, W, 7], fill=RED)

# Bottom accent bar
draw.rectangle([0, H - 7, W, H], fill=RED)

# ── Fonts ────────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
f_bold_lg = load_font(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 54)
f_bold_md = load_font(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 38)
f_bold_sm = load_font(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 29)
f_bold_xs = load_font(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 24)
f_reg_md = load_font(f"{FONT_DIR}/DejaVuSans.ttf", 30)
f_reg_sm = load_font(f"{FONT_DIR}/DejaVuSans.ttf", 26)
f_reg_xs = load_font(f"{FONT_DIR}/DejaVuSans.ttf", 22)
f_oblique = load_font(f"{FONT_DIR}/DejaVuSans-BoldOblique.ttf", 32)

# ── Logo ─────────────────────────────────────────────────────────────────────
logo = Image.open(LOGO).convert("RGBA")
scale = 0.36
nw = int(logo.width * scale)
nh = int(logo.height * scale)
logo = logo.resize((nw, nh), Image.LANCZOS)
img.paste(logo, ((W - nw) // 2, 28), logo)
logo_bottom = 28 + nh

draw = ImageDraw.Draw(img, "RGBA")

# ── Tagline ──────────────────────────────────────────────────────────────────
tag_y = logo_bottom + 14
centered_text(draw, tag_y, "Your Neighbor in the Sky", f_oblique, RED_LIGHT)

# Thin divider
div_y = tag_y + 46
draw.rectangle([120, div_y, W - 120, div_y + 2], fill=(204, 0, 0, 160))

# ── Headline ─────────────────────────────────────────────────────────────────
hl_y = div_y + 22
centered_text(draw, hl_y, "Professional Drone Photography", f_bold_md, WHITE)
centered_text(draw, hl_y + 50, "Right Here in South Florida", f_bold_md, WHITE)

# ── Services card ────────────────────────────────────────────────────────────
card_y = hl_y + 124
card_x1, card_x2 = 60, W - 60
card_h = 230
draw_rounded_rect(draw, [card_x1, card_y, card_x2, card_y + card_h],
                  radius=18, fill=(28, 28, 36, 200), outline=(204, 0, 0, 120), outline_width=2)

draw = ImageDraw.Draw(img)  # switch back to non-RGBA draw for text

centered_text(draw, card_y + 18, "What I Can Do For You", f_bold_sm, RED_LIGHT)

services = [
    "Roof & property photos for insurance claims",
    "Real estate aerial listing photos",
    "Storm damage documentation",
    "Homeowner roof records & maintenance",
]
item_y = card_y + 64
for svc in services:
    draw_checkmark_item(draw, card_x1 + 36, item_y, svc, f_reg_sm)
    item_y += 42

# ── Badges row ───────────────────────────────────────────────────────────────
badge_y = card_y + card_h + 26
badges = [
    ("FAA Part 107", "Certified Pilot"),
    ("Firefighter", "Owned & Operated"),
    ("24-Hour", "Turnaround Available"),
]
bw = 290
bh = 84
bx = (W - (bw * 3 + 30)) // 2
for i, (line1, line2) in enumerate(badges):
    bx_cur = bx + i * (bw + 15)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_rounded_rect(draw, [bx_cur, badge_y, bx_cur + bw, badge_y + bh],
                      radius=12, fill=(36, 12, 12, 220), outline=(204, 0, 0, 180), outline_width=2)
    draw = ImageDraw.Draw(img)
    b1_bbox = draw.textbbox((0, 0), line1, font=f_bold_xs)
    b1w = b1_bbox[2] - b1_bbox[0]
    draw.text((bx_cur + (bw - b1w) // 2, badge_y + 10), line1, font=f_bold_xs, fill=WHITE)
    b2_bbox = draw.textbbox((0, 0), line2, font=f_reg_xs)
    b2w = b2_bbox[2] - b2_bbox[0]
    draw.text((bx_cur + (bw - b2w) // 2, badge_y + 42), line2, font=f_reg_xs, fill=GRAY)

# ── Pricing callout ──────────────────────────────────────────────────────────
price_y = badge_y + bh + 28
draw = ImageDraw.Draw(img, "RGBA")
draw_rounded_rect(draw, [200, price_y, W - 200, price_y + 68],
                  radius=10, fill=(180, 0, 0, 60), outline=(204, 0, 0, 140), outline_width=2)
draw = ImageDraw.Draw(img)
centered_text(draw, price_y + 10, "Starting at $150  ·  Same-Day Available", f_bold_sm, WHITE)
centered_text(draw, price_y + 46, "Palm Beach & Broward County", f_reg_xs, GRAY)

# ── CTA / contact ────────────────────────────────────────────────────────────
cta_y = price_y + 106
centered_text(draw, cta_y, "redlineaerialpb.com", f_bold_md, RED_LIGHT)
centered_text(draw, cta_y + 56, "redlineaerialpb@gmail.com", f_reg_md, GRAY)

# Friendly closing line
centered_text(draw, cta_y + 104, "Happy to answer any questions — drop a comment or DM!", f_reg_xs, GRAY)

# ── Save ─────────────────────────────────────────────────────────────────────
img.save(OUT, "PNG", optimize=True)
print(f"Saved to {OUT}")
