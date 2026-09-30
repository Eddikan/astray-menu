import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

URL = "https://astray-menu.pages.dev/"
OUT = "/Users/eddy/Documents/groove-menu/"

PINK = (236, 72, 153)
PURPLE = (168, 85, 247)
BLUE = (96, 165, 250)
BLACK = (8, 8, 12)
WHITE = (255, 255, 255)

# ---------- 1) Plain high-res QR (black on white, safest for scanning/printing) ----------
qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=40, border=4)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save(OUT + "astray-qr.png")
print("plain:", img.size)

# ---------- 2) Branded table-tent poster ----------
W, H = 1200, 1600
poster = Image.new("RGB", (W, H), BLACK)
d = ImageDraw.Draw(poster)

def font(size, bold=True):
    paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def center_text(y, text, f, fill):
    bbox = d.textbbox((0, 0), text, font=f)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2, y), text, font=f, fill=fill)

# top band
d.rectangle([0, 0, W, 24], fill=PURPLE)

center_text(110, "ASTRAY", font(150), PURPLE)
center_text(280, "GODS", font(96), PINK)
center_text(410, "SCAN FOR OUR MENU", font(56), WHITE)

# QR on white rounded card
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
qr_size = 720
qr_img = qr_img.resize((qr_size, qr_size), Image.NEAREST)
card_pad = 40
card_x = (W - qr_size) // 2 - card_pad
card_y = 520
d.rounded_rectangle(
    [card_x, card_y, card_x + qr_size + 2 * card_pad, card_y + qr_size + 2 * card_pad],
    radius=40, fill=WHITE,
)
poster.paste(qr_img, (card_x + card_pad, card_y + card_pad))

center_text(1370, "Food  •  Cocktails  •  Drinks  •  Shisha", font(44), PURPLE)
center_text(1470, "TikTok   ·   @Astray.gods", font(38), BLUE)

d.rectangle([0, H - 24, W, H], fill=PURPLE)
poster.save(OUT + "astray-qr-poster.png")
print("poster:", poster.size)
