"""Home, about, contact, legal, sitemap, 404."""
from mp import page, crumbs, esc, hp, status, ad, growth_cta, BASE_URL, TODAY, PAGES
from pages_money import radio_cards


def build_home(ctx):
    profiles, guides, videos, dir_count = ctx["profiles"], ctx["guides"], ctx["videos"], ctx["dir_count"]
    prof_cards = "".join(
        f'<a class="tag-card hole dir-card" href="marketplaces/{p["slug"]}.html"><span class="pill">{esc(p.get("category",""))}</span><h3 style="margin-top:6px">{esc(p["name"])}</h3><p>{esc(p.get("best_for",""))}</p><p class="fee"><strong>Fees:</strong> {esc(p.get("fee_summary",""))}</p></a>'
        for p in profiles[:8])
    guide_cards = "".join(
        f'<a class="tag-card hole" href="guides/{g["slug"]}.html"><span class="pill saffron">{esc(g.get("category",""))}</span><span class="pill">{g.get("read_minutes","")} min read</span><h3 style="margin-top:6px">{esc(g["title"])}</h3><p>{esc(g.get("description",""))}</p></a>'
        for g in guides[:6])
    vid_cards = "".join(
        f'<article class="vid-card"><button class="yt" data-yt="{esc(v["id"])}" aria-label="Play: {esc(v["title"])}"><span class="play"></span></button><h3>{esc(v["title"])}</h3><p class="small muted">{esc(v["channel"])}: {esc(v.get("why",""))}</p></article>'
        for v in videos[:3])
    tracks = [("Sell more on marketplaces", "🚀 Sell more", "Channel plan + listing fixes"), ("Launch my own marketplace", "🏗️ Launch a marketplace", "Niche, model, stack, launch"),
              ("Sell my business, store or inventory", "💼 Sell my store or stock", "Buyers, valuation, liquidation")]
    faq = [("Is Market.Place a place to buy and sell?", "No. Market.Place is an independent guide. We help you choose where to buy and sell, understand the fees, and stay safe. You list and buy on the platforms themselves."),
           ("Where does your fee data come from?", "From each platform's official fee and help pages. Every rule shows the date we verified it and links to its source. You can edit any rate in the calculator."),
           ("Do marketplaces pay you to rank them?", "No. Scores and recommendations are editorial and never sold. We earn money from clearly labelled ads, sponsorships and the optional Growth Desk."),
           ("Is it free?", "Yes. Every tool, profile and guide is free, with no account needed. Nothing you type into a calculator leaves your browser.")]
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Market.Place", "url": BASE_URL + "/",
           "description": "The independent guide to online marketplaces: compare platforms, calculate fees, sell smarter and buy safer."},
          {"@context": "https://schema.org", "@type": "Organization", "name": "Market.Place", "url": BASE_URL + "/", "logo": BASE_URL + "/assets/img/favicon.svg"},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    body = f"""<section class="hero"><div class="wrap hero-grid">
 <div>
  <span class="kicker">Independent · Free · No sign-up</span>
  <h1>Every marketplace, compared. Your <em>real profit</em>, calculated.</h1>
  <p class="lede">Market.Place helps you pick the right platform, see exactly what each one takes, write listings that sell and spot scams before they cost you. {len(profiles)} platforms profiled in depth, {dir_count}+ in the directory, and no paid rankings.</p>
  <div class="hero-cta"><a class="btn" href="tools/fee-calculator.html">Calculate my fees</a><a class="btn alt" href="tools/marketplace-match.html">Where should I sell?</a></div>
  <ul class="trust-row"><li>Fees checked against official pages</li><li>Every source linked</li><li>Nothing you type is stored</li></ul>
 </div>
 <div class="widget" id="mini-calc">
  <span class="kicker">Quick fee check</span>
  <h2>What will you actually keep?</h2>
  <div class="form" style="margin-top:12px">
   <div><label for="mc-platform">Platform</label><select id="mc-platform"></select></div>
   <div class="row"><div><label for="mc-price">Sale price</label><input id="mc-price" type="number" min="0" step="0.01" value="40" inputmode="decimal"></div>
   <div><label for="mc-ship">Shipping</label><input id="mc-ship" type="number" min="0" step="0.01" value="6" inputmode="decimal"></div></div>
   <div><label for="mc-cost">What it cost you</label><input id="mc-cost" type="number" min="0" step="0.01" value="10" inputmode="decimal"></div>
  </div>
  <div class="out" aria-live="polite"><div class="stat"><b id="mc-fees">$0</b><span>Fees</span></div><div class="stat"><b id="mc-payout">$0</b><span>Payout</span></div><div class="stat good"><b id="mc-profit">$0</b><span>Profit</span></div></div>
  <p style="margin:14px 0 0"><a class="link-arrow" id="mc-link" href="tools/fee-calculator.html">Full breakdown + compare all 16</a></p>
 </div>
</div></section>
<section class="dark-band tight"><div class="wrap stats-strip">
 <div><b>{len(profiles)}</b><span>platforms profiled in depth</span></div><div><b>{dir_count}+</b><span>marketplaces in the directory</span></div>
 <div><b>5</b><span>free tools, no sign-up</span></div><div><b>{len(guides)}</b><span>long-form guides</span></div>
</div></section>
<section><div class="wrap">
 <div class="sec-head"><div><span class="kicker">Free tools</span><h2>Do the math before you list</h2></div><p>Calculators and checkers built from official fee schedules and real seller workflows.</p></div>
 <div class="grid g3">
  <a class="tag-card hole reveal" href="tools/fee-calculator.html"><div class="ico">🧮</div><h3>Fee &amp; profit calculator</h3><p>16 platforms, every fee line, a reverse price finder and a compare-all table.</p></a>
  <a class="tag-card hole reveal" href="tools/marketplace-match.html"><div class="ico">🎯</div><h3>Marketplace Match quiz</h3><p>Six questions, your three best platforms, and why.</p></a>
  <a class="tag-card hole reveal" href="tools/compare.html"><div class="ico">⚖️</div><h3>Compare side by side</h3><p>Fees, payout, reach, ease and protection in one table.</p></a>
  <a class="tag-card hole reveal" href="tools/flip-calculator.html"><div class="ico">🔁</div><h3>Flip ROI calculator</h3><p>Profit, ROI and hourly rate before you buy to resell.</p></a>
  <a class="tag-card hole reveal" href="tools/scam-checker.html"><div class="ico">🛡️</div><h3>Scam red-flag checker</h3><p>Tick what you're seeing and get a risk score with next steps.</p></a>
  <a class="tag-card hole reveal" href="marketplaces/directory.html"><div class="ico">🗂️</div><h3>Marketplace directory</h3><p>{dir_count}+ platforms filtered by category, region and selling model.</p></a>
 </div>
</div></section>
{ad()}
<section class="band"><div class="wrap">
 <div class="sec-head"><div><span class="kicker">Platform profiles</span><h2>Know each marketplace before you list</h2></div><a class="btn alt small" href="marketplaces/index.html">All {len(profiles)} profiles</a></div>
 <div class="grid g4">{prof_cards}</div>
</div></section>
<section class="dark-band" id="growth"><div class="wrap cta-band">
 <div>
  <span class="kicker" style="color:var(--saffron)">The Growth Desk · free</span>
  <h2 style="font-size:clamp(1.9rem,3.6vw,2.8rem)">Get a free, written plan to sell more, or to launch your own marketplace</h2>
  <p style="font-size:1.08rem">Tell us what you sell and what you want. A marketplace strategist replies within two business days with the platforms to use, the listing fixes that matter most, and a 90-day roadmap. No obligation, no spam.</p>
  <ul class="trust-row" style="color:#CFE0D6"><li>Human-reviewed</li><li>Reply in 2 business days</li><li>Your data is never sold</li></ul>
 </div>
 <div class="lead-box" style="color:var(--ink)">
  <form class="form" data-form="Growth Desk quick lead" data-redirect="thank-you.html">
   {hp()}
   <span class="lbl">I want to…</span>
   {radio_cards("track", tracks)}
   <div><label for="ql-products">What do you sell?</label><input id="ql-products" name="products" required placeholder="e.g. vintage cameras, handmade soap"></div>
   <div class="row"><div><label for="ql-name">Name</label><input id="ql-name" name="name" required autocomplete="name"></div><div><label for="ql-email">Email</label><input id="ql-email" name="email" type="email" required autocomplete="email"></div></div>
   <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>Contact me about my free plan. <a href="privacy.html">Privacy</a></span></label>
   <button class="btn block" type="submit">Get my free plan</button>
   {status()}
   <p class="small muted" style="margin:0">Want to give more detail? Use the <a href="get-matched.html">full Growth Desk form</a>.</p>
  </form>
 </div>
</div></section>
<section><div class="wrap">
 <div class="sec-head"><div><span class="kicker">Guides</span><h2>Sell smarter, buy safer</h2></div><a class="btn alt small" href="guides/index.html">All guides</a></div>
 <div class="grid g3">{guide_cards}</div>
</div></section>
<section class="band"><div class="wrap">
 <div class="sec-head"><div><span class="kicker">Watch &amp; learn</span><h2>Handpicked videos for sellers</h2></div><a class="btn alt small" href="videos.html">Video library</a></div>
 <div class="grid g3">{vid_cards}</div>
</div></section>
<section><div class="wrap"><div class="grid g3">
 <div class="tag-card"><div class="ico">🏆</div><h3>Monthly contests</h3><p style="margin-bottom:12px">Best Flip, Listing Makeover and Scam Spotter, with prizes every month.</p><a class="link-arrow" href="contests.html">Enter free</a></div>
 <div class="tag-card"><div class="ico">💚</div><h3>Support independence</h3><p style="margin-bottom:12px">Reader support keeps rankings unpaid and the tools free.</p><a class="link-arrow" href="support.html">Become a supporter</a></div>
 <div class="tag-card"><div class="ico">🧑‍💻</div><h3>Work with us</h3><p style="margin-bottom:12px">Paid remote roles for writers, researchers and video creators.</p><a class="link-arrow" href="careers.html">See open roles</a></div>
</div></div></section>
{ad()}
<section class="tight"><div class="wrap narrow"><h2>About Market.Place</h2><div class="faq">{faq_html}</div></div></section>"""
    page("index.html", "Market.Place: compare online marketplaces, fees & profit", "Independent guide to online marketplaces. Compare eBay, Etsy, Amazon, Poshmark, Mercari and more, calculate real fees and profit, and avoid scams.",
         body, jsonld=ld, scripts='<script src="assets/js/data.js"></script><script src="assets/js/tools.js"></script>', priority="1.0")


