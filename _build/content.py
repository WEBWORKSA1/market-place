"""Guides, platform profiles, directory, videos, data.js."""
import os, json, re, glob
from mp import page, crumbs, esc, ad, growth_cta, read_front, md, wrap_tables, BASE_URL, TODAY, ROOT
from platforms import FIT, ORDER

C = os.path.join(ROOT, "_build", "content")
R = os.path.join(ROOT, "_build", "research")


def load_guides():
    out = []
    for f in sorted(glob.glob(os.path.join(C, "guides", "*.md"))):
        fm, body = read_front(f)
        if not fm.get("title"):
            continue
        fm["slug"] = fm.get("slug") or os.path.basename(f)[:-3]
        fm["body"] = body
        out.append(fm)
    order = ["sell-online-beginners", "choose-the-right-marketplace", "pricing-strategy", "write-listings-that-sell", "product-photos", "shipping-101",
             "avoid-buyer-scams", "avoid-seller-scams", "safe-local-meetups", "reselling-business", "seller-taxes-records", "launch-your-own-marketplace"]
    out.sort(key=lambda g: order.index(g["slug"]) if g["slug"] in order else 99)
    return out


def load_profiles():
    out = []
    for slug in ORDER:
        f = os.path.join(C, "marketplaces", slug + ".md")
        if not os.path.exists(f):
            continue
        fm, body = read_front(f)
        fm["slug"] = slug
        fm["body"] = body
        regs = fm.get("regions", "")
        fm["regions_list"] = [r.strip() for r in (regs if isinstance(regs, list) else re.split(r"[,/;]| and ", str(regs))) if r.strip()]
        out.append(fm)
    return out


def norm_regions(lst):
    """Map free-text regions to the quiz's region keys."""
    keys = set()
    for r in lst:
        l = r.lower()
        if "global" in l or "worldwide" in l or "international" in l:
            keys.add("Global")
        if "us" == l or "united states" in l or "u.s" in l or l.startswith("us"):
            keys.add("US")
        if "canada" in l or l == "ca":
            keys.add("Canada")
        if "uk" in l or "united kingdom" in l or "britain" in l:
            keys.add("UK")
        if "europe" in l or "eu" == l or "eu " in l:
            keys.add("Europe")
        if "north america" in l:
            keys.update(["US", "Canada"])
    return sorted(keys)


def load_json(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def write_data_js(profiles, fees, directory):
    fee_by = {f["slug"]: f for f in fees}
    plats = []
    for p in profiles:
        s = p["slug"]
        plats.append({"slug": s, "name": p["name"], "url": p.get("url", ""), "category": p.get("category", ""), "best_for": p.get("best_for", ""),
                      "fee_summary": p.get("fee_summary", ""), "regions": norm_regions(p["regions_list"]),
                      "scores": {"reach": p.get("score_reach", 5), "fees": p.get("score_fees", 5), "ease": p.get("score_ease", 5), "protection": p.get("score_protection", 5)},
                      "fit": FIT.get(s), "fees": fee_by.get(s)})
    js = "window.MP_DATA=" + json.dumps({"platforms": plats}, ensure_ascii=False, indent=1) + ";\n"
    open(os.path.join(ROOT, "assets/js/data.js"), "w", encoding="utf-8").write(js)
    dj = "window.MP_DIR=" + json.dumps(directory, ensure_ascii=False, indent=1) + ";\n"
    open(os.path.join(ROOT, "assets/js/directory.js"), "w", encoding="utf-8").write(dj)


def toc_and_ads(h):
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', h)
    toc = "".join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in heads)
    # in-content ad slot after the 3rd h2 (hidden until slot id configured)
    parts = re.split(r'(?=<h2 id=)', h)
    if len(parts) > 4:
        parts.insert(4, ad())
    return "".join(parts), toc


