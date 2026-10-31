"""Tool pages."""
from mp import page, crumbs, esc, hp, status, ad, growth_cta, BASE_URL
from platforms import PRODUCT_TYPES, BANDS, REGIONS, DELIVERY, EFFORT, SELLER

TOOLS = [
    ("fee-calculator.html", "Fee & profit calculator", "See exactly what every platform takes from a sale, what lands in your account, and your real profit. 16 platforms, editable rates, and a reverse price finder.", "🧮"),
    ("marketplace-match.html", "Marketplace Match quiz", "Six quick questions, three best-fit marketplaces, each with the reasons behind the pick. Built for anyone wondering where to sell.", "🎯"),
    ("compare.html", "Compare platforms", "Line up two or three marketplaces side by side: fees, payout on a sample sale, reach, ease and buyer protection.", "⚖️"),
    ("flip-calculator.html", "Flip ROI calculator", "Thinking of buying something to resell? Check profit, ROI and your effective hourly rate before you buy.", "🔁"),
    ("scam-checker.html", "Scam red-flag checker", "Tick the warning signs you're seeing in a listing or chat and get a risk score with what to do next.", "🛡️"),
]


def tool_jsonld(name, desc, path):
    return {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "description": desc,
            "url": f"{BASE_URL}/tools/{path}", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}


def hero(title, lede, crumb_label, kicker="Free tool"):
    c, ld = crumbs([("Home", "{pre}index.html"), ("Tools", "{pre}tools/index.html"), (crumb_label, None)])
    return f'<section class="page-hero"><div class="wrap">{c}<span class="kicker">{kicker}</span><h1>{title}</h1><p class="lede">{lede}</p></div></section>', ld


SCRIPTS = '<script src="{pre}assets/js/data.js"></script><script src="{pre}assets/js/tools.js"></script>'