def legal(path, title, desc, heading, html_body, key=None):
    c, ld = crumbs([("Home", "{pre}index.html"), (heading, None)])
    page(path, title, desc, f'<section class="article-head"><div class="wrap narrow">{c}<h1>{heading}</h1><p class="muted">Last updated {TODAY}</p></div></section><section class="tight" style="padding-top:0"><div class="wrap narrow prose">{html_body}</div></section>',
         jsonld=ld, priority="0.3", nav_key=key)


def build_core(ctx):
    build_home(ctx)
    # About
    c, ld = crumbs([("Home", "{pre}index.html"), ("About", None)])
    body = f"""<section class="article-head"><div class="wrap narrow">{c}<span class="kicker">About &amp; methodology</span><h1>We're the referee, not a player</h1>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">Market.Place is an independent publication that helps people choose, compare and succeed on online marketplaces. We don't run a marketplace, take a cut of your sales, or let any platform buy a better score.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap narrow prose">
<h2>Why we exist</h2>
<p>Selling online has never had more options, or more fine print. Fee structures change several times a year, a fee charged on shipping can quietly halve a thin margin, and scams change faster than help pages do. We built Market.Place to put the numbers, trade-offs and warning signs in one place, in plain language, for free.</p>
<h2 id="methodology">Methodology</h2>
<h3>Fee data</h3>
<p>Every fee rule in our calculators comes from the platform's official fee or help pages. We record the date we checked it and link to the source. We re-verify on a quarterly cycle and whenever a platform announces a change. Where a fee varies by category, we use the general rate and say so. You can override any rate in the calculator to match your category or account.</p>
<h3>Editorial scores</h3>
<p>Each profiled platform gets four 1–10 scores. They're judged against the same criteria on every platform:</p>
<ul><li><strong>Reach</strong>: the size and buying intent of the audience a typical seller can reach.</li><li><strong>Low fees</strong>: total seller cost on a typical sale (10 = cheapest).</li><li><strong>Ease</strong>: time and skill needed to list, sell, ship and get paid.</li><li><strong>Protection</strong>: how clear and fair seller and buyer protection programmes are.</li></ul>
<p>Scores are editorial judgments, not measurements. We explain the reasoning in each profile.</p>
<h3>The Marketplace Match quiz</h3>
<p>The quiz scores platforms on an editorial fit profile: the product types its buyers shop for, workable price bands, regional availability, local pickup, workload and seller type. Availability in your country weighs most.</p>
<h2 id="independence">Independence and how we make money</h2>
<ul><li><strong>Advertising:</strong> Google AdSense ads, always labelled and kept apart from tool results.</li><li><strong>Sponsorships:</strong> labelled sponsor slots in the newsletter, contests and directory. Sponsors never influence scores, rankings or fee data.</li><li><strong>Growth Desk:</strong> optional consulting and, with your permission, introductions to vetted specialists.</li><li><strong>Reader support:</strong> voluntary contributions via our <a href="support.html">support page</a>.</li></ul>
<p>We currently use no affiliate links in rankings or tool results. If that ever changes, links will be clearly disclosed and rankings will stay editorial.</p>
<h2>Editorial standards</h2>
<p>Guides are written from hands-on selling experience and checked against official sources. Specific figures link to their source. When we get something wrong, we fix it and note the change. Spotted an error? <a href="contact.html?topic=Correction">Send a correction</a>.</p>
<h2>Who's behind it</h2>
<p>Market.Place is run by a small, remote team of sellers, researchers and writers. We're always looking for people who have sold online and care about accuracy. See <a href="careers.html">careers</a>.</p>
</div></section>"""
    page("about.html", "About Market.Place & our methodology", "Who runs Market.Place, how we verify marketplace fees, how editorial scores work, and how we stay independent.", body, jsonld=ld, priority="0.5")

    # Contact
    c, ld = crumbs([("Home", "{pre}index.html"), ("Contact", None)])
    topics = ["General question", "Growth Desk / consulting", "Advertising & sponsorship", "Partnership", "Interest in this website or domain", "Fee update", "Correction", "Contest question", "Careers", "Privacy request", "Copyright / trademark notice", "Other"]
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Contact</span><h1>Talk to Market.Place</h1><p class="lede">Questions, corrections, partnerships or press: one form reaches the team, and we reply within two business days.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap tool-shell">
<div><div class="tag-card hole"><h3>Fastest routes</h3><ul style="padding-left:1.1em;margin:0">
<li>Want a selling or launch plan? Use the <a href="get-matched.html">Growth Desk</a>.</li><li>Advertising? See <a href="advertise.html">options &amp; rates</a>.</li>
<li>Interested in this website, domain, sponsorship or partnership? Use the <a href="contact.html" data-owner>owner contact link</a> (also at the top of every page).</li>
<li>Found an outdated fee? Pick "Fee update" and paste the official link.</li></ul></div></div>
<div class="panel"><form class="form" data-form="Contact message" data-ok="Message sent. We reply within two business days.">
 {hp()}
 <div><label for="ct-topic">Topic</label><select id="ct-topic" name="topic" required><option value="">Choose a topic</option>{"".join(f"<option>{esc(t)}</option>" for t in topics)}</select></div>
 <div class="row"><div><label for="c-name">Name</label><input id="c-name" name="name" required autocomplete="name"></div><div><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div></div>
 <div><label for="c-msg">Message</label><textarea id="c-msg" name="message" required></textarea></div>
 <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>I agree that Market.Place may use these details to reply to me. <a href="privacy.html">Privacy</a></span></label>
 <button class="btn" type="submit">Send message</button>
 {status()}