def build_guides(guides):
    cats = ["Selling", "Buying", "Safety", "Business"]
    for i, g in enumerate(guides):
        h, toc = toc_and_ads(wrap_tables(md(g["body"])))
        h = h.replace("<h2 id=\"key-takeaways\">", "<div class=\"takeaways\"><h2 id=\"key-takeaways\">", 1)
        if "<div class=\"takeaways\">" in h:
            h = re.sub(r'(<div class="takeaways"><h2 id="key-takeaways">.*?</ul>)', r"\1</div>", h, count=1, flags=re.S)
        faq = g.get("faq") or []
        faq_html = "".join(f"<details><summary>{esc(q['q'])}</summary><p>{esc(q['a'])}</p></details>" for q in faq if q.get("q"))
        related = [x for x in guides if x["slug"] != g["slug"] and x.get("category") == g.get("category")][:2] + \
                  [x for x in guides if x["slug"] != g["slug"] and x.get("category") != g.get("category")][:3]
        rel = "".join(f'<a class="tag-card hole" href="{x["slug"]}.html"><span class="pill saffron">{esc(x.get("category",""))}</span><h3 style="margin-top:6px;font-size:1.08rem">{esc(x["title"])}</h3></a>' for x in related[:3])
        c, bld = crumbs([("Home", "{pre}index.html"), ("Guides", "{pre}guides/index.html"), (g["title"], None)])
        lead = growth_cta(title="Launching a marketplace?", text="Get a free scoping plan: niche, take rate, stack and a 90-day launch roadmap.") if g["slug"] == "launch-your-own-marketplace" else growth_cta()
        body = f"""<section class="article-head"><div class="wrap">{c}<span class="pill saffron">{esc(g.get('category',''))}</span><h1 style="max-width:900px;font-size:clamp(2rem,4.4vw,3.2rem)">{esc(g['title'])}</h1>
<p class="lede" style="max-width:760px;font-size:1.12rem;color:var(--ink-2)">{esc(g.get('description',''))}</p>
<div class="meta-row"><span>By the Market.Place editors</span><span>·</span><span>{g.get('read_minutes','')} min read</span><span>·</span><span>Updated {TODAY}</span></div></div></section>
<section class="tight" style="padding-top:0"><div class="wrap layout-side"><article class="prose">{h}
{"<h2 id='faq'>Frequently asked questions</h2><div class='faq'>" + faq_html + "</div>" if faq_html else ""}
<p class="small muted" style="margin-top:30px">This guide is general information, not legal, tax or financial advice. Platform rules and fees change, so check the platform's own help pages before you act.</p>
</article>
<aside class="sidebar"><nav class="tag-card toc" aria-label="On this page"><h4>On this page</h4><ol>{toc}</ol></nav>{lead}
<div class="tag-card"><h3>Run your numbers</h3><p style="margin-bottom:12px">See fees and profit on 16 platforms at once.</p><a class="btn small green" href="../tools/fee-calculator.html">Fee calculator</a></div></aside></div></section>
<section class="band tight"><div class="wrap"><h2>Keep reading</h2><div class="grid g3">{rel}</div></div></section>"""
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g.get("description", ""),
               "datePublished": TODAY, "dateModified": TODAY, "author": {"@type": "Organization", "name": "Market.Place editors"},
               "publisher": {"@type": "Organization", "name": "Market.Place", "logo": {"@type": "ImageObject", "url": BASE_URL + "/assets/img/favicon.svg"}},
               "mainEntityOfPage": f"{BASE_URL}/guides/{g['slug']}.html"}
        lds = [bld, art]
        if faq:
            lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in faq if q.get("q")]})
        page(f"guides/{g['slug']}.html", g["title"], g.get("description", ""), body, nav_key="guides", jsonld=lds, priority="0.8", og_type="article")
    # index
    blocks = ""
    for cat in cats:
        items = [g for g in guides if g.get("category") == cat]
        if not items:
            continue
        cards = "".join(f'<a class="tag-card hole" href="{g["slug"]}.html"><span class="pill">{g.get("read_minutes","")} min read</span><h3 style="margin-top:6px">{esc(g["title"])}</h3><p>{esc(g.get("description",""))}</p></a>' for g in items)
        blocks += f'<section class="tight"><div class="wrap"><h2>{cat}</h2><div class="grid g3">{cards}</div></div></section>'
    c, ld = crumbs([("Home", "{pre}index.html"), ("Guides", None)])
    page("guides/index.html", "Guides for online sellers and buyers", "In-depth, practical guides to selling online, pricing, photos, listings, shipping, avoiding scams, reselling, records and launching a marketplace.",
         f'<section class="page-hero"><div class="wrap">{c}<span class="kicker">Guides</span><h1>Practical guides for selling and buying online</h1><p class="lede">Long-form, hands-on and checked against official sources. Start with the basics or jump to what\'s costing you sales.</p></div></section>{blocks}{ad()}<section class="tight"><div class="wrap">{growth_cta()}</div></section>',
         nav_key="guides", jsonld=ld, priority="0.9")


def score_rows(p):
    rows = [("Buyer reach", p.get("score_reach", 0)), ("Low fees", p.get("score_fees", 0)), ("Ease", p.get("score_ease", 0)), ("Protection", p.get("score_protection", 0))]
    return "".join(f'<div class="score-row"><span>{l}</span><div class="bar"><i style="width:{int(v)*10}%"></i></div><b>{v}</b></div>' for l, v in rows)


