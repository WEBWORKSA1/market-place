# Market.Place: idea, business model and phase-wise build prompt

## 1. The idea (chosen position)

**Market.Place = "Compare every online marketplace, calculate your true fees, sell smarter and buy safer."**

An independent, platform-neutral marketplace intelligence hub:

- **Traffic engine:** free fee and profit calculators, a "which marketplace should I sell on" match quiz, side-by-side platform comparisons, a filterable directory of 70+ marketplaces, and anti-scam guides.
- **Money engine:** Google AdSense on high-intent e-commerce traffic, plus the **Growth Desk**, a lead-generation funnel for sellers, brands and founders who want help choosing channels, growing sales or launching their own marketplace.

### Why this beats the alternatives

| Option for Market.Place | Traffic ceiling | Monetization depth | Feasible on free static hosting | Moat | Verdict |
|---|---|---|---|---|---|
| Build an actual two-sided classifieds marketplace | High *if* it reaches liquidity | High | No: needs a database, payments, moderation and trust and safety staff | Weak against Facebook, Craigslist, Kijiji and OLX | Reject for now. It becomes the Phase 5 option once traffic exists |
| Generic e-commerce news blog | Mid | Low to mid | Yes | None | Reject |
| Coupons and deals site | High | Affiliate only, thin content | Yes | None, and a frequent cause of AdSense "low value content" rejections | Reject |
| **Independent marketplace guide + calculators + Growth Desk leads** | **High: "etsy fee calculator", "ebay vs mercari", "is this a scam" are evergreen, high-volume searches** | **High: AdSense on seller-tool, shipping and SaaS CPCs + B2B leads + sponsors** | **Yes, 100% static** | **Owned calculators, owned comparison data, owned scoring** | **Chosen** |

The domain itself says "the place to understand marketplaces". Selling directly would put Market.Place up against the networks it is describing. Being the neutral referee lets it monetize every one of them.

### Revenue model (assumptions, not promises)

Modelled at 100k monthly pageviews, which is realistic 12–18 months in with consistent publishing and calculator SEO:

| Stream | Assumption | Monthly |
|---|---|---|
| AdSense | RPM $6–15 (e-commerce/seller-tools niche, US/CA/UK-heavy) | $600–1,500 |
| Growth Desk leads | 0.08% of visitors submit; 20% close or are referred; $350 average fee or referral | $560–1,400 |
| Marketplace-launch consults | 1–2 per month at $500–2,000 (scoping, or referral to a build partner) | $500–4,000 |
| Sponsorships / featured listings | 1–2 sponsors at $250–1,000 | $250–2,000 |
| Donations / supporter tiers | Small; goodwill and community | $50–200 |
| **Total** | | **$1,960–9,100** |

**The lever:** a single marketplace-launch lead is worth more than a month of AdSense. Treat AdSense as the floor and the Growth Desk as the business.

### Biggest risks and the mitigations built in

1. **AdSense rejection for thin content.** The launch ships with 12 long-form guides, 16 in-depth platform profiles, 5 working tools, a 70+ entry directory, full legal pages, clear navigation, and no empty placeholder sections.
2. **Fee data going stale.** Every fee rule carries a verified date and a link to its official source, users can edit any rate in the calculator, and there is a quarterly re-verification task (see Phase 6).
3. **Trademark exposure around "marketplace".** The site uses only the stylized name "Market.Place", never "Marketplace" as a brand. It carries a full independence and nominative-use disclosure and no third-party logos.

---

## 2. Phase-wise build prompt (reusable)

### Phase 1: Foundation and compliance
> Build a static, responsive, accessible website for the domain **Market.Place**, hosted on GitHub Pages (free plan, this repository, `main` branch, root folder). Use plain HTML/CSS/JS with no server code. A Python generator in `_build/` writes the pages. Every page must include:
> - The Google AdSense loader in `<head>`: `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>`, plus `<meta name="google-adsense-account" content="ca-pub-6620975821265271">`, plus `ads.txt` at the root with `google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`.
> - A top strip on every page: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership". It links to the owner's contact URL, which is assembled at runtime from encoded parts so the owner's domain never appears in markup or visible text.
> - A cookie/consent notice with "Accept all" and "Essential only" (the latter requests non-personalized ads).
> - Privacy & cookies, Terms, Disclaimer, Trademark & copyright, About, Contact and Site map pages, all linked in the footer.
> - Canonical URLs, Open Graph tags, JSON-LD (WebSite, Organization, Article, FAQPage, BreadcrumbList), `sitemap.xml`, `robots.txt`, a web manifest, a custom 404 page and `.nojekyll`.
> - All forms post through one relay endpoint. The owner's single inbox address is stored encoded (reversed base64) in `config.js` and decoded only at send time. The address must never appear in HTML, visible text, README or docs. Every form gets a honeypot field.

