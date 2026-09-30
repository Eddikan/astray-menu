# Astray Gods — Menu

Static digital menu for **Astray Gods**, deployed on Cloudflare Pages.

## Files
- `index.html` — the menu (single self-contained page)
- `astray-logo.jpg` — brand logo used in the header
- `favicon.*`, `apple-touch-icon.png`, `icon-512.png` — site icons
- `astray-qr.png` — plain scannable QR (points to the live site)
- `astray-qr-poster.png` — printable table-tent poster with the QR
- `make_favicon.py`, `make_qr.py` — regenerate the icons / QR assets

## Deploy (Cloudflare Pages)
This repo auto-deploys on every push to `main`. No build step — it's a static
site whose output directory is the repo root.

## Update the menu
Edit `index.html`, commit, and push. Cloudflare rebuilds automatically.
If the live URL changes, update `URL` in `make_qr.py` and re-run it to
regenerate the QR assets:

```bash
python3 make_qr.py
```
