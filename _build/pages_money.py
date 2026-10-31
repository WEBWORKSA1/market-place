"""Lead generation, support, contests, careers, advertise."""
from mp import page, crumbs, esc, hp, status, ad, BASE_URL


def radio_cards(name, opts, required=True, auto_label=None):
    return '<div class="choices" data-need-one>' + "".join(
        f'<label class="choice"><input type="radio" name="{name}" value="{esc(v)}"{" required" if required else ""}><span>{t}{"<small>" + s + "</small>" if s else ""}</span></label>'
        for v, t, s in opts) + "</div>"


def check_cards(name, opts):
    return '<div class="choices">' + "".join(
        f'<label class="choice"><input type="checkbox" name="{name}" value="{esc(v)}"><span>{v}</span></label>' for v in opts) + "</div>"


def options(opts, ph="Choose one"):
    return f'<option value="">{ph}</option>' + "".join(f"<option>{esc(o)}</option>" for o in opts)


COUNTRIES = ["United States", "Canada", "United Kingdom", "Australia", "India", "Germany", "France", "Spain", "Italy", "Netherlands", "Ireland", "New Zealand", "Mexico", "Brazil", "United Arab Emirates", "Singapore", "Philippines", "Nigeria", "South Africa", "Sri Lanka", "Other"]


def lead_form(compact=False):
    tracks = [("Sell more on marketplaces", "🚀 Sell more on marketplaces", "Channel plan, listings, pricing, cross-listing"),
              ("Launch my own marketplace", "🏗️ Launch my own marketplace", "Niche, model, tech stack, launch plan"),
              ("Sell my business, store or inventory", "💼 Sell my business, store or inventory", "Valuation pointers, buyers, liquidation"),
              ("Source products / wholesale", "📦 Source products / wholesale", "Suppliers, liquidation lots, B2B channels"),
              ("Partnership or something else", "🤝 Partnership or something else", "Media, data, co-marketing, other")]
    return f"""<form class="form" data-form="Growth Desk lead" data-steps data-redirect="{{pre}}thank-you.html" novalidate>
 {hp()}
 <div class="steps-bar" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
 <p class="kbd-hint" data-step-label></p>
 <fieldset class="step" data-auto style="border:0;padding:0;margin:0">
  <legend class="lbl" style="font-family:var(--display);font-size:1.45rem;font-weight:650;margin-bottom:14px">What can we help you with?</legend>
  {radio_cards("track", tracks)}
 </fieldset>
 <fieldset class="step" style="border:0;padding:0;margin:0">
  <legend class="lbl" style="font-family:var(--display);font-size:1.45rem;font-weight:650;margin-bottom:14px">Tell us about what you sell</legend>
  <div><label for="lf-role">You are…</label><select id="lf-role" name="role" required>{options(["Individual seller", "Reseller / flipper", "Brand or retailer", "Startup founder", "Agency or consultant", "Investor or acquirer", "Other"])}</select></div>
  <div><label for="lf-products">What do you sell, or plan to?</label><input id="lf-products" name="products" required placeholder="e.g. vintage denim, handmade candles, refurbished laptops"></div>
  <div><span class="lbl">Where do you sell today?</span>{check_cards("channels", ["eBay", "Etsy", "Amazon", "Facebook Marketplace", "Poshmark", "Mercari", "Depop / Vinted", "TikTok Shop / Whatnot", "Own website (Shopify etc.)", "Not selling yet"])}</div>
  <div class="step-acts"><button class="btn alt small" type="button" data-prev>Back</button><button class="btn" type="button" data-next>Continue</button></div>
 </fieldset>
 <fieldset class="step" style="border:0;padding:0;margin:0">
  <legend class="lbl" style="font-family:var(--display);font-size:1.45rem;font-weight:650;margin-bottom:14px">Your size and goals</legend>
  <div class="row"><div><label for="lf-vol">Monthly sales right now</label><select id="lf-vol" name="monthly_sales" required>{options(["Just starting", "Under $1,000", "$1,000 – $10,000", "$10,000 – $50,000", "$50,000 – $250,000", "$250,000+"])}</select></div>
  <div><label for="lf-time">When do you want results?</label><select id="lf-time" name="timeline" required>{options(["As soon as possible", "Within 1–3 months", "Within 3–6 months", "Just exploring"])}</select></div></div>
  <div><label for="lf-budget">Budget for outside help (optional)</label><select id="lf-budget" name="budget">{options(["Free advice only for now", "Under $500", "$500 – $2,500", "$2,500 – $10,000", "$10,000+", "Prefer to discuss"], "Choose if you like")}</select></div>
  <div><label for="lf-goal">What would a win look like in 90 days?</label><textarea id="lf-goal" name="goal" required placeholder="e.g. Double monthly sales, launch on Etsy, cut fees, find a buyer for my store, launch our marketplace MVP"></textarea></div>
  <div class="step-acts"><button class="btn alt small" type="button" data-prev>Back</button><button class="btn" type="button" data-next>Continue</button></div>
 </fieldset>
 <fieldset class="step" style="border:0;padding:0;margin:0">
  <legend class="lbl" style="font-family:var(--display);font-size:1.45rem;font-weight:650;margin-bottom:14px">Where should we send your plan?</legend>
  <div class="row"><div><label for="lf-name">Name</label><input id="lf-name" name="name" required autocomplete="name"></div>
  <div><label for="lf-email">Email</label><input id="lf-email" name="email" type="email" required autocomplete="email"></div></div>
  <div class="row"><div><label for="lf-country">Country</label><select id="lf-country" name="country" required>{options(COUNTRIES)}</select></div>
  <div><label for="lf-phone">Phone or WhatsApp (optional)</label><input id="lf-phone" name="phone" type="tel" autocomplete="tel"></div></div>
  <div><label for="lf-url">Store or website link (optional)</label><input id="lf-url" name="store_url" type="url" placeholder="https://"></div>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>I agree that Market.Place may contact me about this request. If it helps, my request may be shared with one vetted partner, and only with my OK first. See the <a href="{{pre}}privacy.html">privacy policy</a>.</span></label>
  <div class="step-acts"><button class="btn alt small" type="button" data-prev>Back</button><button class="btn" type="submit">Send me my free plan</button></div>
 </fieldset>
 {status()}
</form>"""


