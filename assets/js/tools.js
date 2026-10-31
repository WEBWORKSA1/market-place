/* Market.Place — interactive tools. Data: window.MP_DATA (assets/js/data.js) */
(function () {
  "use strict";
  var D = window.MP_DATA || { platforms: [] };
  var P = {}; D.platforms.forEach(function (p) { P[p.slug] = p; });
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var num = function (el) { var v = parseFloat(el && el.value); return isNaN(v) ? 0 : v; };
  function money(v, cur) {
    try { return new Intl.NumberFormat("en-US", { style: "currency", currency: cur || "USD", maximumFractionDigits: 2 }).format(v); }
    catch (e) { return "$" + v.toFixed(2); }
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var overrides = {}; // slug -> rules copy edited by the user

  function rulesFor(slug) { return overrides[slug] || (P[slug] && P[slug].fees && P[slug].fees.rules) || []; }
  function feeLines(slug, price, ship) {
    var out = [];
    rulesFor(slug).forEach(function (r) {
      var lo = r.min_price == null ? -Infinity : r.min_price, hi = r.max_price == null ? Infinity : r.max_price;
      if (price < lo || price >= hi) return;
      var base = r.base === "item_shipping" ? price + ship : price;
      var f = (r.pct || 0) / 100 * base + (r.fixed || 0);
      out.push({ label: r.label, amount: f });
    });
    return out;
  }
  function calc(slug, price, ship, shipCost, cost, other) {
    var lines = feeLines(slug, price, ship);
    var fees = lines.reduce(function (a, b) { return a + b.amount; }, 0);
    var revenue = price + ship, payout = revenue - fees, profit = payout - shipCost - cost - other;
    return { lines: lines, fees: fees, revenue: revenue, payout: payout, profit: profit, margin: revenue ? profit / revenue : 0, feePct: revenue ? fees / revenue : 0 };
  }
  window.MP_calc = calc;
  function solvePrice(slug, target, ship, shipCost, cost, other) {
    var lo = 0, hi = 1000000;
    for (var i = 0; i < 80; i++) { var mid = (lo + hi) / 2; if (calc(slug, mid, ship, shipCost, cost, other).profit < target) lo = mid; else hi = mid; }
    return Math.ceil(hi * 100) / 100;
  }
  function platformOptions(sel, def) {
    D.platforms.forEach(function (p) {
      if (!p.fees) return;
      var o = document.createElement("option"); o.value = p.slug; o.textContent = p.name; if (p.slug === def) o.selected = true; sel.appendChild(o);
    });
  }

  /* ---------------- Fee & profit calculator ---------------- */
  var fc = $("#fee-calc");
  if (fc) {
    var sel = $("#fc-platform"), mode = "profit";
    var qs = new URLSearchParams(location.search);
    platformOptions(sel, qs.get("p") || "ebay");
    ["price", "ship", "shipcost", "cost", "other", "target"].forEach(function (k) { if (qs.get(k) && $("#fc-" + k)) $("#fc-" + k).value = qs.get(k); });
    $$(".seg button", fc).forEach(function (b) {
      b.addEventListener("click", function () {
        mode = b.getAttribute("data-mode");
        $$(".seg button", fc).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        $("#fc-price-wrap").hidden = mode !== "profit"; $("#fc-target-wrap").hidden = mode !== "reverse";
        run();
      });
    });
    function renderRates() {
      var slug = sel.value, p = P[slug], box = $("#fc-rates");
      var rules = rulesFor(slug);
      var h = '<table class="data"><thead><tr><th>Fee rule</th><th class="num">%</th><th class="num">Fixed</th></tr></thead><tbody>';
      if (!rules.length) h += '<tr><td colspan="3">No seller fee rules on record for this platform.</td></tr>';
      rules.forEach(function (r, i) {
        var tier = (r.min_price != null || r.max_price != null) ? ' <span class="muted small">(' + (r.min_price != null ? "from " + r.min_price : "") + (r.max_price != null ? " under " + r.max_price : "") + ")</span>" : "";
        var base = r.base === "item_shipping" ? ' <span class="muted small">on item + shipping</span>' : "";
        h += "<tr><td>" + esc(r.label) + tier + base + '</td><td class="num"><input class="edit-rate" type="number" step="0.01" min="0" data-i="' + i + '" data-k="pct" value="' + (r.pct || 0) + '" aria-label="Percent for ' + esc(r.label) + '"></td><td class="num"><input class="edit-rate" type="number" step="0.01" min="0" data-i="' + i + '" data-k="fixed" value="' + (r.fixed || 0) + '" aria-label="Fixed amount for ' + esc(r.label) + '"></td></tr>';
      });
      h += "</tbody></table>";
      var f = p.fees || {};
      h += '<p class="small muted">' + esc(f.notes || "") + (f.monthly ? " Subscription: " + esc(f.monthly.label) + " " + money(f.monthly.amount, f.currency) + "/month (not included above)." : "") + '</p>';
      h += '<p class="small">Verified ' + esc(f.verified || "") + (f.source ? ' · <a href="' + esc(f.source) + '" target="_blank" rel="noopener nofollow">official fee page</a>' : "") + ' · <a href="profile.html" data-prof>' + esc(p.name) + ' profile</a> · <button type="button" class="btn small alt" id="fc-reset">Reset rates</button></p>';
      box.innerHTML = h;
      var pl = box.querySelector("[data-prof]"); if (pl) pl.href = "../marketplaces/" + slug + ".html";
      $$(".edit-rate", box).forEach(function (inp) {
        inp.addEventListener("input", function () {
          if (!overrides[slug]) overrides[slug] = JSON.parse(JSON.stringify(rulesFor(slug)));
          overrides[slug][+inp.getAttribute("data-i")][inp.getAttribute("data-k")] = parseFloat(inp.value) || 0;
          run(true);
        });
      });
      $("#fc-reset").addEventListener("click", function () { delete overrides[slug]; renderRates(); run(true); });
    }
    function run(skipRates) {
      var slug = sel.value, p = P[slug], cur = (p.fees && p.fees.currency) || "USD";
      if (!skipRates) renderRates();
      var ship = num($("#fc-ship")), shipCost = num($("#fc-shipcost")), cost = num($("#fc-cost")), other = num($("#fc-other"));
      var price = num($("#fc-price"));
      if (mode === "reverse") { price = solvePrice(slug, num($("#fc-target")), ship, shipCost, cost, other); }
      var r = calc(slug, price, ship, shipCost, cost, other);
      $("#fc-headline-label").textContent = mode === "reverse" ? "List it at" : "Your profit";
      var big = $("#fc-big");
      big.textContent = money(mode === "reverse" ? price : r.profit, cur);
      big.classList.toggle("neg", mode !== "reverse" && r.profit < 0);
      var li = '<li><span>Buyer pays (item + shipping)</span><b>' + money(r.revenue, cur) + "</b></li>";
      r.lines.forEach(function (l) { li += "<li><span>− " + esc(l.label) + "</span><b>" + money(l.amount, cur) + "</b></li>"; });
      li += '<li><span><strong>Platform payout</strong></span><b>' + money(r.payout, cur) + "</b></li>";
      li += "<li><span>− Your shipping cost</span><b>" + money(shipCost, cur) + "</b></li>";
      li += "<li><span>− Item cost</span><b>" + money(cost, cur) + "</b></li>";
      li += "<li><span>− Packaging &amp; other</span><b>" + money(other, cur) + "</b></li>";
      li += '<li><span><strong>Profit</strong></span><b>' + money(r.profit, cur) + "</b></li>";
      $("#fc-breakdown").innerHTML = li;
      $("#fc-feepct").textContent = (r.feePct * 100).toFixed(1) + "%";
      $("#fc-margin").textContent = (r.margin * 100).toFixed(1) + "%";
      $("#fc-fees").textContent = money(r.fees, cur);
      // compare all
      var rows = D.platforms.filter(function (x) { return x.fees; }).map(function (x) {
        var rr = calc(x.slug, price, ship, shipCost, cost, other); rr.p = x; return rr;
      });
      var best = rows.reduce(function (a, b) { return b.profit > a.profit ? b : a; }, rows[0]);
      var tb = "";
      rows.forEach(function (rr) {
        var c = rr.p.fees.currency || "USD";
        tb += '<tr class="' + (rr === best ? "best" : "") + (rr.p.slug === slug ? " cur" : "") + '"><td><a href="../marketplaces/' + rr.p.slug + '.html">' + esc(rr.p.name) + "</a>" + (c !== "USD" ? ' <span class="muted small">' + c + "</span>" : "") + '</td><td class="num" data-v="' + rr.fees.toFixed(4) + '">' + money(rr.fees, c) + '</td><td class="num" data-v="' + rr.feePct.toFixed(4) + '">' + (rr.feePct * 100).toFixed(1) + '%</td><td class="num" data-v="' + rr.payout.toFixed(4) + '">' + money(rr.payout, c) + '</td><td class="num" data-v="' + rr.profit.toFixed(4) + '">' + money(rr.profit, c) + "</td></tr>";
      });
      $("#fc-all tbody").innerHTML = tb;
      $("#fc-all-price").textContent = money(price, "USD").replace("US", "");
      // share link
      var q = new URLSearchParams({ p: slug, price: $("#fc-price").value, ship: $("#fc-ship").value, shipcost: $("#fc-shipcost").value, cost: $("#fc-cost").value, other: $("#fc-other").value });
      $("#fc-share").value = location.origin + location.pathname + "?" + q.toString();
    }
    sel.addEventListener("change", function () { run(); });
    $$("input", $("#fc-inputs")).forEach(function (i) { i.addEventListener("input", function () { run(true); }); });
    var cp = $("#fc-copy"); if (cp) cp.addEventListener("click", function () { var s = $("#fc-share"); s.select(); try { navigator.clipboard.writeText(s.value); cp.textContent = "Copied"; } catch (e) { document.execCommand("copy"); } setTimeout(function () { cp.textContent = "Copy link"; }, 1600); });
    if (window.MP_sortable) window.MP_sortable($("#fc-all"));
    run();
  }

  /* ---------------- Home mini calculator ---------------- */
  var mini = $("#mini-calc");
  if (mini) {
    var ms = $("#mc-platform"); platformOptions(ms, "etsy");
    function mrun() {
      var slug = ms.value, cur = (P[slug].fees && P[slug].fees.currency) || "USD";
      var r = calc(slug, num($("#mc-price")), num($("#mc-ship")), num($("#mc-ship")), num($("#mc-cost")), 0);
      $("#mc-fees").textContent = money(r.fees, cur); $("#mc-payout").textContent = money(r.payout - num($("#mc-ship")), cur);
      $("#mc-profit").textContent = money(r.profit, cur);
      $("#mc-link").href = "tools/fee-calculator.html?p=" + slug + "&price=" + num($("#mc-price")) + "&ship=" + num($("#mc-ship")) + "&shipcost=" + num($("#mc-ship")) + "&cost=" + num($("#mc-cost"));
    }
    ms.addEventListener("change", mrun); $$("input", mini).forEach(function (i) { i.addEventListener("input", mrun); }); mrun();
  }

  /* ---------------- Marketplace Match ---------------- */
  var mq = $("#match-form");
  if (mq) {
    function score(a) {
      return D.platforms.filter(function (p) { return p.fit; }).map(function (p) {
        var f = p.fit, s = 0, why = [];
        if (a.cat === "general") { if (f.cats.indexOf("general") > -1) { s += 5; why.push("Built for mixed, everyday items"); } else s += Math.min(3, f.cats.length / 3); }
        else if (f.cats.indexOf(a.cat) > -1) { s += 6; why.push("Strong buyer demand for " + a.catLabel.toLowerCase()); }
        else s -= 6;
        if (f.bands.indexOf(a.band) > -1) { s += 3; } else { s -= 4; why.push("Less suited to your price range"); }
        var regs = p.regions || [];
        if (regs.indexOf(a.region) > -1 || regs.indexOf("Global") > -1) { s += 3; why.push("Available to sellers in " + a.regionLabel); } else s -= 9;
        if (a.delivery === "local") { if (f.local) { s += 5; why.push("Local pickup is a core feature"); } else s -= 8; }
        else if (a.delivery === "ship") { if (f.ship) s += 2; else s -= 8; }
        else if (f.local) s += 1;
        var E = { low: 0, mid: 1, high: 2 };
        var gap = E[f.effort] - E[a.effort];
        if (gap <= 0) { s += 2; if (f.effort === "low") why.push("Quick to list with little upkeep"); }
        else s -= gap * 3;
        if (f.seller.indexOf(a.seller) > -1) s += 2;
        if (a.seller === "brand" && f.seller.indexOf("brand") > -1) why.push("Tools for brands and storefronts");
        var sc = p.scores || {};
        s += (sc.reach || 5) * 0.35 + (sc.fees || 5) * 0.25 + (sc.ease || 5) * 0.15;
        return { p: p, s: s, why: why.slice(0, 3) };
      }).sort(function (x, y) { return y.s - x.s; });
    }
    function show(a) {
      var res = score(a).slice(0, 3), box = $("#match-result");
      var max = res[0] ? res[0].s : 1;
      var h = '<h2>Your best-fit marketplaces</h2><p class="muted">Based on: ' + esc(a.catLabel) + " · " + esc(a.bandLabel) + " · " + esc(a.regionLabel) + "</p>";
      res.forEach(function (r, i) {
        var pct = Math.max(60, Math.min(98, Math.round(62 + 34 * Math.max(0, r.s) / max)));
        h += '<div class="result-card"><span class="rank">#' + (i + 1) + " match · " + pct + '% fit</span><h3 style="margin:.3em 0">' + esc(r.p.name) + '</h3><p>' + esc(r.p.best_for || "") + "</p><ul>" + r.why.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + '</ul><p class="small"><strong>Fees:</strong> ' + esc(r.p.fee_summary || "") + '</p><p style="margin:0"><a class="link-arrow" href="../marketplaces/' + r.p.slug + '.html">Read the ' + esc(r.p.name) + ' profile</a> &nbsp; <a class="link-arrow" href="fee-calculator.html?p=' + r.p.slug + '">Run the numbers</a></p></div>';
      });
      h += '<div class="tag-card" style="background:var(--saffron-soft);border:0;margin-top:16px"><h3>Want a human to check this?</h3><p style="margin-bottom:12px">The Growth Desk will review your products and send a free channel plan: where to list first, pricing, and what to cross-list.</p><a class="btn" href="../get-matched.html?track=sell&products=' + encodeURIComponent(a.catLabel) + '">Get my free channel plan</a></div>';
      h += '<p class="small" style="margin-top:12px"><button class="btn small alt" type="button" id="match-again">Retake the quiz</button> <button class="btn small alt" type="button" id="match-share">Copy result link</button></p>';
      box.innerHTML = h; box.hidden = false; mq.hidden = true;
      box.scrollIntoView({ behavior: "smooth", block: "start" });
      $("#match-again").addEventListener("click", function () { box.hidden = true; mq.hidden = false; mq.reset(); if (mq._showStep) mq._showStep(0); history.replaceState(null, "", location.pathname); });
      $("#match-share").addEventListener("click", function (e) { try { navigator.clipboard.writeText(location.href); e.target.textContent = "Link copied"; } catch (x) {} });
    }
    function answers(src) {
      var a = {};
      ["cat", "band", "region", "delivery", "effort", "seller"].forEach(function (k) {
        var v = src(k); a[k] = v;
        var lab = mq.querySelector('input[name="' + k + '"][value="' + v + '"]');
        a[k + "Label"] = lab ? lab.getAttribute("data-label") : v;
      });
      return a;
    }
    mq.addEventListener("submit", function (e) {
      e.preventDefault();
      var a = answers(function (k) { var c = mq.querySelector('input[name="' + k + '"]:checked'); return c ? c.value : ""; });
      if (!a.seller) { var st = mq.querySelector(".form-status"); st.className = "form-status err"; st.textContent = "Pick an option to see your results."; return; }
      history.replaceState(null, "", "#" + ["cat", "band", "region", "delivery", "effort", "seller"].map(function (k) { return a[k]; }).join("."));
      show(a);
    });
    if (location.hash.length > 3) {
      var parts = location.hash.slice(1).split("."), keys = ["cat", "band", "region", "delivery", "effort", "seller"];
      if (parts.length === 6) show(answers(function (k) { return parts[keys.indexOf(k)]; }));
    }
  }

  /* ---------------- Compare ---------------- */
  var cmp = $("#compare");
  if (cmp) {
    var sels = $$("select", cmp), qs2 = new URLSearchParams(location.search), defs = (qs2.get("p") || "ebay,etsy,mercari").split(",");
    sels.forEach(function (s, i) {
      if (i === 2) { var o = document.createElement("option"); o.value = ""; o.textContent = "(none)"; s.appendChild(o); }
      D.platforms.forEach(function (p) { var o = document.createElement("option"); o.value = p.slug; o.textContent = p.name; s.appendChild(o); });
      if (defs[i] && P[defs[i]]) s.value = defs[i];
      s.addEventListener("change", crun);
    });
    function bar(v) { return '<div class="bar" role="img" aria-label="' + v + ' out of 10"><i style="width:' + (v * 10) + '%"></i></div>'; }
    function crun() {
      var chosen = sels.map(function (s) { return P[s.value]; }).filter(Boolean);
      var rows = [
        ["Category", function (p) { return esc(p.category || ""); }],
        ["Regions", function (p) { return esc((p.regions || []).join(", ")); }],
        ["Best for", function (p) { return esc(p.best_for || ""); }],
        ["Seller fees", function (p) { return esc(p.fee_summary || ""); }],
        ["Payout on a $50 sale<br><span class='muted small'>$8 shipping charged, no costs</span>", function (p) { if (!p.fees) return "—"; var r = calc(p.slug, 50, 8, 0, 0, 0); return "<strong>" + money(r.payout, p.fees.currency) + "</strong> <span class='muted small'>(" + (r.feePct * 100).toFixed(1) + "% in fees)</span>"; }],
        ["Buyer reach", function (p) { return bar((p.scores || {}).reach || 0); }],
        ["Low fees", function (p) { return bar((p.scores || {}).fees || 0); }],
        ["Ease of selling", function (p) { return bar((p.scores || {}).ease || 0); }],
        ["Protection", function (p) { return bar((p.scores || {}).protection || 0); }],
        ["Local pickup", function (p) { return p.fit && p.fit.local ? "Yes" : "No"; }],
        ["", function (p) { return '<a class="btn small alt" href="../marketplaces/' + p.slug + '.html">Full profile</a>'; }]
      ];
      var h = '<table class="data"><thead><tr><th></th>' + chosen.map(function (p) { return "<th>" + esc(p.name) + "</th>"; }).join("") + "</tr></thead><tbody>";
      rows.forEach(function (r) { h += "<tr><th scope='row'>" + r[0] + "</th>" + chosen.map(function (p) { return "<td>" + r[1](p) + "</td>"; }).join("") + "</tr>"; });
      $("#compare-out").innerHTML = h + "</tbody></table>";
      history.replaceState(null, "", "?p=" + chosen.map(function (p) { return p.slug; }).join(","));
    }
    crun();
  }

  /* ---------------- Flip ROI ---------------- */
  var fl = $("#flip");
  if (fl) {
    var fs = $("#fl-platform"); platformOptions(fs, "ebay");
    function frun() {
      var slug = fs.value, cur = (P[slug].fees && P[slug].fees.currency) || "USD";
      var buy = num($("#fl-buy")), sell = num($("#fl-sell")), ship = num($("#fl-ship")), sup = num($("#fl-sup")), hrs = num($("#fl-hours")), qty = Math.max(1, num($("#fl-qty")));
      var r = calc(slug, sell, 0, ship, buy, sup);
      var invest = buy + ship + sup;
      $("#fl-profit").textContent = money(r.profit, cur);
      $("#fl-profit").classList.toggle("neg", r.profit < 0);
      $("#fl-roi").textContent = invest ? (r.profit / invest * 100).toFixed(0) + "%" : "—";
      $("#fl-hourly").textContent = hrs ? money(r.profit / hrs, cur) + "/h" : "—";
      $("#fl-fees").textContent = money(r.fees, cur);
      $("#fl-batch").textContent = money(r.profit * qty, cur);
      $("#fl-verdict").textContent = r.profit <= 0 ? "Pass. This flip loses money after fees." : (invest && r.profit / invest < 0.3) ? "Thin. Under 30% ROI leaves little room for returns or slow sales." : (hrs && r.profit / hrs < 15) ? "Profitable, but your time is cheap here. Batch the work or raise the price." : "Strong flip. Buy it.";
    }
    fs.addEventListener("change", frun); $$("input", fl).forEach(function (i) { i.addEventListener("input", frun); }); frun();
  }

  /* ---------------- Scam checker ---------------- */
  var sc = $("#scam");
  if (sc) {
    function srun() {
      var tot = 0, max = 0;
      $$("input[type=checkbox]", sc).forEach(function (c) { var w = +c.getAttribute("data-w"); max += w; if (c.checked) tot += w; });
      var pct = Math.min(100, Math.round(tot / 12 * 100));
      $("#scam-needle").style.left = "calc(" + pct + "% - 2px)";
      var v = $("#scam-verdict"), adv = $("#scam-advice");
      if (tot === 0) { v.textContent = "No red flags ticked yet"; adv.textContent = "Tick everything that applies to the listing or conversation."; }
      else if (tot < 4) { v.textContent = "Low risk, stay alert"; adv.textContent = "Keep every message and payment inside the platform, and inspect before you pay."; }
      else if (tot < 8) { v.textContent = "High risk: slow down"; adv.textContent = "Several classic scam signals. Don't send money or items until each one is resolved inside the platform."; }
      else { v.textContent = "Very likely a scam. Walk away"; adv.textContent = "Stop replying, report the listing or account to the platform, and never pay by gift card, wire or crypto."; }
    }
    $$("input", sc).forEach(function (c) { c.addEventListener("change", srun); }); srun();
  }

  /* ---------------- Directory ---------------- */
  var dir = $("#dir");
  if (dir && window.MP_DIR) {
    var q = $("#dir-q"), cat = $("#dir-cat"), reg = $("#dir-reg"), mod = $("#dir-model"), grid = $("#dir-grid");
    var cats = {}, regs = {}, mods = {};
    window.MP_DIR.forEach(function (d) { cats[d.category] = 1; (d.regions || []).forEach(function (r) { regs[r] = 1; }); mods[d.model] = 1; });
    function fill(s, o) { Object.keys(o).sort().forEach(function (k) { var e = document.createElement("option"); e.value = k; e.textContent = k; s.appendChild(e); }); }
    fill(cat, cats); fill(reg, regs); fill(mod, mods);
    var qp = new URLSearchParams(location.search); if (qp.get("cat")) cat.value = qp.get("cat");
    function drun() {
      var t = q.value.trim().toLowerCase(), n = 0, h = "";
      window.MP_DIR.forEach(function (d) {
        if (cat.value && d.category !== cat.value) return;
        if (reg.value && (d.regions || []).indexOf(reg.value) < 0) return;
        if (mod.value && d.model !== mod.value) return;
        if (t && (d.name + " " + d.best_for + " " + d.category).toLowerCase().indexOf(t) < 0) return;
        n++;
        var prof = P[d.slug] ? '<a class="link-arrow small" href="' + d.slug + '.html">Our full profile</a>' : "";
        h += '<article class="tag-card hole dir-card"><h3>' + esc(d.name) + '</h3><span class="pill">' + esc(d.category) + '</span><span class="pill saffron">' + esc(d.model) + '</span><p style="margin-top:6px">' + esc(d.best_for) + '</p><p class="small muted" style="margin:8px 0 0">Regions: ' + esc((d.regions || []).join(", ")) + '</p><p class="fee"><strong>Seller fees:</strong> ' + esc(d.seller_fees) + '</p><p class="small" style="margin:8px 0 0"><a href="' + esc(d.url) + '" target="_blank" rel="noopener nofollow">Visit site ↗</a> ' + prof + "</p></article>";
      });
      grid.innerHTML = h || '<p>No marketplaces match those filters. Try clearing one.</p>';
      $("#dir-count").textContent = n;
    }
    [q, cat, reg, mod].forEach(function (e) { e.addEventListener("input", drun); });
    $("#dir-clear").addEventListener("click", function () { q.value = ""; cat.value = ""; reg.value = ""; mod.value = ""; drun(); });
    drun();
  }
})();