</form></div></div></section>
<script>try{{var t=new URLSearchParams(location.search).get("topic");if(t){{var s=document.getElementById("ct-topic");for(var i=0;i<s.options.length;i++)if(s.options[i].text===t)s.selectedIndex=i;}}}}catch(e){{}}</script>"""
    page("contact.html", "Contact Market.Place", "Contact Market.Place about selling help, advertising, partnerships, fee updates, corrections or careers.", body, jsonld=ld, priority="0.5")

    legal("privacy.html", "Privacy & cookie policy", "How Market.Place handles personal data, cookies, Google AdSense advertising, form submissions and your privacy rights.", "Privacy &amp; cookie policy", """
<p>This policy explains what information Market.Place ("we") collects when you use this website, how we use it, and your choices. Market.Place is an independent informational website.</p>
<h2>Information you give us</h2>
<p>When you submit a form (Growth Desk, contact, newsletter, support pledge, contest entry, job application or advertising inquiry), we receive the details you enter, such as your name, email address and message. We use them only to respond, provide what you asked for, run contests and send the newsletter if you subscribed. Form messages are delivered to our inbox through a third-party form-relay service (FormSubmit), which processes the data only to deliver it.</p>
<p>We never sell or rent your personal information. Growth Desk requests may be shared with one vetted partner only if you agree first.</p>
<h2>Calculators and tools</h2>
<p>Our calculators, quiz and checkers run entirely in your browser. What you type into them is not sent to us or stored on our servers. Some tools put your inputs in the page address so you can share a result, and that address stays on your device unless you share it.</p>
<h2>Cookies and local storage</h2>
<p>We use your browser's local storage to remember your theme (light or dark) and your cookie choice. Our host and font provider may log standard technical information (such as IP address and browser type) for security and performance.</p>
<h2>Advertising: Google AdSense</h2>
<ul>
<li>Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites.</li>
<li>Google's use of advertising cookies enables it and its partners to serve ads to users based on their visit to this site and/or other sites on the Internet.</li>
<li>You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>.</li>
<li>Learn more about <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</li>
</ul>
<p>If you choose "Essential only" in our cookie notice, we ask Google to show non-personalized ads. Visitors in the EEA, UK and Switzerland may be shown a Google-certified consent message, as required.</p>
<h2>Embedded videos</h2>
<p>Videos use YouTube's privacy-enhanced mode and load only when you click play. After that, YouTube's own privacy policy applies.</p>
<h2>Your rights</h2>
<p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA, Quebec Law 25, or the CCPA/CPRA), you may have the right to access, correct, delete or port your personal data and to object to certain processing. To make a request, use the <a href="contact.html?topic=Privacy%20request">contact form</a> with the topic "Privacy request". You can unsubscribe from the newsletter at any time.</p>
<h2>Retention and security</h2>
<p>We keep form submissions only as long as needed to handle your request, or as the law requires. The site is served over HTTPS.</p>
<h2>Children</h2>
<p>This site is not directed to children under 16, and we do not knowingly collect their personal information.</p>
<h2>Changes</h2>
<p>We may update this policy, and the date at the top shows the latest version.</p>""")

    legal("terms.html", "Terms of use", "Terms governing your use of Market.Place, its tools, content, forms and contests.", "Terms of use", """
