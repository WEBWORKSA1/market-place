/* Market.Place site configuration.
   Payments: paste a PayPal donate link, Stripe Payment Link or Buy Me a Coffee URL to switch the
   Support page from "pledge" mode to instant checkout. Leave blank to keep pledge mode. */
window.SITE = {
  name: "Market.Place",
  domain: "market.place",
  adsenseClient: "ca-pub-6620975821265271",
  /* Optional: after AdSense approval, create display ad units and paste their slot IDs to show the in-content units.
     Auto ads (enabled in the AdSense dashboard) work without these. */
  adSlots: { inContent: "", display: "" },
  payments: {
    paypal: "",        // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX
    stripe: "",        // e.g. https://buy.stripe.com/XXXX
    buymeacoffee: ""   // e.g. https://www.buymeacoffee.com/yourname
  },
  /* Encoded keys — keep encoded. Never paste a plain address or owner URL anywhere on the site. */
  _k: ["MWFza3Jvd2Jldw==", "bW9jLmxpYW1n"],
  _o: "dGNhdG5vYy9za3Jvdy5iZXc="
};
