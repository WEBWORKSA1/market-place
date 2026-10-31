#!/usr/bin/env python3
"""Market.Place static site generator.
Run from the repo root:  python3 _build/build.py
Writes plain HTML to the repo root so GitHub Pages (free plan, main branch) serves it as-is."""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp
from mp import ROOT, BASE_URL, TODAY, PAGES, LOGO
import content, pages_core, pages_tools, pages_money


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def static_files():
    w = lambda p, s: open(os.path.join(ROOT, p), "w", encoding="utf-8").write(s)
    os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
    w("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" ' + LOGO[5:].replace(' aria-hidden="true"', ''))
    w("assets/img/og.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#FBF7F0"/><rect x="0" y="0" width="1200" height="14" fill="#0F3D2E"/>
<g transform="translate(90 170) scale(5)">{LOGO[LOGO.index('>')+1:-6]}</g>
<text x="330" y="290" font-family="Georgia,serif" font-size="110" font-weight="700" fill="#13241D">Market<tspan fill="#E8492C">.</tspan>Place</text>
<text x="334" y="370" font-family="Arial,sans-serif" font-size="38" fill="#3B4A43">Compare marketplaces. Know your real fees.</text>
<text x="334" y="425" font-family="Arial,sans-serif" font-size="38" fill="#3B4A43">Sell smarter, buy safer.</text></svg>''')
    w("site.webmanifest", json.dumps({"name": "Market.Place", "short_name": "Market.Place", "start_url": "./index.html", "display": "standalone",
                                      "background_color": "#FBF7F0", "theme_color": "#0F3D2E", "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))
    w("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    w("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {BASE_URL}/sitemap.xml\n")
    w(".nojekyll", "\n")


def sitemap_xml():
    seen, rows = set(), []
    for u, pr in PAGES:
        if u in seen:
            continue
        seen.add(u)
        rows.append(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")


def main():
    guides = content.load_guides()
    profiles = content.load_profiles()
    fees = content.load_json(os.path.join(content.C, "fees.json"), [])
    directory = content.load_json(os.path.join(content.R, "directory.json"), [])
    videos = content.load_json(os.path.join(content.R, "videos.json"), [])
    # link directory entries to our profiles
    by_name = {p["name"].lower(): p["slug"] for p in profiles}
    alias = {"facebook marketplace": "facebook-marketplace", "facebook": "facebook-marketplace", "walmart": "walmart-marketplace", "walmart marketplace": "walmart-marketplace",
             "tiktok shop": "tiktok-shop", "amazon": "amazon", "ebay": "ebay"}
    for d in directory:
        n = d["name"].lower()
        d["slug"] = by_name.get(n) or alias.get(n) or ""
        if d["slug"] and d["slug"] not in {p["slug"] for p in profiles}:
            d["slug"] = ""
    directory.sort(key=lambda d: (0 if d["slug"] else 1, d["name"].lower()))
    static_files()
    content.write_data_js(profiles, fees, directory)
    ctx = {"profiles": profiles, "guides": guides, "videos": videos, "dir_count": len(directory)}
    pages_core.build_core(ctx)
    pages_tools.build_tools()
    pages_money.build_money()
    content.build_guides(guides)
    content.build_profiles(profiles, fees)
    content.build_directory(directory, profiles)
    content.build_videos(videos)
    pages_core.build_sitemap_page(ctx)
    sitemap_xml()
    print(f"Built {len(PAGES)} pages · {len(profiles)} profiles · {len(guides)} guides · {len(directory)} directory · {len(videos)} videos · {len(fees)} fee sets")


if __name__ == "__main__":
    main()