<p>By using Market.Place you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>Informational use only</h2>
<p>Content, calculators and scores are general information to help you make your own decisions. They are not legal, tax, financial or professional advice. Results depend on the data you enter and on fee rules that platforms can change at any time.</p>
<h2>Accuracy</h2>
<p>We work hard to keep fee data current and link every source, but we can't guarantee completeness or accuracy. Always confirm fees and policies on the platform before you list, buy or sign up.</p>
<h2>Intellectual property</h2>
<p>The site's original text, calculators, scores, data compilations, designs and code are owned by Market.Place and protected by copyright. You may share links and quote short excerpts with attribution. You may not republish substantial portions, scrape the data or reproduce the tools without written permission. Third-party names and trademarks belong to their owners. See our <a href="trademark.html">trademark &amp; copyright disclosure</a>.</p>
<h2>Submissions</h2>
<p>When you send us content (contest entries, tips, corrections), you confirm it's yours to share and grant us a non-exclusive licence to use it as described on the relevant page. Don't submit other people's personal information.</p>
<h2>Third-party links</h2>
<p>We link to platforms and resources we don't control and aren't responsible for their content or practices.</p>
<h2>Acceptable use</h2>
<p>Don't misuse forms, attempt to disrupt the site, or use it for unlawful purposes.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, Market.Place is not liable for any loss arising from your use of the site or reliance on its content, including selling or buying decisions.</p>
<h2>Changes</h2>
<p>We may update these terms, and continued use means you accept the current version.</p>""")

    legal("disclaimer.html", "Disclaimer", "Market.Place disclaimer: independent informational content, fee accuracy, no professional advice, advertising and sponsorship disclosure.", "Disclaimer", """