def build_money():
    # ------------- Growth Desk -------------
    c, ld = crumbs([("Home", "{pre}index.html"), ("Growth Desk", None)])
    faq = [("Is it really free?", "Yes. The first plan is free and comes with no obligation. If you want hands-on help afterwards (listing rewrites, store setup, a marketplace build), we'll quote it clearly or introduce you to a vetted specialist. You decide."),
           ("Who reads my request?", "A Market.Place editor who works on marketplace strategy every day. Not a bot, and not a call centre."),
           ("Will you sell my details?", "No. We never sell or rent contact details. We only make an introduction to a partner if you say yes first."),
           ("How fast will I hear back?", "Within two business days, usually sooner. Complex marketplace-launch requests may get a short follow-up question first."),
           ("Do you work outside the US?", "Yes. We cover North America, the UK, Europe, India, Australia and global cross-border selling.")]
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    body = f"""<section class="page-hero"><div class="wrap">{c}</div></section>
<section style="padding-top:0"><div class="wrap cta-band" style="align-items:start">
 <div>
  <span class="kicker">The Market.Place Growth Desk</span>
  <h1 style="font-size:clamp(2rem,4.4vw,3.2rem)">Get a free, expert plan to sell more or launch your own marketplace</h1>
  <p class="lede" style="font-size:1.12rem;color:var(--ink-2)">Answer four short steps (about 90 seconds). A real marketplace strategist reviews your products, numbers and goals, then sends a written plan: where to sell, what to fix first, and what results to expect.</p>
  <div class="lead-box" style="margin-top:22px">{lead_form()}</div>
 </div>
 <aside class="sidebar" style="top:90px">
  <div class="tag-card hole"><h3>What's in your free plan</h3><ul style="padding-left:1.1em;margin:0">
   <li>The 1–3 platforms that fit your products and margins</li><li>Fee and profit check on your top items</li><li>Your three highest-impact listing fixes</li><li>A cross-listing or launch roadmap for 90 days</li><li>Honest "don't do this" warnings</li></ul></div>
  <div class="tag-card"><h3>How it works</h3><ol class="steps-list"><li><strong>Tell us your goal.</strong> Four steps, no account needed.</li><li><strong>We review.</strong> A strategist checks your products and channels.</li><li><strong>You get a plan.</strong> Written, specific, and yours to keep, within 2 business days.</li></ol></div>
  <div class="notice">🔒 No spam, no data selling. One reply from a person, plus an optional follow-up.</div>
 </aside>
</div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div><span class="kicker">Who we help</span><h2>Four kinds of people use the Growth Desk</h2></div></div>
<div class="grid g4">
 <div class="tag-card"><div class="ico">🧺</div><h3>Side-hustle sellers</h3><p>You're selling on one platform and want to know whether a second is worth the effort.</p></div>
 <div class="tag-card"><div class="ico">🔁</div><h3>Resellers</h3><p>You source in volume and want better sell-through, cleaner cross-listing and fewer fee surprises.</p></div>
 <div class="tag-card"><div class="ico">🏷️</div><h3>Brands &amp; retailers</h3><p>You want Amazon, Walmart, Etsy or TikTok Shop as a channel without wrecking your margins.</p></div>
 <div class="tag-card"><div class="ico">🏗️</div><h3>Marketplace founders</h3><p>You're building a niche marketplace and need help with the niche, take rate, liquidity and stack.</p></div>
</div></div></section>
<section><div class="wrap narrow"><h2>Questions, answered</h2><div class="faq">{faq_html}</div>
<p style="margin-top:24px">Prefer to read first? Try the <a href="tools/marketplace-match.html">Marketplace Match quiz</a> or our guide to <a href="guides/launch-your-own-marketplace.html">launching your own marketplace</a>.</p></div></section>"""
    page("get-matched.html", "Growth Desk: free marketplace growth plan", "Get a free expert plan to sell more on eBay, Etsy, Amazon and other marketplaces, or to launch your own marketplace. Reply within 2 business days.",
         body, nav_key=None, jsonld=[ld, faq_ld], priority="1.0")

    # ------------- Thank you -------------
    page("thank-you.html", "Thanks, your request is in", "Your Growth Desk request has been received.", """<section class="page-hero"><div class="wrap narrow center">
<div class="ico" style="margin:0 auto 16px;width:64px;height:64px;font-size:2rem">✅</div>
<h1>Got it. Your plan is in the queue.</h1>
<p class="lede" style="margin:0 auto">A Market.Place strategist will review your request and reply within two business days. Check your spam folder if you don't see us. Meanwhile, here are three useful next steps:</p>
<div class="grid g3" style="margin-top:28px;text-align:left">
<a class="tag-card hole" href="tools/fee-calculator.html"><h3>Check your fees</h3><p>See what every platform takes from your best-selling item.</p></a>
<a class="tag-card hole" href="guides/write-listings-that-sell.html"><h3>Fix your listings</h3><p>Titles and descriptions that get found and convert.</p></a>
<a class="tag-card hole" href="contests.html"><h3>Enter this month's contest</h3><p>Share your best flip or listing makeover to win prizes.</p></a></div>
</div></section>""")

    # ------------- Support / donations -------------
    c, ld = crumbs([("Home", "{pre}index.html"), ("Support", None)])
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Keep Market.Place independent</span><h1>Support free, independent marketplace research</h1>
<p class="lede">No platform pays to be ranked here. Every calculator, profile and guide is free and paid for by ads and readers like you. Your support covers the hours spent re-checking fee pages, testing platforms and writing honest guides.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap tool-shell">
<div class="panel">
 <h2>Choose an amount</h2>
 <div class="tiers" style="grid-template-columns:repeat(2,1fr)">
  <button type="button" class="tier" data-amount="5" aria-pressed="false"><b>$5</b><span class="small">Coffee for a fee-checker</span></button>
  <button type="button" class="tier" data-amount="15" aria-pressed="true"><b>$15</b><span class="small">Funds one platform re-verification</span></button>
  <button type="button" class="tier" data-amount="50" aria-pressed="false"><b>$50</b><span class="small">Sponsors a new guide</span></button>
  <button type="button" class="tier" data-amount="250" aria-pressed="false"><b>$250</b><span class="small">Founding supporter (named on the site)</span></button>
 </div>
 <div id="pay-links" class="ticker" style="margin-top:16px"></div>
 <p id="pay-note" class="small muted" hidden>Payments are processed securely by the provider you choose. We never see your card details.</p>
 <h3 style="margin-top:22px">Where your money goes</h3>
 <div class="alloc">
  <div><span><strong>Operations</strong>: hosting, tools, fee re-verification</span><b>35%</b></div><div class="bar"><i style="width:35%"></i></div>
  <div><span><strong>Promotions &amp; marketing</strong>: reaching sellers who need this</span><b>25%</b></div><div class="bar"><i style="width:25%"></i></div>
  <div><span><strong>Hiring talent</strong>: writers, researchers, video creators</span><b>20%</b></div><div class="bar"><i style="width:20%"></i></div>
  <div><span><strong>Contests &amp; prizes</strong>: rewarding the community</span><b>20%</b></div><div class="bar"><i style="width:20%"></i></div>
 </div>