def build_profiles(profiles, fees):
    fee_by = {f["slug"]: f for f in fees}
    for p in profiles:
        h, toc = toc_and_ads(wrap_tables(md(p["body"])))
        f = fee_by.get(p["slug"], {})
        others = [x for x in profiles if x["slug"] != p["slug"]]
        same = [x for x in others if x.get("category") == p.get("category")]
        alts = (same + [x for x in others if x not in same])[:3]
        alt_html = "".join(f'<a class="tag-card hole" href="{x["slug"]}.html"><span class="pill">{esc(x.get("category",""))}</span><h3 style="margin-top:6px;font-size:1.1rem">{esc(x["name"])}</h3><p class="small">{esc(x.get("fee_summary",""))}</p></a>' for x in alts)
        cmp_links = "".join(f'<a class="btn small alt" href="../tools/compare.html?p={p["slug"]},{x["slug"]}">{esc(p["name"])} vs {esc(x["name"])}</a>' for x in alts)
        c, bld = crumbs([("Home", "{pre}index.html"), ("Marketplaces", "{pre}marketplaces/index.html"), (p["name"], None)])
        body = f"""<section class="article-head"><div class="wrap">{c}<span class="pill">{esc(p.get('category',''))}</span><span class="pill saffron">{esc(p.get('regions',''))}</span>
<h1 style="font-size:clamp(2rem,4.6vw,3.3rem)">{esc(p['name'])}: fees, pros, cons &amp; selling tips</h1>
<p class="lede" style="max-width:760px;font-size:1.15rem;color:var(--ink-2)">{esc(p.get('tagline',''))}</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap layout-side"><article class="prose">{h}
<p class="small muted" style="margin-top:28px">Market.Place is independent and not affiliated with {esc(p['name'])}. Fees verified {esc(f.get('verified',''))} from the <a href="{esc(f.get('source', p.get('url','')))}" target="_blank" rel="noopener nofollow">official fee page</a>. Confirm current fees there before you list.</p></article>
<aside class="sidebar">
 <div class="tag-card hole"><h4>Market.Place scores</h4>{score_rows(p)}<p class="small muted" style="margin:10px 0 0">Editorial ratings out of 10. <a href="../about.html#methodology">How we score</a></p></div>
 <div class="tag-card"><h4>Quick facts</h4><p class="small" style="margin:0 0 6px"><strong>Best for:</strong> {esc(p.get('best_for',''))}</p><p class="small" style="margin:0 0 6px"><strong>Seller fees:</strong> {esc(p.get('fee_summary',''))}</p><p class="small" style="margin:0 0 12px"><strong>Regions:</strong> {esc(p.get('regions',''))}</p>
 <a class="btn small green" href="../tools/fee-calculator.html?p={p['slug']}">Calculate {esc(p['name'])} fees</a> <a class="btn small alt" style="margin-top:8px" href="{esc(p.get('url',''))}" target="_blank" rel="noopener nofollow">Official site ↗</a></div>
 <nav class="tag-card toc" aria-label="On this page"><h4>On this page</h4><ol>{toc}</ol></nav>
 {growth_cta(title=f"Thinking of selling on {esc(p['name'])}?", text="Get a free channel plan from the Growth Desk: whether it fits your products, how to price, and what to cross-list.")}
</aside></div></section>
<section class="band tight"><div class="wrap"><h2>Alternatives to {esc(p['name'])}</h2><div class="grid g3">{alt_html}</div><div class="ticker" style="margin-top:18px">{cmp_links}</div></div></section>"""
        rev = {"@context": "https://schema.org", "@type": "Review", "itemReviewed": {"@type": "Organization", "name": p["name"], "url": p.get("url", "")},
               "author": {"@type": "Organization", "name": "Market.Place"}, "datePublished": TODAY,
               "reviewRating": {"@type": "Rating", "ratingValue": round((p.get("score_reach", 5) + p.get("score_fees", 5) + p.get("score_ease", 5) + p.get("score_protection", 5)) / 4, 1), "bestRating": 10, "worstRating": 1},
               "reviewBody": p.get("tagline", "")}
        page(f"marketplaces/{p['slug']}.html", f"{p['name']} for sellers: fees, pros & cons", f"Independent {p['name']} review for sellers: current fees with a worked example, strengths, watch-outs, buyer protection and tips to sell more.",
             body, nav_key="marketplaces", jsonld=[bld, rev], priority="0.8", og_type="article")
    # index
    cards = "".join(f'<a class="tag-card hole dir-card" href="{p["slug"]}.html"><span class="pill">{esc(p.get("category",""))}</span><h3 style="margin-top:6px">{esc(p["name"])}</h3><p>{esc(p.get("tagline",""))}</p>{score_rows(p)}<p class="fee"><strong>Fees:</strong> {esc(p.get("fee_summary",""))}</p></a>' for p in profiles)
    c, ld = crumbs([("Home", "{pre}index.html"), ("Marketplaces", None)])
    page("marketplaces/index.html", "Online marketplace profiles & reviews for sellers", "Independent profiles of eBay, Etsy, Amazon, Facebook Marketplace, Poshmark, Mercari, Depop, Vinted, Kijiji, Reverb, Whatnot, StockX and more.",
         f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Platform profiles</span><h1>Marketplace profiles, written for sellers</h1>
<p class="lede">What each platform costs, who buys there, what it does well, what to watch out for, and how to sell more. Want the long list? Browse the <a href="directory.html">directory</a>.</p>
<div class="ticker"><a class="btn small" href="../tools/marketplace-match.html">Find my best match</a><a class="btn small alt" href="../tools/compare.html">Compare side by side</a><a class="btn small alt" href="directory.html">Directory</a></div></div></section>
<section class="tight" style="padding-top:0"><div class="wrap"><div class="grid g4">{cards}</div></div></section>{ad()}""",
         nav_key="marketplaces", jsonld=ld, priority="0.9")


def build_directory(directory, profiles):
    c, ld = crumbs([("Home", "{pre}index.html"), ("Marketplaces", "{pre}marketplaces/index.html"), ("Directory", None)])
    noscript = "".join(f'<li><a href="{esc(d["url"])}" rel="noopener nofollow">{esc(d["name"])}</a>: {esc(d["category"])}. {esc(d["best_for"])}</li>' for d in directory)
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Directory</span><h1>The online marketplace directory</h1>
<p class="lede">{len(directory)} marketplaces worth knowing, from global giants to niche specialists, filtered by what you sell, where you are and how they work. Platforms with a full Market.Place profile are linked.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap" id="dir">
<div class="filters"><div><label class="lbl" for="dir-q">Search</label><input id="dir-q" type="search" placeholder="Name, product or keyword"></div>
<div><label class="lbl" for="dir-cat">Category</label><select id="dir-cat"><option value="">All categories</option></select></div>
<div><label class="lbl" for="dir-reg">Region</label><select id="dir-reg"><option value="">All regions</option></select></div>
<div><label class="lbl" for="dir-model">Model</label><select id="dir-model"><option value="">All models</option></select></div></div>
<p><span class="count" id="dir-count">{len(directory)}</span> marketplaces · <button type="button" class="btn small alt" id="dir-clear">Clear filters</button></p>
<div class="grid g3" id="dir-grid"><noscript><ul>{noscript}</ul></noscript></div>
<p class="small muted" style="margin-top:20px">Fee summaries come from official platform pages where we could verify them. Otherwise we say "See official fee page". Listing here is editorial and free. Sponsored placements, if any, are always labelled. Missing a marketplace? <a href="../contact.html?topic=General%20question">Suggest one</a>.</p>
</div></section>{ad()}<section class="tight"><div class="wrap">{growth_cta()}</div></section>"""
    page("marketplaces/directory.html", f"Online marketplace directory ({len(directory)} platforms)", f"Directory of {len(directory)} online marketplaces by category, region and selling model, with seller fee summaries and who each one suits best.",
         body, nav_key="marketplaces", jsonld=ld, priority="0.8",
         scripts='<script src="{pre}assets/js/data.js"></script><script src="{pre}assets/js/directory.js"></script><script src="{pre}assets/js/tools.js"></script>')


def build_videos(videos):
    topics = []
    for v in videos:
        if v.get("topic") not in topics:
            topics.append(v.get("topic"))
    blocks = ""
    for t in topics:
        cards = "".join(f'<article class="vid-card"><button class="yt" data-yt="{esc(v["id"])}" aria-label="Play: {esc(v["title"])}"><span class="play"></span></button><h3>{esc(v["title"])}</h3><p class="small muted" style="margin:0 0 4px">{esc(v["channel"])}</p><p class="small">{esc(v.get("why",""))}</p></article>' for v in videos if v.get("topic") == t)
        blocks += f'<section class="tight"><div class="wrap"><h2>{esc(t)}</h2><div class="grid g3">{cards}</div></div></section>'
    c, ld = crumbs([("Home", "{pre}index.html"), ("Videos", None)])
    vids_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"https://www.youtube.com/watch?v={v['id']}", "name": v["title"]} for i, v in enumerate(videos)]}
    page("videos.html", "Video library for online sellers", "Handpicked videos on selling online, product photography, shipping, avoiding marketplace scams, pricing and building an e-commerce business.",
         f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Video library</span><h1>Learn to sell online, one video at a time</h1>
<p class="lede">We watched dozens of tutorials and kept the ones that are clear, current and actually useful, many from the platforms themselves and from consumer-protection agencies. Videos load only when you press play.</p></div></section>
{blocks}{ad()}
<section class="tight"><div class="wrap cta-band"><div><h2>Make videos with us</h2><p>We commission short tutorials on our tools and guides. If you create seller content, we'd like to hear from you.</p></div><div><a class="btn" href="careers.html">See creator roles</a></div></div></section>""",
         nav_key="videos", jsonld=[ld, vids_ld], priority="0.7")