<h2>Independence</h2>
<p>Market.Place is not affiliated with, endorsed by or sponsored by any marketplace or platform we cover. Platform names are used only to identify them.</p>
<h2>Fee data</h2>
<p>Fees are compiled from official sources on the date shown and can change without notice. Category exceptions, promotions, account levels, taxes, currency conversion and optional advertising can change what you actually pay. Confirm on the platform before you rely on a figure.</p>
<h2>No professional advice</h2>
<p>Guides on taxes, records, business or legal topics are general education, not advice for your situation. Consult a qualified professional where you live.</p>
<h2>Safety content</h2>
<p>Our scam and safety guidance lowers risk but can't eliminate it. If you're the victim of fraud, contact the platform, your bank or card issuer and the relevant authorities promptly.</p>
<h2>Advertising and sponsorship</h2>
<p>We show ads through Google AdSense and may feature labelled sponsors. Advertisers don't control or endorse our content, and we don't endorse advertised products unless we say so explicitly.</p>
<h2>External links and videos</h2>
<p>Linked sites and embedded videos are provided for convenience. Their owners are responsible for their content.</p>""")

    legal("trademark.html", "Trademark & copyright disclosure", "Market.Place trademark and copyright disclosure: independent publication, no affiliation with any 'Marketplace' brand, nominative use of platform names.", "Trademark &amp; copyright disclosure", """
