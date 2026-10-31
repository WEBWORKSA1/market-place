"""Market.Place shared layout + helpers."""
import json, os, html, datetime, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://market.place"
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year
ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
PAGES = []  # (canon, priority)

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true">'
        '<path d="M4 20 15 6h19a2 2 0 0 1 2 2v24a2 2 0 0 1-2 2H15L4 20z" fill="#0F3D2E"/>'
        '<circle cx="14.5" cy="20" r="3" fill="#FBF7F0"/>'
        '<path d="M21 14h9M21 20h9M21 26h6" stroke="#F2B33D" stroke-width="2.6" stroke-linecap="round"/>'
        '<circle cx="33" cy="30" r="3.6" fill="#E8492C"/></svg>')

NAV = [("marketplaces/index.html", "Marketplaces", "marketplaces"), ("tools/index.html", "Tools", "tools"),
       ("guides/index.html", "Guides", "guides"), ("videos.html", "Videos", "videos"),
       ("contests.html", "Contests", "contests"), ("support.html", "Support", "support"), ("advertise.html", "Advertise", "advertise")]


def esc(s):
    return html.escape(str(s), quote=True)


def hp():
    return '<div class="hp" aria-hidden="true"><label>Leave this empty<input name="_hp" tabindex="-1" autocomplete="off"></label></div>'


def status():
    return '<p class="form-status" aria-live="polite"></p>'


def ad(slot="inContent"):
    # Hidden until an ad-unit slot ID is configured in assets/js/config.js (Auto ads need nothing here).
    return f'<div class="ad-slot" data-slot="{slot}" hidden><span class="ad-label">Advertisement</span></div>'


def owner_strip():
    return ('<div class="owner-strip">Contact, if you are interested in this website / domain name / Sponsorship / '
            'Advertisement / Partnership: <a href="{pre}contact.html" data-owner rel="noopener">contact here</a></div>')


def header(pre, key):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{pre}{h}"{cur if key == k else ""}>{l}</a>' for h, l, k in NAV)
    return f"""<header class="site-head">
 <div class="wrap head-row">
  <a class="brand" href="{pre}index.html" aria-label="Market.Place home">{LOGO}<span>Market<span class="dot">.</span>Place</span></a>
  <button class="icon-btn menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn small" href="{pre}get-matched.html">Growth Desk</a>
   <button class="icon-btn" data-theme-toggle aria-label="Switch light or dark theme"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
  </nav>
 </div>
</header>"""


def footer(pre):
    return f"""<footer class="site-foot">
 <div class="wrap">
  <div class="foot-grid">
   <div>
    <a class="brand" href="{pre}index.html">{LOGO}<span>Market<span class="dot">.</span>Place</span></a>
    <p style="margin-top:14px">The independent guide to online marketplaces. Compare platforms, know your real fees, sell smarter and buy safer.</p>
    <form class="form" data-form="Newsletter signup" data-ok="You're in. The next Market Notes issue lands on Tuesday." style="margin-top:14px">
     <label for="nl-email" style="color:#fff">Market Notes: fee changes, selling tactics and scam alerts every Tuesday</label>
     {hp()}
     <input id="nl-email" type="email" name="email" placeholder="you@example.com" required autocomplete="email">
     <select name="i_am" aria-label="I mostly…"><option value="">I mostly… (optional)</option><option>Sell as a hobby / declutter</option><option>Resell / flip for profit</option><option>Run a brand or shop</option><option>Buy online</option><option>Build or run a marketplace</option></select>
     <button class="btn" type="submit">Subscribe free</button>
     {status()}
    </form>
   </div>
   <div><h4>Explore</h4><ul>
    <li><a href="{pre}marketplaces/index.html">Marketplace profiles</a></li><li><a href="{pre}marketplaces/directory.html">Directory (70+)</a></li>
    <li><a href="{pre}tools/fee-calculator.html">Fee &amp; profit calculator</a></li><li><a href="{pre}tools/marketplace-match.html">Marketplace Match quiz</a></li>
    <li><a href="{pre}tools/compare.html">Compare platforms</a></li><li><a href="{pre}guides/index.html">Guides</a></li><li><a href="{pre}videos.html">Videos</a></li></ul></div>
   <div><h4>Work with us</h4><ul>
    <li><a href="{pre}get-matched.html">Growth Desk (free consult)</a></li><li><a href="{pre}advertise.html">Advertise &amp; sponsor</a></li>
    <li><a href="{pre}contests.html">Contests &amp; prizes</a></li><li><a href="{pre}support.html">Support Market.Place</a></li>
    <li><a href="{pre}careers.html">Careers &amp; contributors</a></li></ul></div>
   <div><h4>About</h4><ul>
    <li><a href="{pre}about.html">About &amp; methodology</a></li><li><a href="{pre}contact.html">Contact</a></li>
    <li><a href="{pre}privacy.html">Privacy &amp; cookies</a></li><li><a href="{pre}terms.html">Terms of use</a></li>
    <li><a href="{pre}disclaimer.html">Disclaimer</a></li><li><a href="{pre}trademark.html">Trademark &amp; copyright</a></li>
    <li><a href="{pre}sitemap.html">Site map</a></li></ul></div>
  </div>
  <div class="foot-legal">
   <p>© <span data-year>{YEAR}</span> Market.Place. All original articles, calculators, scores, data compilations and designs on this site are protected by copyright.</p>
   <p>Independence &amp; trademark notice: Market.Place is an independent publication. It is not affiliated with, endorsed by or sponsored by any online marketplace or by any company that uses "Marketplace" or a similar name in its products or services (including Facebook Marketplace, Amazon Marketplace or Walmart Marketplace). Platform names are used only to identify the services we review. All trademarks belong to their respective owners. <a href="{pre}trademark.html">Full disclosure</a>.</p>
   <p>Fee figures are compiled from each platform's official pages on the date shown and can change without notice. Always confirm on the platform before you list. Ads on this site are served by Google AdSense.</p>
  </div>
 </div>
</footer>
<div class="consent" id="consent" hidden role="dialog" aria-label="Cookie notice">
 <p>We use cookies to run this site and, through Google AdSense, to show ads. Accept personalized ads, or keep essential cookies only and see non-personalized ads. See our <a href="{pre}privacy.html">privacy policy</a>.</p>
 <div class="acts"><button class="btn small" data-consent="all">Accept all</button><button class="btn small alt" data-consent="essential">Essential only</button></div>
</div>"""