### Phase 2: Design system
> Brand concept: "price tag and ledger". Warm paper background, deep market-green ink, tomato-red call-to-action colour, saffron highlight tags. Use Fraunces for display type and Manrope for UI and body text. Cards are styled like hang-tags, with a punched hole and a slight tilt on hover. Include light and dark themes and a mobile-first layout with a slide-down menu. The focus states, contrast (WCAG AA), skip link and reduced-motion support are all non-negotiable. Ad slots are clearly labelled "Advertisement" and kept away from buttons and form controls (AdSense placement policy).

### Phase 3: Traffic engine (tools and data)
> Build five working client-side tools:
> 1. **Fee & profit calculator.** It covers 16 platforms. Each fee rule has a percentage, a fixed amount, a base (item, or item plus shipping) and price tiers. The tool shows net payout, margin and profit, includes a "price to list to net $X" reverse mode, compares every platform at once as a sortable table, and lets users edit any rate. Each rate shows its verified date and source link.
> 2. **Marketplace Match quiz.** Six questions (what you sell, price band, region, local vs shipped, effort, audience) are scored against the platform matrix. It returns the top 3 platforms with reasons, a CTA into the Growth Desk, and a shareable result URL.
> 3. **Compare tool.** Pick 2–3 platforms for a side-by-side view of fees, reach, ease, protection and best fit.
> 4. **Flip / resale ROI calculator.** Takes cost, fees, shipping, supplies and hours, and returns profit, ROI and effective hourly rate.
> 5. **Scam red-flag checker.** An interactive checklist that scores risk and links the matching safety guides.
>
> Also build a **marketplace directory** of 70+ platforms, with search, category, region and model filters, plus 16 in-depth **platform profiles** (at a glance, who it's for, worked fee example, strengths, watch-outs, tips, buyer protection, editorial scores).

### Phase 4: Content engine
> Write 12 long-form, original, people-first guides (1,300–1,800 words each) across Selling, Buying, Safety and Business, each with key takeaways, checklists, tables and an FAQ (with FAQPage schema). Add a curated video library of verified YouTube videos (lite embeds with no third-party load until click, and youtube-nocookie). Use internal linking everywhere: guide to tool to profile to Growth Desk.

### Phase 5: Money engine
> - **Growth Desk** (`get-matched.html`): a high-converting, three-track, multi-step lead form ("Sell more on marketplaces", "Launch my own marketplace", "Sell my business / inventory"). It has a progress bar, one question per step, qualification fields (volume, budget, timeline), trust signals (what happens next, response time, no-spam promise), a consent checkbox, and a thank-you page with next steps. Teaser blocks for it appear on the home page, tools and guides.
> - **Support** (`support.html`): donation and supporter tiers, with a transparent breakdown of where money goes (operations, promotions and marketing, hiring talent, contests and prizes). It runs in pledge mode now, and switches to instant checkout when PayPal, Stripe or Buy Me a Coffee links are pasted into `config.js`.
> - **Contests** (`contests.html`): monthly contests with prizes, an entry form, and full official rules (no purchase necessary, eligibility, judging, odds, privacy, where void).
> - **Careers** (`careers.html`): open roles for contributors, marketplace experts, video creators and community moderators, with an application form.
> - **Advertise & sponsor** (`advertise.html`): audience, placements, rate guidance and an inquiry form. Partnership and domain-acquisition inquiries are routed through the top strip.

### Phase 6: Launch, approval and growth
> 1. Push to `main` and enable GitHub Pages (Settings → Pages → Deploy from a branch → `main` / root).
> 2. Point DNS at GitHub Pages: apex A records 185.199.108.153, .109, .110 and .111 (AAAA 2606:50c0:8000::153 to 8003::153), and a `www` CNAME pointing at your `<username>.github.io`. Then add a `CNAME` file containing `market.place` and tick "Enforce HTTPS".
> 3. Verify the domain in Google Search Console and submit `sitemap.xml`.
> 4. Apply in AdSense with the domain `market.place`. Once approved, Auto ads can be enabled. The labelled in-content slots are already in place.
> 5. Send one test submission from every form to activate the relay (the first message asks the inbox owner to confirm).
> 6. Growth plan: publish 2 new guides and 1 platform profile per month, re-verify fees quarterly, run one contest per month, and pitch the calculators to reseller communities and newsletters for links.