<h2>About our name</h2>
<p><strong>"Market.Place"</strong> is the name of this independent website, written with a dot as the stylized form of its domain. We use it only as the title of an informational publication about online marketplaces. We don't use it, or "Marketplace", as a brand for any goods, payment services or trading platform.</p>
<h2>No affiliation</h2>
<p>Market.Place is not affiliated with, connected to, endorsed by or sponsored by any company or service whose name or mark includes "Marketplace", "Market Place" or something similar. That includes, without limitation, <em>Facebook Marketplace</em> (Meta Platforms, Inc.), <em>Amazon Marketplace</em> (Amazon.com, Inc.), <em>Walmart Marketplace</em> (Walmart Inc.), <em>Microsoft Marketplace / Azure Marketplace</em>, <em>Google Workspace Marketplace</em>, <em>Shopify Marketplace</em>, <em>Mercado Libre</em> and any other "marketplace" brand anywhere in the world. Nothing on this site implies any partnership with these companies.</p>
<h2>Use of third-party names</h2>
<p>eBay, Etsy, Amazon, Facebook, Meta, Walmart, Mercari, Poshmark, Depop, Vinted, OfferUp, Craigslist, Kijiji, Reverb, Whatnot, TikTok, StockX and every other company, product or service name on this site are trademarks or registered trademarks of their respective owners. We use them only to identify and accurately describe those services in editorial reviews, comparisons and calculators (nominative fair use). We don't use third-party logos.</p>
<h2>The word "marketplace"</h2>
<p>"Marketplace" is a common English word for a place where goods are bought and sold. We use it in that everyday, descriptive sense.</p>
<h2>Copyright</h2>
<p>© Market.Place. All original articles, guides, platform profiles, editorial scores, data compilations, calculators, quiz logic, page designs, graphics and source code on this site are protected by copyright. All rights reserved, except where stated. YouTube videos embedded here remain the property of their creators and are shown using YouTube's embedding features.</p>
<h2>Notices</h2>
<p>If you believe content on this site infringes your trademark or copyright, send a notice through our <a href="contact.html?topic=Copyright%20%2F%20trademark%20notice">contact form</a>. Include the work concerned, where it appears on our site, your contact details, and a statement that you are the rights holder or authorized to act for them. We review every notice promptly and remove or correct material where appropriate.</p>""")


def build_sitemap_page(ctx):
    profiles, guides = ctx["profiles"], ctx["guides"]
    from pages_tools import TOOLS
    c, ld = crumbs([("Home", "{pre}index.html"), ("Site map", None)])
    body = f"""<section class="article-head"><div class="wrap">{c}<h1>Site map</h1></div></section><section class="tight" style="padding-top:0"><div class="wrap sitemap-cols prose">