</div>
<div class="panel">
 <h2>Make a pledge</h2>
 <p class="muted">Pledge below and we'll send you a secure payment link for your amount and preferred method, with a receipt. It takes 30 seconds.</p>
 <form class="form" data-form="Support pledge" data-ok="Thank you! We'll email your secure payment link within one business day.">
  {hp()}
  <div class="row"><div><label for="amount">Amount (USD)</label><input id="amount" name="amount" type="number" min="1" step="1" value="15" required></div>
  <div><label for="freq">How often</label><select id="freq" name="frequency"><option>One time</option><option>Monthly</option><option>Yearly</option></select></div></div>
  <div><label for="fund">Put it towards (optional)</label><select id="fund" name="allocate_to"><option value="">Wherever it's needed most</option><option>Operations</option><option>Promotions &amp; marketing</option><option>Hiring talent</option><option>Contests &amp; prizes</option></select></div>
  <div><label for="pm">Preferred payment method</label><select id="pm" name="payment_method"><option>Card</option><option>PayPal</option><option>Bank transfer / Interac</option><option>UPI (India)</option><option>Other</option></select></div>
  <div class="row"><div><label for="s-name">Name</label><input id="s-name" name="name" required autocomplete="name"></div><div><label for="s-email">Email</label><input id="s-email" name="email" type="email" required autocomplete="email"></div></div>
  <div><label for="s-msg">Message (optional)</label><textarea id="s-msg" name="message" style="min-height:80px"></textarea></div>
  <label class="check"><input type="checkbox" name="public_credit" value="yes"> <span>Thank me publicly on the supporters list</span></label>
  <button class="btn" type="submit">Pledge my support</button>
  {status()}
  <p class="small muted">Contributions support an independent publication and are not tax-deductible charitable donations. Supporters get no editorial influence. See our <a href="about.html#independence">independence policy</a>.</p>
 </form>
