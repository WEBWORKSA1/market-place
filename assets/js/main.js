/* Market.Place — core interactions */
(function () {
  "use strict";
  var S = window.SITE || {};
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var dec = function (b) { try { return atob(b).split("").reverse().join(""); } catch (e) { return ""; } };

  /* Theme */
  var root = document.documentElement;
  var saved = store.get("mp-theme");
  if (saved) root.setAttribute("data-theme", saved);
  document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme");
      var dark = cur === "dark" || (!cur && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = dark ? "light" : "dark";
      root.setAttribute("data-theme", next); store.set("mp-theme", next);
    });
  });

  /* Mobile menu */
  var mb = document.querySelector(".menu-btn"), nav = document.getElementById("nav");
  if (mb && nav) mb.addEventListener("click", function () {
    var open = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", open);
  });

  /* Year */
  document.querySelectorAll("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });

  /* Owner link: destination assembled at click time, never present in markup */
  document.querySelectorAll("[data-owner]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var u = S._o ? "https://" + dec(S._o) : "";
      if (!u) return;
      e.preventDefault();
      var w = window.open(u, "_blank", "noopener");
      if (!w) location.href = u;
    });
  });

  /* Cookie notice */
  var c = document.getElementById("consent");
  if (c && !store.get("mp-consent")) {
    c.hidden = false;
    c.querySelectorAll("[data-consent]").forEach(function (b) {
      b.addEventListener("click", function () {
        store.set("mp-consent", b.getAttribute("data-consent"));
        if (b.getAttribute("data-consent") === "essential") {
          (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
        }
        c.hidden = true;
      });
    });
  }
  if (store.get("mp-consent") === "essential") {
    (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
  }

  /* Manual ad units: only rendered once ad-unit slot IDs are added to config.js (Auto ads work without them) */
  var slots = S.adSlots || {};
  document.querySelectorAll(".ad-slot[data-slot]").forEach(function (box) {
    var id = slots[box.getAttribute("data-slot")];
    if (!id) return;
    box.hidden = false;
    var ins = document.createElement("ins");
    ins.className = "adsbygoogle";
    ins.style.display = "block";
    ins.setAttribute("data-ad-client", S.adsenseClient);
    ins.setAttribute("data-ad-slot", id);
    ins.setAttribute("data-ad-format", "auto");
    ins.setAttribute("data-full-width-responsive", "true");
    box.appendChild(ins);
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });

  /* Relay endpoint (address assembled at runtime, never present in markup) */
  function relay() {
    var k = S._k || [];
    return "https://formsubmit.co/ajax/" + dec(k[0]) + String.fromCharCode(64) + dec(k[1]);
  }

  /* Multi-step forms */
  document.querySelectorAll("form[data-steps]").forEach(function (f) {
    var steps = f.querySelectorAll(".step"), bars = f.querySelectorAll(".steps-bar i"), i = 0;
    var label = f.querySelector("[data-step-label]");
    function show(n) {
      steps.forEach(function (s, j) { s.hidden = j !== n; });
      bars.forEach(function (b, j) { b.classList.toggle("on", j <= n); });
      if (label) label.textContent = "Step " + (n + 1) + " of " + steps.length;
      i = n;
      var first = steps[n].querySelector("input:not([type=hidden]),select,textarea");
      if (first && n > 0) first.focus({ preventScroll: true });
    }
    function valid() {
      var ok = true, st = f.querySelector(".form-status");
      steps[i].querySelectorAll("[required]").forEach(function (el) { if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; } });
      steps[i].querySelectorAll("[data-need-one]").forEach(function (g) {
        if (ok && !g.querySelector("input:checked")) { ok = false; if (st) { st.className = "form-status err"; st.textContent = "Pick an option to continue."; } }
      });
      if (ok && st) st.textContent = "";
      return ok;
    }
    f.querySelectorAll("[data-next]").forEach(function (b) { b.addEventListener("click", function () { if (valid()) show(i + 1); }); });
    f.querySelectorAll("[data-prev]").forEach(function (b) { b.addEventListener("click", function () { show(i - 1); }); });
    /* Auto-advance on single-choice radio steps */
    f.querySelectorAll(".step[data-auto] input[type=radio]").forEach(function (r) {
      r.addEventListener("change", function () { setTimeout(function () { if (valid() && i < steps.length - 1) show(i + 1); }, 180); });
    });
    f._showStep = show;
    show(0);
  });

  /* Prefill from query string (?track=launch etc.) */
  try {
    var qs = new URLSearchParams(location.search);
    qs.forEach(function (v, k) {
      document.querySelectorAll('form[data-form] [name="' + k + '"]').forEach(function (el) {
        if (el.type === "radio" || el.type === "checkbox") { if (el.value === v) el.checked = true; }
        else if (!el.value) el.value = v;
      });
    });
  } catch (e) {}

  /* All forms */
  document.querySelectorAll("form[data-form]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = f.querySelector(".form-status"), btn = f.querySelector("[type=submit]");
      var hpI = f.querySelector(".hp input");
      if (hpI && hpI.value) return;
      var data = {};
      new FormData(f).forEach(function (v, k) {
        if (k === "_hp") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "Market.Place — " + f.getAttribute("data-form") + (data.name ? " from " + data.name : "");
      data._template = "table"; data._captcha = "false";
      data.page = location.href;
      if (typeof f._extra === "function") Object.assign(data, f._extra());
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending…"; }
      if (status) { status.className = "form-status"; status.textContent = ""; }
      fetch(relay(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function () {
          var go = f.getAttribute("data-redirect");
          if (go) { location.href = go; return; }
          if (status) { status.className = "form-status ok"; status.textContent = f.getAttribute("data-ok") || "Sent. We reply within two business days."; }
          f.reset();
          if (f._showStep) f._showStep(0);
        })
        .catch(function () {
          if (status) { status.className = "form-status err"; status.textContent = "That didn't go through. Check your connection and try again, or use the contact page."; }
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* Lite YouTube embeds: nothing loads from YouTube until the visitor clicks */
  document.querySelectorAll("[data-yt]").forEach(function (b) {
    var id = b.getAttribute("data-yt");
    b.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "Video";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      var w = document.createElement("div"); w.className = "yt-wrap"; w.appendChild(f);
      b.replaceWith(w);
    });
  });

  /* Sortable tables */
  window.MP_sortable = function (table) {
    table.querySelectorAll("th[data-sort]").forEach(function (th, idx) {
      th.setAttribute("aria-sort", "none"); th.tabIndex = 0;
      function go() {
        var col = Array.prototype.indexOf.call(th.parentNode.children, th);
        var asc = th.getAttribute("aria-sort") !== "ascending";
        table.querySelectorAll("th[data-sort]").forEach(function (x) { x.setAttribute("aria-sort", "none"); });
        th.setAttribute("aria-sort", asc ? "ascending" : "descending");
        var tb = table.tBodies[0], rows = Array.prototype.slice.call(tb.rows);
        rows.sort(function (a, b) {
          var x = a.cells[col].getAttribute("data-v") || a.cells[col].textContent, y = b.cells[col].getAttribute("data-v") || b.cells[col].textContent;
          var nx = parseFloat(x), ny = parseFloat(y);
          var r = (!isNaN(nx) && !isNaN(ny)) ? nx - ny : x.localeCompare(y);
          return asc ? r : -r;
        });
        rows.forEach(function (r) { tb.appendChild(r); });
      }
      th.addEventListener("click", go);
      th.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); } });
    });
  };
  document.querySelectorAll("table.sortable").forEach(window.MP_sortable);

  /* Support page: tiers + payment links */
  var tiers = document.querySelectorAll(".tier");
  if (tiers.length) {
    var amt = document.getElementById("amount");
    tiers.forEach(function (t) {
      t.addEventListener("click", function () {
        tiers.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        t.setAttribute("aria-pressed", "true");
        if (amt) amt.value = t.getAttribute("data-amount");
      });
    });
    var p = S.payments || {}, box = document.getElementById("pay-links");
    if (box) {
      var links = [["paypal", "Give with PayPal"], ["stripe", "Give by card (Stripe)"], ["buymeacoffee", "Buy us a coffee"]];
      var any = false;
      links.forEach(function (l) {
        if (p[l[0]]) { any = true; var a = document.createElement("a"); a.href = p[l[0]]; a.className = "btn green"; a.target = "_blank"; a.rel = "noopener"; a.textContent = l[1]; box.appendChild(a); }
      });
      if (any) { var n = document.getElementById("pay-note"); if (n) n.hidden = false; }
    }
  }

  /* Reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { rootMargin: "0px 0px -40px 0px" });
    document.querySelectorAll(".reveal").forEach(function (n) { io.observe(n); });
  } else { document.querySelectorAll(".reveal").forEach(function (n) { n.classList.add("in"); }); }
})();