<h3>Main</h3><ul><li><a href="index.html">Home</a></li><li><a href="get-matched.html">Growth Desk</a></li><li><a href="videos.html">Videos</a></li><li><a href="contests.html">Contests</a></li><li><a href="support.html">Support</a></li><li><a href="advertise.html">Advertise</a></li><li><a href="careers.html">Careers</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li></ul>
<h3>Tools</h3><ul><li><a href="tools/index.html">All tools</a></li>{"".join(f'<li><a href="tools/{h}">{t}</a></li>' for h, t, _, _ in TOOLS)}</ul>
<h3>Marketplaces</h3><ul><li><a href="marketplaces/index.html">All profiles</a></li><li><a href="marketplaces/directory.html">Directory</a></li>{"".join(f'<li><a href="marketplaces/{p["slug"]}.html">{esc(p["name"])}</a></li>' for p in profiles)}</ul>
<h3>Guides</h3><ul><li><a href="guides/index.html">All guides</a></li>{"".join(f'<li><a href="guides/{g["slug"]}.html">{esc(g["title"])}</a></li>' for g in guides)}</ul>
<h3>Legal</h3><ul><li><a href="privacy.html">Privacy &amp; cookies</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclaimer.html">Disclaimer</a></li><li><a href="trademark.html">Trademark &amp; copyright</a></li></ul>
</div></section>"""
    page("sitemap.html", "Site map", "Every page on Market.Place: tools, marketplace profiles, guides and legal pages.", body, jsonld=ld, priority="0.3")
    page("404.html", "Page not found", "This page doesn't exist.", """<section class="page-hero"><div class="wrap narrow center"><span class="price-tag">404 · Sold out</span><h1 style="margin-top:16px">This page has left the market</h1>
<p class="lede" style="margin:0 auto 22px">The link may be old or mistyped. Try one of these instead:</p>
<div class="ticker" style="justify-content:center"><a class="btn" href="index.html">Home</a><a class="btn alt" href="tools/fee-calculator.html">Fee calculator</a><a class="btn alt" href="marketplaces/index.html">Marketplaces</a><a class="btn alt" href="guides/index.html">Guides</a></div></div></section>""", dynbase=True)