</div></div></section>
<section class="band"><div class="wrap"><h2>Other ways to help</h2><div class="grid g4">
<div class="tag-card"><div class="ico">📣</div><h3>Share a tool</h3><p>Post the <a href="tools/fee-calculator.html">fee calculator</a> in a seller group that would find it useful.</p></div>
<div class="tag-card"><div class="ico">✍️</div><h3>Contribute</h3><p>Write, research or film with us. Paid roles are on the <a href="careers.html">careers page</a>.</p></div>
<div class="tag-card"><div class="ico">🏆</div><h3>Sponsor a contest</h3><p>Put your brand behind a monthly prize. <a href="advertise.html">See options</a>.</p></div>
<div class="tag-card"><div class="ico">🐛</div><h3>Report a fee change</h3><p>Spotted outdated data? <a href="contact.html?topic=Fee%20update">Tell us</a> and we'll credit you.</p></div>
</div></div></section>"""
    page("support.html", "Support Market.Place", "Support independent marketplace research. Donations fund operations, promotion, hiring writers and researchers, and community contests and prizes.",
         body, nav_key="support", jsonld=ld, priority="0.6")

    # ------------- Contests -------------
    c, ld = crumbs([("Home", "{pre}index.html"), ("Contests", None)])
    contests = [
        ("🔁", "Best Flip of the Month", "Show us your best resale: what you paid, where you sold it, what you netted after fees. We judge on profit, creativity and how useful the story is to other sellers.", "$100 prize + featured story", "flip"),
        ("✨", "Listing Makeover Challenge", "Share a before-and-after listing: new photos, title and description. Bonus points if you can show more views or a faster sale.", "$75 prize + expert listing review", "makeover"),
        ("🛡️", "Scam Spotter", "Spotted a clever marketplace scam? Send screenshots with personal details removed and explain the red flags. The best entries become public safety alerts.", "$50 prize + credit in our alert", "scam"),
    ]
    cards = "".join(f'<article class="tag-card hole lift"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p><p style="margin-top:12px"><span class="price-tag">{p}</span></p></article>' for i, t, d, p, k in contests)
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Monthly contests</span><h1>Win prizes for selling smart</h1>
<p class="lede">Every month we run three free contests for sellers and buyers. No purchase needed. Winners are announced in the first week of the following month on this page and in Market Notes.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="band"><div class="wrap tool-shell">
<div><h2>Enter now</h2><p>One entry per person per contest each month. Original work only. Remove personal information from screenshots (names, addresses, order numbers).</p>
<div class="notice"><strong>Sponsors wanted.</strong> Want to put your product in front of motivated sellers? Sponsor a monthly prize. <a href="advertise.html">Contest sponsorship options</a>.</div></div>
<div class="panel"><form class="form" data-form="Contest entry" data-ok="Entry received. Good luck! Winners are announced in the first week of next month.">
 {hp()}
 <div><label for="ct-which">Contest</label><select id="ct-which" name="contest" required><option value="">Choose a contest</option>{"".join(f"<option>{t}</option>" for _, t, _, _, _ in contests)}</select></div>
 <div class="row"><div><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div><div><label for="ct-email">Email</label><input id="ct-email" name="email" type="email" required autocomplete="email"></div></div>
 <div><label for="ct-country">Country</label><input id="ct-country" name="country" required autocomplete="country-name"></div>
 <div><label for="ct-story">Your entry</label><textarea id="ct-story" name="entry" required placeholder="Tell the story with numbers: cost, sale price, fees, platform, what you changed…"></textarea></div>
 <div><label for="ct-link">Link to photos or listing (Google Drive, Imgur, listing URL)</label><input id="ct-link" name="link" type="url" placeholder="https://"></div>
 <label class="check"><input type="checkbox" name="age_rules" value="yes" required> <span>I'm 18 or older (or the age of majority where I live) and I accept the official rules below.</span></label>
 <label class="check"><input type="checkbox" name="feature_ok" value="yes"> <span>Market.Place may publish my entry with my first name and country</span></label>
 <button class="btn" type="submit">Submit my entry</button>
 {status()}
</form></div></div></section>
<section><div class="wrap narrow prose" id="rules"><h2>Official rules (summary)</h2>
<ol>
<li><strong>No purchase necessary.</strong> Buying anything does not improve your chance of winning. Void where prohibited or restricted by law.</li>
<li><strong>Eligibility.</strong> Open to individuals who are 18 or older (or the age of majority in their place of residence) in jurisdictions where the contest is lawful. Market.Place staff, contractors and sponsors' employees, and their immediate families, are not eligible.</li>
<li><strong>Entry period.</strong> Each contest runs from the first day of the calendar month at 00:00 to the last day at 23:59 Eastern Time.</li>
<li><strong>Judging.</strong> These are skill-based contests, not lotteries. A panel of Market.Place editors scores entries on usefulness to other sellers (40%), clarity and evidence (30%) and originality (30%). Judges' decisions are final.</li>
<li><strong>Prizes.</strong> Prize values are shown in USD and paid by digital gift card or PayPal within 30 days of the winner confirming. Market.Place may substitute a prize of equal or greater value. Prizes aren't transferable. Winners are responsible for any taxes. Canadian residents must correctly answer a time-limited skill-testing question to claim a prize.</li>
<li><strong>Notification.</strong> Winners are notified by email and must reply within 14 days or an alternate winner may be chosen.</li>
<li><strong>Licence.</strong> You keep ownership of your entry. By entering you grant Market.Place a non-exclusive, royalty-free licence to publish it (with your first name and country, if you agreed) for editorial and promotional use.</li>
<li><strong>Conduct.</strong> Entries must be your own, truthful, and free of personal data belonging to others. We may disqualify plagiarised, fraudulent or offensive entries.</li>
<li><strong>Privacy.</strong> Entry data is used only to run the contest. See our <a href="privacy.html">privacy policy</a>.</li>
<li><strong>Not sponsored by any platform.</strong> These contests are not sponsored, endorsed or administered by eBay, Etsy, Amazon, Meta or any other marketplace mentioned.</li>
</ol></div></section>"""
    page("contests.html", "Contests & prizes for online sellers", "Free monthly contests for marketplace sellers: Best Flip of the Month, Listing Makeover Challenge and Scam Spotter. Win cash prizes and features.",
         body, nav_key="contests", jsonld=ld, priority="0.6")

    # ------------- Careers -------------
    c, ld = crumbs([("Home", "{pre}index.html"), ("Careers", None)])
    roles = [
        ("Marketplace Fee Researcher", "Contract · Remote · ~10 h/month", "Re-verify fee schedules on the platforms we cover against their official pages each quarter, log changes and update the data behind our calculators."),
        ("Contributing Writer: Reselling & E-commerce", "Freelance · Remote · Per article", "Write practical, original guides from real selling experience. You've sold on at least two marketplaces and can show your numbers."),
        ("Short-form Video Creator", "Freelance · Remote · Per video", "Turn our tools and guides into 30–90 second tutorials for YouTube Shorts, TikTok and Reels."),
        ("Community & Contest Moderator", "Part-time · Remote", "Review contest entries, keep the newsletter community friendly and help pick monthly winners."),
        ("Partnerships & Ad Sales", "Commission · Remote", "Bring in contest sponsors, newsletter sponsors and Growth Desk partners from e-commerce SaaS, logistics and seller services."),
        ("Growth Desk Partner (agencies & consultants)", "Partner network", "Marketplace agencies, Amazon/Etsy consultants and marketplace developers can apply to receive vetted, opted-in referrals."),
    ]
    rc = "".join(f'<article class="tag-card hole"><h3>{t}</h3><p class="small" style="color:var(--tomato);font-weight:700;margin-bottom:8px">{m}</p><p>{d}</p></article>' for t, m, d in roles)
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Careers &amp; contributors</span><h1>Help sellers keep more of every sale</h1>
<p class="lede">We're a small, remote, independent team. We hire people who have actually sold online and care about getting the numbers right. Pay is project-based and agreed up front.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap"><div class="grid g3">{rc}</div></div></section>
<section class="band"><div class="wrap tool-shell"><div><h2>Apply</h2><p>Tell us which role you want, show us something you've made, and tell us a marketplace lesson you learned the hard way. We reply to every applicant within ten business days.</p>
<ul><li>Fully remote, async-first</li><li>Paid per project or hour, agreed in writing</li><li>Bylines and portfolio credit</li></ul></div>
<div class="panel"><form class="form" data-form="Job application" data-ok="Application received. Thank you! We reply to every applicant within ten business days.">
 {hp()}
 <div><label for="jb-role">Role</label><select id="jb-role" name="role" required><option value="">Choose a role</option>{"".join(f"<option>{t}</option>" for t, _, _ in roles)}</select></div>
 <div class="row"><div><label for="jb-name">Name</label><input id="jb-name" name="name" required autocomplete="name"></div><div><label for="jb-email">Email</label><input id="jb-email" name="email" type="email" required autocomplete="email"></div></div>
 <div class="row"><div><label for="jb-loc">Location / time zone</label><input id="jb-loc" name="location" required></div><div><label for="jb-port">Portfolio, LinkedIn or store link</label><input id="jb-port" name="portfolio" type="url" required placeholder="https://"></div></div>
 <div><label for="jb-why">Experience and one hard-won marketplace lesson</label><textarea id="jb-why" name="experience" required></textarea></div>
 <button class="btn" type="submit">Send application</button>
 {status()}
