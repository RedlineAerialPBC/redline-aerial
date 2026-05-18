#!/usr/bin/env python3
"""Generates a flashy Nextdoor promotional post image for Redline Aerial."""

import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
OUT = "public/nextdoor-post.png"
LOGO = "public/logo-main.png"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# Brand colors
RED       = (220, 20, 20)
RED_BRIGHT= (255, 50, 50)
RED_DIM   = (140, 10, 10)
WHITE     = (255, 255, 255)
OFF_WHITE = (230, 232, 238)
SILVER    = (190, 195, 205)
GRAY      = (130, 135, 148)
BLACK     = (0, 0, 0)


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except Exception:
        return ImageFont.load_default()


def cx_text(draw, y, text, f, color, width=W, shadow=False, shadow_color=(0,0,0)):
    if shadow:
        bbox = draw.textbbox((0, 0), text, font=f)
        tw = bbox[2] - bbox[0]
        x = (width - tw) // 2
        draw.text((x+3, y+3), text, font=f, fill=shadow_color)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    x = (width - tw) // 2
    draw.text((x, y), text, font=f, fill=color)
    return bbox[3] - bbox[1]


def rrect(draw, xy, r, fill=None, outline=None, ow=2):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=ow)


# ── 1. BASE BACKGROUND ────────────────────────────────────────────────────────
base = Image.new("RGB", (W, H))
bd = ImageDraw.Draw(base)

# Rich dark gradient top→bottom
for y in range(H):
    t = y / H
    r = int(8  + t * 18)
    g = int(8  + t * 8)
    b = int(12 + t * 20)
    bd.line([(0, y), (W, y)], fill=(r, g, b))

# ── 2. DIAGONAL RED SLASH BAND ────────────────────────────────────────────────
slash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(slash)

