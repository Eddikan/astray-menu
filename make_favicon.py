from PIL import Image, ImageDraw, ImageFont

OUT = "/Users/eddy/Documents/groove-menu/"
BLACK = (8, 8, 12)
ACCENT = (168, 85, 247)  # Astray neon purple

def font(size):
    for p in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "/System/Library/Fonts/Helvetica.ttc"]:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def make(size, radius_ratio=0.24):
    # render at 4x then downscale for smooth edges
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(s * radius_ratio)
    d.rounded_rectangle([0, 0, s, s], radius=r, fill=BLACK)
    f = font(int(s * 0.46))
    txt = "AG"
    bbox = d.textbbox((0, 0), txt, font=f)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((s - w) / 2 - bbox[0], (s - h) / 2 - bbox[1]), txt, font=f, fill=ACCENT)
    return img.resize((size, size), Image.LANCZOS)

# Standard favicon PNGs
make(32).save(OUT + "favicon-32.png")
make(180).save(OUT + "apple-touch-icon.png")      # iOS home screen
make(512).save(OUT + "icon-512.png")              # Android / PWA

# Multi-size .ico
ico = make(64)
ico.save(OUT + "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("favicons written")