def page(path, title, desc, body, nav_key=None, jsonld=None, scripts="", extra_head="", priority="0.7", og_type="website", dynbase=False):
    depth = path.count("/")
    pre = "../" * depth
    canon = BASE_URL + "/" + (path[:-10] if path.endswith("index.html") else path)
    full_title = title if "Market.Place" in title else f"{title} | Market.Place"
    lds = jsonld if isinstance(jsonld, list) else ([jsonld] if jsonld else [])
    ld = "\n".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False, indent=1) + "</script>" for x in lds)
    body = body.replace("{pre}", pre)
    basetag = ("<script>document.write('<base href=\"'+(location.pathname.indexOf('/market-place/')===0?'/market-place/':'/')+'\">')</script>\n") if dynbase else ""
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{basetag}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Market.Place">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE_URL}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F3D2E">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<script>try{{var t=localStorage.getItem("mp-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{pre}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,500..800,50;1,9..144,500..700,50&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
{ADS}
{ld}
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{owner_strip().replace("{pre}", pre)}
{header(pre, nav_key)}
<main id="main">
{body.strip()}
</main>
{footer(pre)}
<script src="{pre}assets/js/config.js"></script>
<script src="{pre}assets/js/main.js"></script>
{scripts.replace("{pre}", pre)}
</body>
</html>
"""
    dest = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(shortlines(doc))
    if path not in ("404.html", "thank-you.html"):
        PAGES.append((canon, priority))


def crumbs(items):
    """items: list of (label, href or None). Returns html + JSON-LD dict."""
    parts, ld = [], []
    for i, (label, href) in enumerate(items):
        parts.append(f'<a href="{href}">{esc(label)}</a>' if href else f'<span aria-current="page">{esc(label)}</span>')
        url = BASE_URL + "/" + href.replace("{pre}", "").replace("index.html", "") if href else None
        e = {"@type": "ListItem", "position": i + 1, "name": label}
        if url:
            e["item"] = url
        ld.append(e)
    return ('<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>",
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld})


def read_front(path):
    import yaml
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        return {}, raw
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        # tolerant fallback for flat "key: value" front matter containing colons
        fm = {}
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith((" ", "-")):
                k, v = line.split(":", 1)
                v = v.strip().strip('"')
                fm[k.strip()] = int(v) if re.fullmatch(r"\d+", v) else v
        return fm, m.group(2)


def md(text):
    import markdown
    return markdown.markdown(text, extensions=["tables", "toc", "sane_lists", "attr_list"])


def wrap_tables(h):
    return re.sub(r"(<table>.*?</table>)", r'<div class="table-scroll">\1</div>', h, flags=re.S)


def growth_cta(pre="{pre}", title="Want a second opinion on where to sell?", text="Tell the Growth Desk what you sell. We reply with a free, no-obligation channel plan: which marketplaces to use, what to fix in your listings, and what to expect."):
    return f"""<aside class="tag-card hole" style="background:var(--saffron-soft);border-color:transparent">
 <span class="kicker">Free Growth Desk</span>
 <h3>{title}</h3>
 <p style="margin-bottom:14px">{text}</p>
 <a class="btn small" href="{pre}get-matched.html">Get my free plan</a>
</aside>"""


def shortlines(doc, limit=240):
    """Keep source lines short (between-tag breaks only) so files stay diff- and transfer-friendly."""
    out = []
    for line in doc.split("\n"):
        while len(line) > limit:
            i = line.find("><", limit // 2)
            if i == -1:
                break
            out.append(line[:i + 1]); line = line[i + 1:]
        out.append(line)
    return "\n".join(out)