def build_tools():
    # index
    cards = "".join(f'<a class="tag-card hole" href="{h}"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></a>' for h, t, d, i in TOOLS)
    c, ld = crumbs([("Home", "{pre}index.html"), ("Tools", None)])
    page("tools/index.html", "Free marketplace seller tools", "Free tools for online sellers and buyers: fee and profit calculator, Marketplace Match quiz, platform comparison, flip ROI calculator and scam checker.",
         f"""<section class="page-hero"><div class="wrap">{c}<span class="kicker">Free, no sign-up</span><h1>Tools that do the math before you list</h1>
<p class="lede">Every tool runs in your browser. Nothing you type is stored or sent anywhere. Fee rules come from each platform's official pages and show the date we last checked them.</p></div></section>
<section class="tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
{ad()}
<section class="tight"><div class="wrap">{growth_cta()}</div></section>""", nav_key="tools", jsonld=ld, priority="0.9")

    # Fee calculator
    h, ld = hero("Marketplace fee &amp; profit calculator", "Pick a platform, enter your price and costs, and see every fee line, your payout and your real profit. The table below runs the same sale on all 16 platforms at once. Want to try a different rate? Edit it.", "Fee & profit calculator")
    body = h + f"""<section class="tight" style="padding-top:0"><div class="wrap">
<div class="tool-shell" id="fee-calc">
 <div class="panel">
  <div class="seg" role="group" aria-label="Calculator mode"><button type="button" data-mode="profit" aria-pressed="true">Profit from price</button><button type="button" data-mode="reverse" aria-pressed="false">Price to hit a profit</button></div>
  <div class="form" id="fc-inputs">
   <div><label for="fc-platform">Platform</label><select id="fc-platform"></select></div>
   <div id="fc-price-wrap"><label for="fc-price">Item price</label><input id="fc-price" type="number" min="0" step="0.01" value="50" inputmode="decimal"></div>
   <div id="fc-target-wrap" hidden><label for="fc-target">Profit you want per sale</label><input id="fc-target" type="number" min="0" step="0.01" value="20" inputmode="decimal"></div>
   <div class="row"><div><label for="fc-ship">Shipping charged to buyer</label><input id="fc-ship" type="number" min="0" step="0.01" value="8" inputmode="decimal"></div>
   <div><label for="fc-shipcost">Your actual shipping cost</label><input id="fc-shipcost" type="number" min="0" step="0.01" value="8" inputmode="decimal"></div></div>
   <div class="row"><div><label for="fc-cost">What the item cost you</label><input id="fc-cost" type="number" min="0" step="0.01" value="15" inputmode="decimal"></div>
   <div><label for="fc-other">Packaging &amp; other</label><input id="fc-other" type="number" min="0" step="0.01" value="1" inputmode="decimal"></div></div>
  </div>
 </div>
 <div class="panel" aria-live="polite">
  <span class="kicker" id="fc-headline-label">Your profit</span>
  <div class="result-big" id="fc-big">$0.00</div>
  <div class="out" style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:10px">
   <div class="stat"><b id="fc-fees">$0</b><span>Total platform fees</span></div>
   <div class="stat"><b id="fc-feepct">0%</b><span>Fees as % of sale</span></div>
   <div class="stat good"><b id="fc-margin">0%</b><span>Profit margin</span></div>
  </div>
  <ul class="breakdown" id="fc-breakdown"></ul>
  <h3 style="margin-top:22px;font-size:1.05rem">Fee rules used (editable)</h3>
  <div id="fc-rates" class="table-scroll"></div>
  <label for="fc-share" class="lbl" style="margin-top:12px">Share this calculation</label>
  <div style="display:flex;gap:8px"><input id="fc-share" readonly><button type="button" class="btn small alt" id="fc-copy">Copy link</button></div>
 </div>
</div>
</div></section>
<section class="tight"><div class="wrap">
 <div class="sec-head"><div><span class="kicker">Same sale, every platform</span><h2>Where does a <span id="fc-all-price">$50</span> sale pay you most?</h2></div><p>Click a column to sort. The best result is highlighted. Amounts use each platform's home currency at face value, so convert before comparing across currencies.</p></div>
 <div class="table-scroll"><table class="data sortable" id="fc-all"><thead><tr><th data-sort>Platform</th><th data-sort class="num">Fees</th><th data-sort class="num">Fee %</th><th data-sort class="num">Payout</th><th data-sort class="num">Profit</th></tr></thead><tbody></tbody></table></div>
</div></section>
{ad()}
<section class="tight"><div class="wrap layout-side"><div class="prose">
<h2>How this calculator works</h2>
<p>Each platform's fees are stored as simple rules: a percentage, a fixed amount, and what the percentage is charged on (the item price alone, or the item price plus the shipping the buyer pays). Some rules only kick in within a price band, like a flat fee under a threshold and a percentage above it. The calculator adds up every rule that applies to your price, subtracts the total from what the buyer pays, then takes off your own costs.</p>
<h3>What's included and what isn't</h3>
<ul><li><strong>Included:</strong> selling or referral fees, transaction fees, payment processing and per-order fixed fees, where the platform publishes them.</li>
<li><strong>Not included:</strong> optional promoted-listing ads, monthly subscriptions (shown as a note), currency conversion, sales tax or VAT the platform collects from buyers, and category exceptions beyond the general rate.</li></ul>
<h3>Why profit is lower than you think</h3>
<p>The fee line most new sellers miss is the percentage charged on shipping. If a platform charges its fee on the order total, a $10 shipping charge costs you more than $10. The other one is packaging: boxes, mailers, tape and labels quietly cost $0.50 to $2 per order. Put both in and your margin is honest.</p>
<h3>Use the reverse mode before you buy inventory</h3>
<p>Switch to <em>Price to hit a profit</em>, enter the profit you need per sale, and the calculator finds the lowest list price that gets you there after fees. If that price is above what similar items actually sell for, don't buy the inventory. Pair it with the <a href="flip-calculator.html">flip ROI calculator</a> and our <a href="../guides/pricing-strategy.html">pricing guide</a>.</p>
<div class="notice"><strong>Fees change.</strong> Every rule shows the date we verified it and links to the platform's official fee page. Check that page before you make a big decision, and if you spot a change before we do, <a href="../contact.html?topic=Fee%20update">tell us</a>.</div>
</div><aside class="sidebar">{growth_cta()}<div class="tag-card"><h3>Not sure which platform?</h3><p style="margin-bottom:12px">Take the 60-second quiz to get your top three matches.</p><a class="btn small green" href="marketplace-match.html">Start the quiz</a></div></aside></div></section>"""
    page("tools/fee-calculator.html", "Marketplace fee & profit calculator (16 platforms)", "Free fee calculator for eBay, Etsy, Amazon, Poshmark, Mercari, Depop, Vinted, Facebook Marketplace and more. See fees, payout and real profit.",
         body, nav_key="tools", jsonld=[ld, tool_jsonld("Marketplace fee & profit calculator", "Calculate selling fees, payout and profit across 16 online marketplaces.", "fee-calculator.html")], scripts=SCRIPTS, priority="1.0")

    # Match quiz
    def step(name, q, opts, sub=None, extra=""):
        ch = "".join(f'<label class="choice"><input type="radio" name="{name}" value="{v}" data-label="{esc(l)}" required><span>{l}</span></label>' for v, l in opts)
        return f'<fieldset class="step" data-auto style="border:0;padding:0;margin:0"><legend class="lbl" style="font-family:var(--display);font-size:1.4rem;font-weight:650;margin-bottom:14px">{q}</legend>{"<p class=muted>" + sub + "</p>" if sub else ""}<div class="choices" data-need-one>{ch}</div>{extra}</fieldset>'
    nav = '<div class="step-acts"><button class="btn alt small" type="button" data-prev>Back</button></div>'
    steps = (step("cat", "What do you mostly want to sell?", PRODUCT_TYPES) +
             step("band", "What's a typical price for one item?", BANDS, extra=nav) +
             step("region", "Where are you selling from?", REGIONS, extra=nav) +
             step("delivery", "Will you ship, or sell locally?", DELIVERY, extra=nav) +
             step("effort", "How much effort can you put in?", EFFORT, extra=nav) +
             step("seller", "Which describes you best?", SELLER, extra='<div class="step-acts"><button class="btn alt small" type="button" data-prev>Back</button><button class="btn" type="submit">Show my matches</button></div>'))
    steps = steps.replace('<fieldset class="step" data-auto style="border:0;padding:0;margin:0"><legend class="lbl" style="font-family:var(--display);font-size:1.4rem;font-weight:650;margin-bottom:14px">Which describes you best?',
                          '<fieldset class="step" style="border:0;padding:0;margin:0"><legend class="lbl" style="font-family:var(--display);font-size:1.4rem;font-weight:650;margin-bottom:14px">Which describes you best?')
    h, ld = hero("Marketplace Match: where should you sell?", "Answer six quick questions. We score all 16 platforms in our profiles against what you sell, your price range, your country, local or shipped, how much effort you want to put in, and what kind of seller you are.", "Marketplace Match")
    body = h + f"""<section class="tight" style="padding-top:0"><div class="wrap layout-side"><div>
<div class="lead-box">
<form id="match-form" data-steps novalidate>
 <div class="steps-bar" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
 <p class="kbd-hint" data-step-label></p>
 {steps}
 {status()}
</form>
<div id="match-result" hidden aria-live="polite"></div>
</div>
<div class="prose" style="margin-top:36px">
<h2>How the match is scored</h2>
<p>Each platform has an editorial fit profile: the product types its buyers actively shop for, the price ranges that sell well, whether it supports local pickup, how much ongoing work it takes, and which kinds of sellers it suits. Your answers add or subtract points on each dimension. Availability in your country is weighted heavily, because a perfect platform you can't sell on is useless. Our reach, fee and ease scores break ties.</p>
<p>No platform pays to be ranked here, and the quiz has no affiliate links. If the result surprises you, read the profiles and run your numbers in the <a href="fee-calculator.html">fee calculator</a>. Most successful sellers end up on two or three platforms. The <a href="../guides/choose-the-right-marketplace.html">choosing a marketplace guide</a> explains how to cross-list without burning out.</p>
</div></div>
<aside class="sidebar">{growth_cta(title="Selling for a brand or at volume?", text="If you're moving serious inventory, a quiz is a starting point. The Growth Desk builds a channel plan around your margins, catalogue and goals, free.")}</aside></div></section>
{ad()}"""
    page("tools/marketplace-match.html", "Marketplace Match quiz: where should I sell?", "Answer 6 questions and get your top 3 best-fit online marketplaces (eBay, Etsy, Poshmark, Facebook Marketplace and more) with reasons.",
         body, nav_key="tools", jsonld=[ld, tool_jsonld("Marketplace Match quiz", "Find the best online marketplace for what you sell.", "marketplace-match.html")], scripts=SCRIPTS, priority="0.9")

    # Compare
    h, ld = hero("Compare marketplaces side by side", "Pick two or three platforms. You'll see fees, the payout on the same sample sale, our editorial scores for reach, cost, ease and buyer protection, and who each one suits. The URL updates, so you can share any comparison.", "Compare")
    body = h + f"""<section class="tight" style="padding-top:0"><div class="wrap" id="compare">
<div class="grid g3" style="margin-bottom:18px"><div><label class="lbl" for="c1">Platform 1</label><select id="c1"></select></div><div><label class="lbl" for="c2">Platform 2</label><select id="c2"></select></div><div><label class="lbl" for="c3">Platform 3 (optional)</label><select id="c3"></select></div></div>
<div class="table-scroll" id="compare-out"></div>
<p class="small muted" style="margin-top:12px">Scores are Market.Place editorial ratings out of 10, set the same way for every platform. See <a href="../about.html#methodology">methodology</a>. Payouts use fee rules verified on the dates shown in each profile.</p>
</div></section>
<section class="tight"><div class="wrap"><h2>Popular match-ups</h2><div class="ticker">
<a class="btn small alt" href="?p=ebay,mercari">eBay vs Mercari</a><a class="btn small alt" href="?p=poshmark,depop,vinted">Poshmark vs Depop vs Vinted</a><a class="btn small alt" href="?p=etsy,ebay">Etsy vs eBay</a><a class="btn small alt" href="?p=facebook-marketplace,offerup,craigslist">Facebook vs OfferUp vs Craigslist</a><a class="btn small alt" href="?p=amazon,walmart-marketplace">Amazon vs Walmart</a><a class="btn small alt" href="?p=stockx,ebay">StockX vs eBay</a><a class="btn small alt" href="?p=whatnot,tiktok-shop">Whatnot vs TikTok Shop</a><a class="btn small alt" href="?p=kijiji,facebook-marketplace">Kijiji vs Facebook</a>
</div></div></section>
{ad()}
<section class="tight"><div class="wrap">{growth_cta()}</div></section>"""
    page("tools/compare.html", "Compare online marketplaces side by side", "Compare eBay, Etsy, Amazon, Poshmark, Mercari, Depop, Vinted, Facebook Marketplace and more: fees, payout, reach, ease and buyer protection.",
         body, nav_key="tools", jsonld=[ld, tool_jsonld("Marketplace comparison tool", "Compare online marketplaces side by side.", "compare.html")], scripts=SCRIPTS, priority="0.9")

    # Flip calc
    h, ld = hero("Flip ROI calculator for resellers", "Before you buy anything to resell, check whether it's worth it. Enter the purchase price, your expected sale price and your costs. You get profit after platform fees, ROI and what you earn per hour of work.", "Flip ROI calculator")
    body = h + f"""<section class="tight" style="padding-top:0"><div class="wrap"><div class="tool-shell" id="flip">
<div class="panel"><div class="form">
 <div><label for="fl-platform">Where you'll sell it</label><select id="fl-platform"></select></div>
 <div class="row"><div><label for="fl-buy">Purchase price</label><input id="fl-buy" type="number" min="0" step="0.01" value="12"></div><div><label for="fl-sell">Expected sale price</label><input id="fl-sell" type="number" min="0" step="0.01" value="45"></div></div>
 <div class="row"><div><label for="fl-ship">Shipping you pay</label><input id="fl-ship" type="number" min="0" step="0.01" value="7.5"></div><div><label for="fl-sup">Cleaning &amp; supplies</label><input id="fl-sup" type="number" min="0" step="0.01" value="1.5"></div></div>
 <div class="row"><div><label for="fl-hours">Hours (source, clean, list, ship)</label><input id="fl-hours" type="number" min="0" step="0.25" value="1"></div><div><label for="fl-qty">Units in this lot</label><input id="fl-qty" type="number" min="1" step="1" value="1"></div></div>
</div></div>
<div class="panel" aria-live="polite"><span class="kicker">Profit per item</span><div class="result-big" id="fl-profit">$0</div>
<p id="fl-verdict" style="font-weight:700"></p>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px">
<div class="stat good"><b id="fl-roi">0%</b><span>Return on money invested</span></div><div class="stat"><b id="fl-hourly">$0</b><span>Effective hourly rate</span></div>
<div class="stat"><b id="fl-fees">$0</b><span>Platform fees</span></div><div class="stat"><b id="fl-batch">$0</b><span>Profit for the whole lot</span></div></div>
<p class="small muted" style="margin-top:14px">Assumes free shipping for the buyer (shipping cost comes out of your sale price). Promoted-listing ads, returns and unsold inventory aren't included. Budget for them.</p></div>
</div></div></section>
{ad()}
<section class="tight"><div class="wrap narrow prose"><h2>The three numbers that matter in a flip</h2>
<p><strong>ROI</strong> tells you how hard your money is working. Many full-time resellers aim to at least double their cost on low-priced items, because fees, returns and dead stock eat the difference. <strong>Effective hourly rate</strong> tells you whether you're running a business or just keeping busy. <strong>Lot profit</strong> matters when you buy in bulk: one great item can carry a box of duds, but only if you price the great one properly.</p>
<p>Use real sold prices, not asking prices, for your expected sale price. Our <a href="../guides/reselling-business.html">reselling business guide</a> walks through sourcing, comps and scaling, and the <a href="fee-calculator.html">fee calculator</a> shows every fee line for any platform.</p></div></section>"""
    page("tools/flip-calculator.html", "Flip ROI calculator for resellers", "Free reselling profit calculator: enter purchase price, sale price and costs to see profit after marketplace fees, ROI and hourly rate.",
         body, nav_key="tools", jsonld=[ld, tool_jsonld("Flip ROI calculator", "Reselling profit, ROI and hourly-rate calculator.", "flip-calculator.html")], scripts=SCRIPTS, priority="0.8")

    # Scam checker
    flags = [
        (3, "They want to pay or be paid outside the platform (Zelle, wire, crypto, \"friends & family\")"),
        (3, "They ask for gift cards, or for you to buy gift cards"),
        (3, "They send a link to a \"shipping\", \"escrow\" or \"payment confirmation\" site to log in or pay"),
        (3, "They \"accidentally\" overpaid and want the difference sent back"),
        (2, "They ask for a verification code sent to your phone"),
        (2, "Price is far below every comparable listing"),
        (2, "Seller refuses a video call, in-person inspection or extra photos"),
        (2, "Pressure to decide now (\"other buyers are waiting\", \"leaving the country\")"),
        (1, "Brand-new account, no reviews or ratings"),
        (1, "Stock photos or photos that appear elsewhere online"),
        (1, "Story keeps changing, or vague answers to specific questions"),
        (1, "Wants to ship to a different address than the one on the order"),
        (1, "Asks you to move the chat to WhatsApp, Telegram or email"),
        (2, "Asks you to mark the item as delivered or shipped before it is"),
    ]
    boxes = "".join(f'<label class="check" style="padding:10px 0;border-bottom:1px dashed var(--line-2)"><input type="checkbox" data-w="{w}"> <span>{esc(t)}</span></label>' for w, t in flags)
    h, ld = hero("Marketplace scam red-flag checker", "Buying or selling and something feels off? Tick every warning sign you're seeing. You'll get a risk level and the safest next step. Nothing you tick leaves your device.", "Scam checker", kicker="Safety tool")
    body = h + f"""<section class="tight" style="padding-top:0"><div class="wrap tool-shell" id="scam">
<div class="panel"><h2>What are you seeing?</h2>{boxes}</div>
<div class="panel" aria-live="polite"><span class="kicker">Risk level</span><h2 id="scam-verdict" style="font-size:1.7rem"></h2>
<div class="risk-meter" aria-hidden="true"><i id="scam-needle" style="left:0"></i></div>
<p id="scam-advice" style="font-weight:600"></p>
<h3 style="font-size:1.05rem;margin-top:20px">Rules that stop almost every scam</h3>
<ol><li>Keep messages and payment inside the platform, where purchase protection applies.</li><li>Never share a verification code, password or banking login.</li><li>Never pay with gift cards, wire transfers or crypto for marketplace items.</li><li>Meet in public, ideally a police-station exchange zone, for local deals.</li><li>Don't refund an "overpayment" until the original payment has fully cleared, and better still, cancel it.</li></ol>
<p><a class="link-arrow" href="../guides/avoid-buyer-scams.html">Buyer scam guide</a><br><a class="link-arrow" href="../guides/avoid-seller-scams.html">Seller scam guide</a><br><a class="link-arrow" href="../guides/safe-local-meetups.html">Safe local meetups</a></p>
<p class="small muted">Lost money already? Contact the platform and your bank or card issuer right away, then report it to your national fraud authority (for example ReportFraud.ftc.gov in the US or the Canadian Anti-Fraud Centre).</p></div>
</div></section>
{ad()}"""
    page("tools/scam-checker.html", "Online marketplace scam checker", "Is this marketplace listing or buyer a scam? Tick the red flags you see to get a risk score and the safest next step. Free, private, instant.",
         body, nav_key="tools", jsonld=[ld, tool_jsonld("Marketplace scam red-flag checker", "Score the scam risk of an online marketplace deal.", "scam-checker.html")], scripts=SCRIPTS, priority="0.8")