</form></div></div></section>"""
    page("careers.html", "Careers, contributors & partner network", "Paid remote roles at Market.Place: fee researcher, e-commerce writers, video creators, moderators, ad sales, plus the Growth Desk partner network.",
         body, jsonld=ld, priority="0.5")

    # ------------- Advertise -------------
    c, ld = crumbs([("Home", "{pre}index.html"), ("Advertise & sponsor", None)])
    offers = [
        ("📰", "Market Notes sponsorship", "One sponsor per weekly issue, in a native slot clearly marked \"Sponsor\".", "from $99 / issue"),
        ("🧮", "Presented-by tool sponsorship", "Your brand on a calculator or quiz page for a month, as a labelled sponsor card. Rankings and results are never affected.", "from $499 / month"),
        ("🏆", "Contest sponsorship", "Fund a monthly prize and get named in the contest, the winners' post and the newsletter.", "from $250 / contest"),
        ("📌", "Featured directory listing", "A highlighted, clearly labelled \"Sponsored\" card in the marketplace directory, for marketplaces and seller tools.", "from $49 / month"),
        ("🎥", "Sponsored video segment", "A clearly disclosed integration in one of our tutorial videos.", "quoted per video"),
        ("🤝", "Partnerships & domain inquiries", "Co-marketing, data licensing, white-label calculators, or interest in acquiring this website or domain.", "let's talk"),
    ]
    oc = "".join(f'<article class="tag-card hole"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p><p style="margin-top:12px"><span class="price-tag">{p}</span></p></article>' for i, t, d, p in offers)
    body = f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Advertise, sponsor, partner</span><h1>Reach people at the moment they decide where and how to sell</h1>
<p class="lede">Our readers are working out fees, choosing platforms and fixing listings. That's high intent for seller tools, shipping and packaging, e-commerce software, marketplace platforms and financial services for small businesses.</p></div></section>
<section class="tight" style="padding-top:0"><div class="wrap"><div class="grid g3">{oc}</div>
<p class="small muted" style="margin-top:14px">Our editorial rules: sponsors never influence scores, rankings, fee data or reviews. Every paid placement is labelled. We turn down products we wouldn't recommend to a friend.</p></div></section>
<section class="band"><div class="wrap tool-shell"><div><h2>Tell us what you have in mind</h2><p>Send your goals and budget, and we'll reply with availability, current audience numbers and a proposal within two business days.</p>
<p>For partnership, sponsorship or acquisition interest in this website or domain, you can also use the <a href="contact.html" data-owner>owner contact link</a> at the top of every page.</p></div>
<div class="panel"><form class="form" data-form="Advertising inquiry" data-ok="Thanks! We'll reply with availability and a proposal within two business days.">
 {hp()}
 <div class="row"><div><label for="ad-name">Name</label><input id="ad-name" name="name" required autocomplete="name"></div><div><label for="ad-email">Work email</label><input id="ad-email" name="email" type="email" required autocomplete="email"></div></div>
 <div class="row"><div><label for="ad-co">Company</label><input id="ad-co" name="company" required autocomplete="organization"></div><div><label for="ad-site">Website</label><input id="ad-site" name="website" type="url" placeholder="https://"></div></div>
 <div><span class="lbl">Interested in</span><div class="choices">{"".join(f'<label class="choice"><input type="checkbox" name="interest" value="{esc(t)}"><span>{t}</span></label>' for _, t, _, _ in offers)}</div></div>
 <div class="row"><div><label for="ad-budget">Budget</label><select id="ad-budget" name="budget"><option value="">Choose</option><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option></select></div><div><label for="ad-start">Ideal start</label><input id="ad-start" name="start" placeholder="e.g. next month"></div></div>
 <div><label for="ad-msg">Goals</label><textarea id="ad-msg" name="message" required></textarea></div>
 <button class="btn" type="submit">Request a proposal</button>
 {status()}
</form></div></div></section>"""
    page("advertise.html", "Advertise, sponsor & partner with Market.Place", "Sponsor Market Notes, tools, contests and directory listings, or partner with Market.Place to reach high-intent online sellers.",
         body, nav_key="advertise", jsonld=ld, priority="0.6")