# Main diagonal band
angle_pts = [(-80, H//2 - 60), (W+80, H//2 - 280),
             (W+80, H//2 - 160), (-80, H//2 + 40)]
sd.polygon(angle_pts, fill=(220, 20, 20, 55))

# Thinner bright edge line above
edge1 = [(-80, H//2 - 62), (W+80, H//2 - 282),
          (W+80, H//2 - 270), (-80, H//2 - 50)]
sd.polygon(edge1, fill=(255, 80, 80, 130))

# Subtle second band below
band2 = [(-80, H//2 + 60), (W+80, H//2 - 160),
          (W+80, H//2 - 130), (-80, H//2 + 90)]
sd.polygon(band2, fill=(180, 10, 10, 35))

base = Image.alpha_composite(base.convert("RGBA"), slash).convert("RGB")

# ── 3. GLOW LAYERS (soft blurred circles) ────────────────────────────────────
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)

# Top-center red halo behind logo
for i in range(60):
    a = int(38 * (1 - i/60)**2)
    r = 180 + i * 9
    gd.ellipse([W//2-r, 30-r//2, W//2+r, 30+r//2], fill=(220, 20, 20, a))

# Bottom right accent glow
for i in range(40):
    a = int(25 * (1 - i/40)**2)
    r = 100 + i * 8
    gd.ellipse([W-r-60, H-r-60, W+r-60, H+r-60], fill=(200, 15, 15, a))

glow_blur = glow.filter(ImageFilter.GaussianBlur(radius=30))
base = Image.alpha_composite(base.convert("RGBA"), glow_blur).convert("RGB")

# ── 4. GRID LINES (subtle perspective grid) ───────────────────────────────────
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
grd = ImageDraw.Draw(grid)

# Horizontal grid lines fading out
for i in range(8):
    y = H//2 + 30 + i * 62
    a = max(0, 28 - i * 4)
    grd.line([(0, y), (W, y)], fill=(180, 180, 200, a), width=1)

# Converging vertical grid lines from bottom
vp_x, vp_y = W//2, H//2 + 30
for i in range(-6, 7):
    ex = i * 90
    a = max(0, 22 - abs(i) * 3)
    grd.line([(vp_x + ex*6, H), (vp_x, vp_y)], fill=(180, 180, 200, a), width=1)

base = Image.alpha_composite(base.convert("RGBA"), grid).convert("RGB")

# ── 5. LOGO ───────────────────────────────────────────────────────────────────
logo = Image.open(LOGO).convert("RGBA")
scale = 0.46
nw, nh = int(logo.width * scale), int(logo.height * scale)
logo = logo.resize((nw, nh), Image.LANCZOS)

# Drop shadow for logo
shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
s_img = Image.new("RGBA", (nw+30, nh+30), (0, 0, 0, 0))
s_img.paste((0, 0, 0, 180), [8, 8, nw+8, nh+8])
s_img = s_img.filter(ImageFilter.GaussianBlur(12))
lx = (W - nw) // 2
ly = 38
shadow_layer.paste(s_img, (lx - 15, ly - 15), s_img)
base = Image.alpha_composite(base.convert("RGBA"), shadow_layer).convert("RGB")
base.paste(logo, (lx, ly), logo)

draw = ImageDraw.Draw(base)
logo_bottom = ly + nh

# ── 6. TAGLINE ────────────────────────────────────────────────────────────────
f_oblique  = font("DejaVuSans-BoldOblique.ttf", 30)
f_bold_xl  = font("DejaVuSans-Bold.ttf", 58)
f_bold_lg  = font("DejaVuSans-Bold.ttf", 44)
f_bold_md  = font("DejaVuSans-Bold.ttf", 31)
f_bold_sm  = font("DejaVuSans-Bold.ttf", 26)
f_bold_xs  = font("DejaVuSans-Bold.ttf", 22)
f_reg_md   = font("DejaVuSans.ttf", 28)
f_reg_sm   = font("DejaVuSans.ttf", 24)
f_reg_xs   = font("DejaVuSans.ttf", 20)

tag_y = logo_bottom + 10
cx_text(draw, tag_y, "✦  YOUR NEIGHBOR IN THE SKY  ✦", f_oblique, RED_BRIGHT, shadow=True)

# Divider with red diamonds
div_y = tag_y + 44
draw.rectangle([80, div_y+1, W//2-40, div_y+2], fill=(220, 20, 20, 180))
draw.rectangle([W//2+40, div_y+1, W-80, div_y+2], fill=(220, 20, 20, 180))
draw.polygon([W//2-12, div_y-6, W//2, div_y+8, W//2+12, div_y-6, W//2, div_y-18],
             fill=RED_BRIGHT)

# ── 7. HEADLINE ───────────────────────────────────────────────────────────────
hl_y = div_y + 24
cx_text(draw, hl_y,      "PROFESSIONAL DRONE", f_bold_xl, WHITE, shadow=True, shadow_color=(0,0,0))
cx_text(draw, hl_y + 68, "PHOTOGRAPHY", f_bold_xl, RED_BRIGHT, shadow=True, shadow_color=(80,0,0))

sub_y = hl_y + 140
cx_text(draw, sub_y, "Right Here in South Florida", f_bold_md, SILVER, shadow=True)

# ── 8. SERVICES CARD ─────────────────────────────────────────────────────────
card_y = sub_y + 52
card_x1, card_x2 = 48, W - 48
card_h = 218

# Card background with RGBA
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.rounded_rectangle([card_x1, card_y, card_x2, card_y+card_h],
                     radius=20, fill=(20, 18, 26, 215))
od.rounded_rectangle([card_x1, card_y, card_x2, card_y+card_h],
                     radius=20, outline=(220, 20, 20, 160), width=2)
# Top inner glow line
od.rounded_rectangle([card_x1+1, card_y+1, card_x2-1, card_y+3],
                     radius=2, fill=(255, 80, 80, 80))
base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
draw = ImageDraw.Draw(base)

# "WHAT I CAN DO FOR YOU" header in card
cx_text(draw, card_y + 14, "— WHAT I CAN DO FOR YOU —", f_bold_sm, RED_BRIGHT)

services = [
    ("🏠", "Roof & property photos for insurance claims"),
    ("🏡", "Real estate aerial listing photos"),
    ("⛈", "Storm damage documentation"),
    ("📋", "Homeowner roof records & maintenance"),
]
item_y = card_y + 54
col_x = card_x1 + 30
for icon, text in services:
    # Red bullet
    draw.ellipse([col_x, item_y+8, col_x+14, item_y+22], fill=RED_BRIGHT)
    draw.text((col_x + 24, item_y), text, font=f_reg_sm, fill=OFF_WHITE)
    item_y += 40

# ── 9. CREDENTIAL BADGES ─────────────────────────────────────────────────────
badge_y = card_y + card_h + 22
badges = [
    ("FAA PART 107", "Certified Pilot"),
    ("FIREFIGHTER", "Owned & Operated"),
    ("24-HOUR", "Turnaround Available"),
]
bw, bh = 302, 88
bx_start = (W - (bw * 3 + 24)) // 2

for i, (line1, line2) in enumerate(badges):
    bx = bx_start + i * (bw + 12)

    # Badge with gradient effect
    badge_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bad = ImageDraw.Draw(badge_overlay)
    bad.rounded_rectangle([bx, badge_y, bx+bw, badge_y+bh],
                          radius=14, fill=(30, 8, 8, 230))
    bad.rounded_rectangle([bx, badge_y, bx+bw, badge_y+bh],
                          radius=14, outline=(220, 20, 20, 200), width=2)
    # Top highlight
    bad.rounded_rectangle([bx+2, badge_y+2, bx+bw-2, badge_y+6],
                          radius=4, fill=(255, 100, 100, 60))
    base = Image.alpha_composite(base.convert("RGBA"), badge_overlay).convert("RGB")
    draw = ImageDraw.Draw(base)

    b1_bbox = draw.textbbox((0, 0), line1, font=f_bold_sm)
    b1w = b1_bbox[2] - b1_bbox[0]
    draw.text((bx + (bw - b1w)//2, badge_y + 12), line1, font=f_bold_sm, fill=WHITE)

    b2_bbox = draw.textbbox((0, 0), line2, font=f_reg_xs)
    b2w = b2_bbox[2] - b2_bbox[0]
    draw.text((bx + (bw - b2w)//2, badge_y + 48), line2, font=f_reg_xs, fill=SILVER)

# ── 10. PRICING BAR ──────────────────────────────────────────────────────────
price_y = badge_y + bh + 22
price_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pd = ImageDraw.Draw(price_overlay)
pd.rounded_rectangle([80, price_y, W-80, price_y+72],
                     radius=12, fill=(200, 15, 15, 90))
pd.rounded_rectangle([80, price_y, W-80, price_y+72],
                     radius=12, outline=(255, 60, 60, 180), width=2)
base = Image.alpha_composite(base.convert("RGBA"), price_overlay).convert("RGB")
draw = ImageDraw.Draw(base)

cx_text(draw, price_y + 8,  "Starting at $150  ·  Same-Day Available", f_bold_md, WHITE, shadow=True)
cx_text(draw, price_y + 46, "Serving Palm Beach & Broward County", f_reg_xs, SILVER)

# ── 11. CTA / CONTACT ────────────────────────────────────────────────────────
cta_y = price_y + 96
cx_text(draw, cta_y,      "redlineaerialpb.com", f_bold_lg, RED_BRIGHT, shadow=True, shadow_color=(80,0,0))
cx_text(draw, cta_y + 58, "redlineaerialpb@gmail.com", f_reg_md, SILVER)
cx_text(draw, cta_y + 96, "Drop a comment or DM — happy to help your neighbors!", f_reg_xs, GRAY)

# ── 12. TOP & BOTTOM ACCENT BARS ─────────────────────────────────────────────
draw.rectangle([0, 0, W, 8], fill=RED_BRIGHT)
draw.rectangle([0, H-8, W, H], fill=RED_BRIGHT)

# Corner accent brackets
bracket_size = 30
bracket_w = 4
corners = [(0, 0), (W-bracket_size, 0), (0, H-bracket_size), (W-bracket_size, H-bracket_size)]
for (cx2, cy2) in corners:
    if cx2 == 0 and cy2 == 0:
        draw.rectangle([cx2, cy2+8, cx2+bracket_size, cy2+8+bracket_w], fill=RED_BRIGHT)
        draw.rectangle([cx2, cy2+8, cx2+bracket_w, cy2+bracket_size], fill=RED_BRIGHT)
    elif cx2 != 0 and cy2 == 0:
        draw.rectangle([cx2, cy2+8, cx2+bracket_size, cy2+8+bracket_w], fill=RED_BRIGHT)
        draw.rectangle([cx2+bracket_size-bracket_w, cy2+8, cx2+bracket_size, cy2+bracket_size], fill=RED_BRIGHT)
    elif cx2 == 0 and cy2 != 0:
        draw.rectangle([cx2, cy2+bracket_size-bracket_w, cx2+bracket_size, cy2+bracket_size], fill=RED_BRIGHT)
        draw.rectangle([cx2, cy2, cx2+bracket_w, cy2+bracket_size], fill=RED_BRIGHT)
    else:
        draw.rectangle([cx2, cy2+bracket_size-bracket_w, cx2+bracket_size, cy2+bracket_size], fill=RED_BRIGHT)
        draw.rectangle([cx2+bracket_size-bracket_w, cy2, cx2+bracket_size, cy2+bracket_size], fill=RED_BRIGHT)

# ── 13. SAVE ─────────────────────────────────────────────────────────────────
base.save(OUT, "PNG", optimize=True)
print(f"Saved → {OUT}")
