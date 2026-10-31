# Market.Place

The independent guide to online marketplaces: compare platforms, calculate true selling fees, sell smarter and buy safer.

This is a static site (plain HTML/CSS/JS) served by GitHub Pages from the `main` branch root. There is no server code.

## What's inside

- **Tools** (`/tools/`)
  - Fee & profit calculator: 16 platforms, editable rates, a reverse price finder and a compare-all table
  - Marketplace Match quiz
  - Compare tool
  - Flip ROI calculator
  - Scam red-flag checker
- **Marketplaces** (`/marketplaces/`): 16 in-depth platform profiles and a filterable directory of 100+ marketplaces
- **Guides** (`/guides/`): 12 long-form guides with FAQ schema
- **Videos** (`/videos.html`): curated YouTube library using lite, click-to-load embeds
- **Money pages**
  - Growth Desk lead funnel (`get-matched.html`)
  - Support/donations (`support.html`)
  - Contests (`contests.html`)
  - Careers (`careers.html`)
  - Advertise (`advertise.html`)
- **Compliance**
  - Privacy, terms, disclaimer, and trademark & copyright pages
  - Cookie notice
  - `ads.txt`, `robots.txt`, `sitemap.xml`, a web manifest and a 404 page

## Editing

Pages are generated. Edit the sources in `_build/`, then rebuild:

```bash
pip install markdown pyyaml
python3 _build/build.py
```

- Guides: `_build/content/guides/*.md`
- Platform profiles: `_build/content/marketplaces/*.md`
- Fee rules for the calculators: `_build/content/fees.json`. Each rule has a `pct`, a `fixed` amount, a `base` of `item` or `item_shipping`, and optional `min_price`/`max_price`.
- Directory: `_build/research/directory.json`
- Videos: `_build/research/videos.json`
- Quiz fit matrix: `_build/platforms.py`
- Competitive research: `_build/research/RESEARCH.md`
- Build prompt and business model: `PROMPTS.md`

## Configuration (`assets/js/config.js`)

- `payments`: paste PayPal, Stripe Payment Link or Buy Me a Coffee URLs to switch the Support page from pledge mode to instant checkout.
- `adSlots`: optional AdSense ad-unit slot IDs for the in-content units. Auto ads work without them.
- `_k` / `_o`: encoded contact keys. Keep them encoded. Never put a plain contact address or owner URL in any page.

## Forms

All forms post to a form-relay service. The first submission triggers a one-time activation email to the site inbox, and you must confirm it before messages are delivered.

## Publishing

1. Go to **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, and select `main` / `(root)`.
2. For the custom domain:
   - Set apex A records to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and point `www` with a CNAME to the GitHub Pages host.
   - Add a `CNAME` file containing `market.place`.
   - Enable **Enforce HTTPS**.

## Trademark

"Market.Place" is the name of this independent publication. It is not affiliated with any company that uses "Marketplace" in its name. All platform names are trademarks of their respective owners. See `trademark.html`.
