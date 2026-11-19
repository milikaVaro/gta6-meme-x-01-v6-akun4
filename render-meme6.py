#!/usr/bin/env python3
"""Render meme #6 untuk gta6-meme-x-01 (akun 4): CV/resume "Professional Waiter".
Teks tajam via PIL (bukan AI image) supaya terbaca di 480px.
Output: meme6.png (1080x1080). Logo hantu dari press kit resmi make.fun.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
ASSETS = os.path.expanduser('~/workspace/makefun/meme-x-assets')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme6.png')

PAPER = (251, 250, 247)
INK = (26, 24, 40)
MUTED = (110, 104, 122)
MAGENTA = (214, 51, 132)
WHITE = (255, 255, 255)
LINE = (200, 190, 180)
CARD = (240, 236, 230)


def font(name, size):
    paths = [
        f'/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf',
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)

MX = 64  # margin x

# --- header: ghost + make.fun + resume ---
ghost = Image.open(os.path.join(ASSETS, 'mark-1024.png')).convert('RGBA')
ghost = ghost.resize((88, 88), Image.LANCZOS)
img.paste(ghost, (MX, 48), ghost)
d.text((MX + 108, 54), 'make.fun', font=font('Bold', 38), fill=INK)
d.text((MX + 108, 102), 'RESUME', font=font('Regular', 22), fill=MUTED)
d.text((W - MX, 58), 'EST. 2013', font=font('Bold', 28), fill=INK, anchor='ra')
d.text((W - MX, 98), '13 YRS EXP.', font=font('Regular', 22), fill=MUTED, anchor='ra')

d.line([(MX, 172), (W - MX, 172)], fill=LINE, width=2)

# --- name + title ---
d.text((MX, 196), 'ME', font=font('Black', 88), fill=INK)
d.text((MX, 296), 'PROFESSIONAL WAITER — 13 YEARS OF EXPERIENCE',
       font=font('Bold', 25), fill=MUTED)

# --- experience card ---
d.text((MX, 356), 'EXPERIENCE', font=font('Bold', 26), fill=MUTED)
ey0, ey1 = 396, 544
d.rounded_rectangle([(MX, ey0), (W - MX, ey1)], radius=18, fill=CARD)
d.text((MX + 28, ey0 + 16), 'Professional GTA VI Waiter', font=font('Black', 36), fill=INK)
d.text((MX + 28, ey0 + 64), '2013 - Present  |  Leonida (in my dreams)',
       font=font('Regular', 26), fill=MUTED)
d.text((MX + 28, ey0 + 102), '13 years. 0 releases. Still here.',
       font=font('Bold', 28), fill=INK)

# --- skills ---
d.text((MX, 580), 'SKILLS', font=font('Bold', 26), fill=MUTED)
skills = [
    ('Checking release dates', 'Expert'),
    ('Patience', 'Depleted'),
    ('Dreaming in Vice City', 'Fluent'),
]
y = 620
for name, level in skills:
    d.text((MX + 8, y), '-', font=font('Bold', 32), fill=MAGENTA)
    d.text((MX + 44, y), name, font=font('Regular', 32), fill=INK)
    d.text((W - MX - 8, y), level, font=font('Bold', 32), fill=MAGENTA, anchor='ra')
    y += 46

# --- education ---
d.text((MX, 786), 'EDUCATION', font=font('Bold', 26), fill=MUTED)
d.text((MX, 822), 'School of Waiting, Class of 2013-2026', font=font('Regular', 30), fill=INK)

# --- punchline bar ---
bar_y0, bar_y1 = 900, 1004
d.rounded_rectangle([(MX, bar_y0), (W - MX, bar_y1)], radius=22, fill=MAGENTA)
d.text((W // 2, bar_y0 + 14), 'CURRENT ROLE: MY AGENT EARNS', font=font('Bold', 30), fill=WHITE, anchor='ma')
d.text((W // 2, bar_y0 + 56), 'REAL MONEY ON make.fun.', font=font('Bold', 28), fill=WHITE, anchor='ma')

img.save(OUT, 'PNG')
print('saved', OUT, img.size, os.path.getsize(OUT), 'bytes')
