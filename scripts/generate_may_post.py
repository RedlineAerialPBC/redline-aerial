#!/usr/bin/env python3
"""May hurricane-prep themed Nextdoor post image for Redline Aerial."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
OUT  = "public/nextdoor-may-post.png"
LOGO = "public/logo-main.png"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

RED        = (220, 20, 20)
RED_BRIGHT = (255, 60, 60)
RED_DIM    = (130, 8, 8)
ORANGE     = (230, 110, 20)
ORANGE_DIM = (180, 80, 10)
AMBER      = (255, 180, 0)
WHITE      = (255, 255, 255)
OFF_WHITE  = (228, 232, 240)
SILVER     = (185, 192, 205)
GRAY       = (120, 128, 142)
DARK       = (10, 10, 14)


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except Exception:
        return ImageFont.load_default()


def cx(draw, y, text, f, color, shadow=False, sc=(0, 0, 0)):
    bb = draw.textbbox((0, 0), text, font=f)
    tw = bb[2] - bb[0]
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 3, y + 3), text, font=f, fill=sc)
    draw.text((x, y), text, font=f, fill=color)
    return bb[3] - bb[1]


def overlay_rgba(base, layer):
    return Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB")


def rrect_rgba(size, xy, r, fill=None, outline=None, ow=2):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=ow)
    return layer


# ── 1. BACKGROUND ─────────────────────────────────────────────────────────────
base = Image.new("RGB", (W, H))
bd = ImageDraw.Draw(base)

# Deep storm-sky gradient: near-black navy at top → dark charcoal at bottom
for y in range(H):
    t = y / H
    r = int(6  + t * 16)
    g = int(8  + t * 10)
    b = int(18 + t * 24)
    bd.line([(0, y), (W, y)], fill=(r, g, b))

# ── 2. STORMY ATMOSPHERE LAYERS ───────────────────────────────────────────────
# Dramatic wide sweep from top-left
sweep = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(sweep)
for i in range(50):
    a = int(30 * (1 - i / 50) ** 1.6)
    sd.polygon([(-100, -100 + i * 8), (W + 100, H // 3 - i * 4),
                (W + 100, H // 3 - i * 4 + 60), (-100, -100 + i * 8 + 80)],
               fill=(40, 10, 80, a))
base = overlay_rgba(base, sweep)

# Amber/orange warning glow from bottom center (hurricane warning color)
warm = Image.new("RGBA", (W, H), (0, 0, 0, 0))
wd = ImageDraw.Draw(warm)
for i in range(55):
    a = int(36 * (1 - i / 55) ** 2)
    r = 220 + i * 12
    wd.ellipse([W // 2 - r, H - r // 2, W // 2 + r, H + r // 2],
               fill=(220, 90, 10, a))
warm_b = warm.filter(ImageFilter.GaussianBlur(28))
base = overlay_rgba(base, warm_b)

# Red glow behind top logo area
red_glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
rg = ImageDraw.Draw(red_glow)
for i in range(45):
    a = int(32 * (1 - i / 45) ** 2)
    r = 160 + i * 11
    rg.ellipse([W // 2 - r, 10 - r // 2, W // 2 + r, 10 + r // 2],
               fill=(200, 15, 15, a))
red_glow_b = red_glow.filter(ImageFilter.GaussianBlur(22))
base = overlay_rgba(base, red_glow_b)

# ── 3. DIAGONAL WARNING STRIPE ────────────────────────────────────────────────
stripe = Image.new("RGBA", (W, H), (0, 0, 0, 0))
strd = ImageDraw.Draw(stripe)
strd.polygon([(-60, H // 2 - 20), (W + 60, H // 2 - 230),
              (W + 60, H // 2 - 195), (-60, H // 2 + 15)],
             fill=(200, 70, 10, 40))
strd.polygon([(-60, H // 2 - 22), (W + 60, H // 2 - 232),
              (W + 60, H // 2 - 228), (-60, H // 2 - 18)],
             fill=(255, 120, 20, 90))
base = overlay_rgba(base, stripe)

# ── 4. LOGO ───────────────────────────────────────────────────────────────────
logo = Image.open(LOGO).convert("RGBA")
scale = 0.40
nw, nh = int(logo.width * scale), int(logo.height * scale)
logo = logo.resize((nw, nh), Image.LANCZOS)

shadow_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sh = Image.new("RGBA", (nw + 40, nh + 40), (0, 0, 0, 0))
sh.paste((0, 0, 0, 160), [10, 10, nw + 10, nh + 10])
sh = sh.filter(ImageFilter.GaussianBlur(14))
lx = (W - nw) // 2
ly = 34
shadow_l.paste(sh, (lx - 20, ly - 20), sh)
base = overlay_rgba(base, shadow_l)
base.paste(logo, (lx, ly), logo)
draw = ImageDraw.Draw(base)
logo_bot = ly + nh

# ── 5. FONTS ──────────────────────────────────────────────────────────────────
f_bold_xxl = font("DejaVuSans-Bold.ttf", 64)
f_bold_xl  = font("DejaVuSans-Bold.ttf", 52)
f_bold_lg  = font("DejaVuSans-Bold.ttf", 40)
f_bold_md  = font("DejaVuSans-Bold.ttf", 30)
f_bold_sm  = font("DejaVuSans-Bold.ttf", 25)
f_bold_xs  = font("DejaVuSans-Bold.ttf", 21)
f_obl_md   = font("DejaVuSans-BoldOblique.ttf", 27)
f_reg_md   = font("DejaVuSans.ttf", 26)
f_reg_sm   = font("DejaVuSans.ttf", 23)
f_reg_xs   = font("DejaVuSans.ttf", 19)

# ── 6. MONTH BADGE ────────────────────────────────────────────────────────────
badge_layer = rrect_rgba((W, H), [36, logo_bot + 10, 220, logo_bot + 52],
                         r=10, fill=(200, 15, 15, 220), outline=(255, 70, 70, 180), ow=2)
base = overlay_rgba(base, badge_layer)
draw = ImageDraw.Draw(base)
draw.text((52, logo_bot + 16), "MAY 2026", font=f_bold_xs, fill=WHITE)

# ── 7. URGENCY HOOK ───────────────────────────────────────────────────────────
hook_y = logo_bot + 18
cx(draw, hook_y, "⚠  Hurricane Season Starts June 1st  ⚠", f_obl_md, AMBER,
   shadow=True, sc=(80, 40, 0))

divider_y = hook_y + 50
draw.rectangle([70, divider_y, W - 70, divider_y + 2], fill=(200, 80, 10, 200))

# ── 8. MAIN HEADLINE ──────────────────────────────────────────────────────────
hl_y = divider_y + 18
cx(draw, hl_y,      "IS YOUR ROOF", f_bold_xxl, WHITE, shadow=True)
cx(draw, hl_y + 74, "DOCUMENTED?", f_bold_xxl, RED_BRIGHT, shadow=True, sc=(80, 0, 0))

sub_y = hl_y + 152
cx(draw, sub_y, "Before the first storm — get your aerial photos now.", f_bold_sm, OFF_WHITE)

# ── 9. WHY IT MATTERS CARD ────────────────────────────────────────────────────
card_y = sub_y + 50
card_l = rrect_rgba((W, H), [44, card_y, W - 44, card_y + 196],
                    r=18, fill=(14, 12, 22, 220), outline=(200, 70, 10, 180), ow=2)
# Top glow edge
cg = ImageDraw.Draw(card_l)
cg.rounded_rectangle([45, card_y + 1, W - 45, card_y + 4], radius=3, fill=(255, 130, 40, 70))
base = overlay_rgba(base, card_l)
draw = ImageDraw.Draw(base)

cx(draw, card_y + 14, "WHY NEIGHBORS ARE CALLING NOW", f_bold_sm, ORANGE)

points = [
    "Pre-storm photos are your BEST insurance evidence",
    "No ladder needed — fast, safe, no roof walking",
    "24-hr turnaround before the season kicks off",
    "Document now while skies are clear",
]
py = card_y + 52
for pt in points:
    # Arrow bullet
    draw.polygon([(54, py + 8), (68, py + 15), (54, py + 22)], fill=ORANGE)
    draw.text((80, py), pt, font=f_reg_sm, fill=OFF_WHITE)
    py += 38

# ── 10. CREDENTIAL BADGES ────────────────────────────────────────────────────
bdy = card_y + 212
badges = [
    ("FAA PART 107", "Certified Pilot"),
    ("FIREFIGHTER", "Owned & Operated"),
    ("ONLY $100", "Community Rate"),
]
bw, bh = 296, 80
bx0 = (W - (bw * 3 + 22)) // 2
for i, (l1, l2) in enumerate(badges):
    bx = bx0 + i * (bw + 11)
    bl = rrect_rgba((W, H), [bx, bdy, bx + bw, bdy + bh],
                   r=12, fill=(22, 10, 10, 225), outline=(200, 70, 10, 200), ow=2)
    hl = ImageDraw.Draw(bl)
    hl.rounded_rectangle([bx + 2, bdy + 2, bx + bw - 2, bdy + 5], radius=3, fill=(255, 130, 40, 55))
    base = overlay_rgba(base, bl)
    draw = ImageDraw.Draw(base)
    b1 = draw.textbbox((0, 0), l1, font=f_bold_xs)
    draw.text((bx + (bw - (b1[2]-b1[0])) // 2, bdy + 10), l1, font=f_bold_xs, fill=WHITE)
    b2 = draw.textbbox((0, 0), l2, font=f_reg_xs)
    draw.text((bx + (bw - (b2[2]-b2[0])) // 2, bdy + 44), l2, font=f_reg_xs, fill=SILVER)

# ── 11. CTA SECTION ──────────────────────────────────────────────────────────
cta_y = bdy + bh + 24
# Glowing button bar
cta_l = rrect_rgba((W, H), [80, cta_y, W - 80, cta_y + 64],
                   r=12, fill=(200, 15, 15, 100), outline=(255, 70, 50, 200), ow=2)
cb = ImageDraw.Draw(cta_l)
cb.rounded_rectangle([81, cta_y + 1, W - 81, cta_y + 5], radius=3, fill=(255, 100, 80, 60))
base = overlay_rgba(base, cta_l)
draw = ImageDraw.Draw(base)
cx(draw, cta_y + 8,  "Only $100 for neighbors — book before June 1st!", f_bold_md, WHITE, shadow=True)
cx(draw, cta_y + 44, "Same-day scheduling available · Palm Beach & Broward", f_reg_xs, SILVER)

domain_y = cta_y + 88
cx(draw, domain_y,      "redlineaerialpb.com", f_bold_lg, RED_BRIGHT, shadow=True, sc=(80, 0, 0))
cx(draw, domain_y + 52, "redlineaerialpb@gmail.com", f_reg_md, SILVER)
cx(draw, domain_y + 88, "DM me or drop a comment — happy to help a neighbor out!", f_reg_xs, GRAY)

# ── 12. FRAME ACCENTS ────────────────────────────────────────────────────────
draw.rectangle([0, 0, W, 8], fill=RED_BRIGHT)
draw.rectangle([0, H - 8, W, H], fill=RED_BRIGHT)
# Orange inner line under top bar
draw.rectangle([0, 8, W, 12], fill=(220, 90, 10, 160))

bs = 32
bw2 = 4
for (cx2, cy2, dx, dy) in [(0,8,1,1),(W-bs,8,0,1),(0,H-bs-8,-1,0),(W-bs,H-bs-8,0,0)]:
    draw.rectangle([cx2, cy2, cx2 + bs, cy2 + bw2], fill=ORANGE)
    draw.rectangle([cx2 if dx else cx2 + bs - bw2, cy2,
                    (cx2 + bw2) if dx else cx2 + bs, cy2 + bs], fill=ORANGE)

# ── 13. SAVE ─────────────────────────────────────────────────────────────────
base.save(OUT, "PNG", optimize=True)
print(f"Saved → {OUT}")
