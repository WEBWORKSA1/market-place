window.MP_DATA={
 "platforms": [
  {
   "slug": "amazon",
   "name": "Amazon",
   "url": "https://sell.amazon.com",
   "category": "General Retail",
   "best_for": "Brands and resellers with steady inventory who want maximum buyer traffic",
   "fee_summary": "15% referral fee in most categories plus $39.99/month on the Professional plan",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 10,
    "fees": 4,
    "ease": 4,
    "protection": 7
   },
   "fit": {
    "cats": [
     "electronics",
     "home",
     "media",
     "general",
     "collectibles"
    ],
    "bands": [
     "low",
     "mid",
     "high"
    ],
    "local": false,
    "ship": true,
    "effort": "high",
    "seller": [
     "brand",
     "reseller"
    ]
   },
   "fees": {
    "slug": "amazon",
    "name": "Amazon",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://sell.amazon.com/pricing",
    "rules": [
     {
      "label": "Referral fee minimum (most categories)",
      "pct": 0,
      "fixed": 0.3,
      "base": "item_shipping",
      "max_price": 2
     },
     {
      "label": "Referral fee (most categories)",
      "pct": 15,
      "fixed": 0,
      "base": "item_shipping",
      "min_price": 2
     }
    ],
    "monthly": {
     "label": "Professional plan",
     "amount": 39.99
    },
    "notes": "15% covers most categories (8% computers/electronics, tiered apparel/beauty); $0.30 min. Media adds $1.80 closing fee. FBA and ad costs excluded. Individual plan: $0.99/item."
   }
  },
  {
   "slug": "ebay",
   "name": "eBay",
   "url": "https://www.ebay.com",
   "category": "General & Collectibles",
   "best_for": "Resellers, collectors and anyone selling used, rare or niche items nationwide",
   "fee_summary": "13.6% final value fee (most categories) + $0.30–$0.40 per order",
   "regions": [
    "Global",
    "US"
   ],
   "scores": {
    "reach": 9,
    "fees": 6,
    "ease": 7,
    "protection": 8
   },
   "fit": {
    "cats": [
     "electronics",
     "collectibles",
     "vintage",
     "media",
     "sneakers",
     "luxury",
     "music",
     "general",
     "fashion",
     "home"
    ],
    "bands": [
     "low",
     "mid",
     "high",
     "lux"
    ],
    "local": false,
    "ship": true,
    "effort": "mid",
    "seller": [
     "declutter",
     "reseller",
     "brand"
    ]
   },
   "fees": {
    "slug": "ebay",
    "name": "eBay",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4364",
    "rules": [
     {
      "label": "Final value fee (most categories)",
      "pct": 13.6,
      "fixed": 0,
      "base": "item_shipping",
      "max_price": 7500
     },
     {
      "label": "Final value fee, sale over $7,500 (13.6% to $7,500 + 2.35% above)",
      "pct": 2.35,
      "fixed": 843.75,
      "base": "item_shipping",
      "min_price": 7500
     },
     {
      "label": "Per-order fee (order $10 or less)",
      "pct": 0,
      "fixed": 0.3,
      "base": "item",
      "max_price": 10.01
     },
     {
      "label": "Per-order fee (order over $10)",
      "pct": 0,
      "fixed": 0.4,
      "base": "item",
      "min_price": 10.01
     }
    ],
    "notes": "Most-categories rate; others vary. eBay also charges FVF on sales tax (not modeled). 250 free listings/month, then $0.35 each. Store plans and promoted listings extra."
   }
  },
  {
   "slug": "etsy",
   "name": "Etsy",
   "url": "https://www.etsy.com",
   "category": "Handmade & Vintage",
   "best_for": "Makers, vintage dealers and craft-supply sellers who want buyers looking for unique goods",
   "fee_summary": "$0.20 listing + 6.5% transaction + 3% + $0.25 payment processing (US)",
   "regions": [
    "Global"
   ],
   "scores": {
    "reach": 8,
    "fees": 7,
    "ease": 7,
    "protection": 7
   },
   "fit": {
    "cats": [
     "handmade",
     "vintage",
     "home"
    ],
    "bands": [
     "low",
     "mid",
     "high"
    ],
    "local": false,
    "ship": true,
    "effort": "mid",
    "seller": [
     "brand",
     "reseller"
    ]
   },
   "fees": {
    "slug": "etsy",
    "name": "Etsy",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://www.etsy.com/legal/fees/",
    "rules": [
     {
      "label": "Listing fee",
      "pct": 0,
      "fixed": 0.2,
      "base": "item"
     },
     {
      "label": "Transaction fee",
      "pct": 6.5,
      "fixed": 0,
      "base": "item_shipping"
     },
     {
      "label": "Payment processing (US)",
      "pct": 3,
      "fixed": 0.25,
      "base": "item_shipping"
     }
    ],
    "notes": "US Etsy Payments rate 3% + $0.25 (also charged on tax). Offsite Ads fee of 15% (12% for $10k+ shops, $100 cap) applies only to ad-attributed orders; not modeled."
   }
  },
  {
   "slug": "facebook-marketplace",
   "name": "Facebook Marketplace",
   "url": "https://www.facebook.com/marketplace",
   "category": "Local & Social Classifieds",
   "best_for": "Local sellers of furniture, household goods and bulky items, plus casual shippers",
   "fee_summary": "Free for local pickup; 10% (minimum $0.80) on shipped orders",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 9,
    "fees": 7,
    "ease": 9,
    "protection": 5
   },
   "fit": {
    "cats": [
     "furniture",
     "home",
     "general",
     "electronics",
     "fashion",
     "collectibles",
     "media"
    ],
    "bands": [
     "low",
     "mid",
     "high",
     "lux"
    ],
    "local": true,
    "ship": true,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "facebook-marketplace",
    "name": "Facebook Marketplace",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://www.facebook.com/business/help/223030991929920",
    "rules": [
     {
      "label": "Selling fee, flat (shipment $8 or less)",
      "pct": 0,
      "fixed": 0.8,
      "base": "item",
      "max_price": 8.01
     },
     {
      "label": "Selling fee (shipped orders)",
      "pct": 10,
      "fixed": 0,
      "base": "item_shipping",
      "min_price": 8.01
     }
    ],
    "notes": "Shipped orders only: 10% or $0.80 minimum. Local pickup with cash/P2P is free. Official page blocks automated reading; rate cross-checked with Sept 2026 third-party guides."
   }
  },
  {
   "slug": "walmart-marketplace",
   "name": "Walmart Marketplace",
   "url": "https://marketplace.walmart.com",
   "category": "General Retail",
   "best_for": "Established brands and resellers with reliable inventory and fulfillment",
   "fee_summary": "15% referral fee in most categories; no setup or monthly fees",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 7,
    "fees": 5,
    "ease": 3,
    "protection": 7
   },
   "fit": {
    "cats": [
     "general",
     "electronics",
     "home",
     "media"
    ],
    "bands": [
     "low",
     "mid",
     "high"
    ],
    "local": false,
    "ship": true,
    "effort": "high",
    "seller": [
     "brand"
    ]
   },
   "fees": {
    "slug": "walmart-marketplace",
    "name": "Walmart Marketplace",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://marketplace.walmart.com/referral-fees/",
    "rules": [
     {
      "label": "Referral fee (Everything Else)",
      "pct": 15,
      "fixed": 0,
      "base": "item_shipping"
     }
    ],
    "notes": "No setup or monthly fee. 15% default; tiered rates in apparel, beauty, grocery, jewelry, furniture, electronics accessories, watches. WFS fulfillment fees excluded."
   }
  },
  {
   "slug": "mercari",
   "name": "Mercari",
   "url": "https://www.mercari.com",
   "category": "General Resale",
   "best_for": "Casual sellers and resellers shipping everyday items, collectibles and electronics",
   "fee_summary": "Flat 10% selling fee on item + shipping; buyers pay a 3.6% protection fee",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 6,
    "fees": 7,
    "ease": 9,
    "protection": 7
   },
   "fit": {
    "cats": [
     "general",
     "fashion",
     "collectibles",
     "electronics",
     "media",
     "home"
    ],
    "bands": [
     "low",
     "mid"
    ],
    "local": false,
    "ship": true,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "mercari",
    "name": "Mercari",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://www.mercari.com/us/help_center/article/2517/",
    "rules": [
     {
      "label": "Selling fee",
      "pct": 10,
      "fixed": 0,
      "base": "item_shipping"
     }
    ],
    "notes": "Flat 10% on item + buyer-paid shipping; no separate processing fee. Buyers pay a 3.6% protection fee. Standard payout free; Instant Pay $3. Some sellers offered tier discounts."
   }
  },
  {
   "slug": "poshmark",
   "name": "Poshmark",
   "url": "https://poshmark.com",
   "category": "Fashion Resale",
   "best_for": "Closet cleaners and fashion resellers who enjoy community-driven selling",
   "fee_summary": "$2.95 flat on sales $15 and under; 20% on sales over $15",
   "regions": [
    "Canada",
    "US"
   ],
   "scores": {
    "reach": 6,
    "fees": 3,
    "ease": 8,
    "protection": 7
   },
   "fit": {
    "cats": [
     "fashion",
     "luxury",
     "sneakers",
     "home"
    ],
    "bands": [
     "low",
     "mid",
     "high",
     "lux"
    ],
    "local": false,
    "ship": true,
    "effort": "mid",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "poshmark",
    "name": "Poshmark",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://poshmark.com/fee_policy",
    "rules": [
     {
      "label": "Flat fee (sale $15 and under)",
      "pct": 0,
      "fixed": 2.95,
      "base": "item",
      "max_price": 15.01
     },
     {
      "label": "Commission (sale over $15)",
      "pct": 20,
      "fixed": 0,
      "base": "item",
      "min_price": 15.01
     }
    ],
    "notes": "US rates reverted Oct 24, 2024; buyer protection fee removed. Buyer pays the shipping label; discounted shipping you offer comes out of earnings. Canada differs."
   }
  },
  {
   "slug": "depop",
   "name": "Depop",
   "url": "https://www.depop.com",
   "category": "Fashion Resale",
   "best_for": "Vintage, streetwear and Y2K sellers targeting style-conscious, younger buyers",
   "fee_summary": "No US selling fee; payment processing 3.3% + $0.45 per sale",
   "regions": [
    "UK",
    "US"
   ],
   "scores": {
    "reach": 5,
    "fees": 9,
    "ease": 8,
    "protection": 6
   },
   "fit": {
    "cats": [
     "fashion",
     "sneakers",
     "vintage"
    ],
    "bands": [
     "low",
     "mid"
    ],
    "local": false,
    "ship": true,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller",
     "brand"
    ]
   },
   "fees": {
    "slug": "depop",
    "name": "Depop",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://depophelp.zendesk.com/hc/en-gb/articles/360001791127-Seller-fees-and-charges",
    "rules": [
     {
      "label": "Payment processing (Depop Payments)",
      "pct": 3.3,
      "fixed": 0.45,
      "base": "item_shipping"
     }
    ],
    "notes": "No selling fee for US sellers (since July 2024). Processing also applies to tax. Optional Boost costs 12% on boosted sales. Buyers pay a marketplace fee at checkout."
   }
  },
  {
   "slug": "vinted",
   "name": "Vinted",
   "url": "https://www.vinted.com",
   "category": "Fashion Resale",
   "best_for": "Everyday clothing sellers who want zero seller fees and quick, low-effort sales",
   "fee_summary": "No seller fees; buyers pay about 5% + €0.70 (US: 5% + $0.70) at checkout",
   "regions": [
    "Europe",
    "UK"
   ],
   "scores": {
    "reach": 7,
    "fees": 10,
    "ease": 8,
    "protection": 7
   },
   "fit": {
    "cats": [
     "fashion",
     "sneakers",
     "vintage",
     "media",
     "home"
    ],
    "bands": [
     "low",
     "mid"
    ],
    "local": false,
    "ship": true,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "vinted",
    "name": "Vinted",
    "currency": "EUR",
    "verified": "2026-10",
    "source": "https://www.vinted.ie/pricelist",
    "rules": [],
    "notes": "Sellers pay no listing or selling fee. Buyers pay a Vinted fee, usually 5% + €0.70 (US site: 5% + $0.70), plus shipping. Bumps and spotlight promos are optional paid extras."
   }
  },
  {
   "slug": "offerup",
   "name": "OfferUp",
   "url": "https://offerup.com",
   "category": "Local Classifieds",
   "best_for": "Local sellers of furniture, electronics, tools and vehicles who meet buyers in person",
   "fee_summary": "No fees on in-person sales; local-only since nationwide shipping ended in 2025",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 5,
    "fees": 10,
    "ease": 9,
    "protection": 3
   },
   "fit": {
    "cats": [
     "furniture",
     "electronics",
     "general",
     "home"
    ],
    "bands": [
     "low",
     "mid",
     "high",
     "lux"
    ],
    "local": true,
    "ship": false,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "offerup",
    "name": "OfferUp",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://help.offerup.com/hc/en-us/articles/360031989092-What-is-OfferUp",
    "rules": [],
    "notes": "No fees on in-person sales. Nationwide shipping was retired Sept-Oct 2025, so listings are local only. Paid extras: promotions, posts beyond free allotment, job/service ads."
   }
  },
  {
   "slug": "craigslist",
   "name": "Craigslist",
   "url": "https://www.craigslist.org",
   "category": "Local Classifieds",
   "best_for": "Local sales of furniture, appliances, tools and vehicles without any commission",
   "fee_summary": "Free for most by-owner posts; $5 for US vehicle-by-owner and dealer posts",
   "regions": [
    "Global",
    "US"
   ],
   "scores": {
    "reach": 6,
    "fees": 10,
    "ease": 7,
    "protection": 2
   },
   "fit": {
    "cats": [
     "furniture",
     "general",
     "electronics",
     "music",
     "home"
    ],
    "bands": [
     "mid",
     "high",
     "lux"
    ],
    "local": true,
    "ship": false,
    "effort": "low",
    "seller": [
     "declutter"
    ]
   },
   "fees": {
    "slug": "craigslist",
    "name": "Craigslist",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://www.craigslist.org/about/help/posting_fees",
    "rules": [],
    "notes": "Most by-owner for-sale posts are free; no commission. US posts cost $5 for cars/trucks, RVs and motorcycles by owner, and for all by-dealer for-sale categories."
   }
  },
  {
   "slug": "kijiji",
   "name": "Kijiji",
   "url": "https://www.kijiji.ca",
   "category": "Local Classifieds",
   "best_for": "Canadians selling furniture, electronics, vehicles and household goods locally",
   "fee_summary": "No commission; most private Buy & Sell ads free, some categories charge listing fees",
   "regions": [
    "Canada"
   ],
   "scores": {
    "reach": 6,
    "fees": 10,
    "ease": 8,
    "protection": 2
   },
   "fit": {
    "cats": [
     "furniture",
     "general",
     "electronics",
     "home",
     "music"
    ],
    "bands": [
     "low",
     "mid",
     "high",
     "lux"
    ],
    "local": true,
    "ship": false,
    "effort": "low",
    "seller": [
     "declutter",
     "reseller"
    ]
   },
   "fees": {
    "slug": "kijiji",
    "name": "Kijiji",
    "currency": "CAD",
    "verified": "2026-10",
    "source": "https://community.kijiji.ca/t/category-pricing-overview-listing-fees/141",
    "rules": [],
    "notes": "No commission on sales. Most private Buy & Sell ads free; some categories (vehicles past free limit, tickets, services, pets, real estate) charge per-31-day listing fees."
   }
  },
  {
   "slug": "reverb",
   "name": "Reverb",
   "url": "https://reverb.com",
   "category": "Music Gear",
   "best_for": "Musicians, gear collectors and music shops selling instruments and audio equipment",
   "fee_summary": "5% selling fee + 3.19% + $0.49 payment processing (US)",
   "regions": [
    "Global"
   ],
   "scores": {
    "reach": 5,
    "fees": 8,
    "ease": 7,
    "protection": 8
   },
   "fit": {
    "cats": [
     "music"
    ],
    "bands": [
     "mid",
     "high",
     "lux"
    ],
    "local": false,
    "ship": true,
    "effort": "mid",
    "seller": [
     "declutter",
     "reseller",
     "brand"
    ]
   },
   "fees": {
    "slug": "reverb",
    "name": "Reverb",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://reverb.com/legal/reverbs-billing-policy",
    "rules": [
     {
      "label": "Selling fee minimum",
      "pct": 0,
      "fixed": 0.5,
      "base": "item",
      "max_price": 10
     },
     {
      "label": "Selling fee",
      "pct": 5,
      "fixed": 0,
      "base": "item_shipping",
      "min_price": 10,
      "max_price": 10000
     },
     {
      "label": "Selling fee cap",
      "pct": 0,
      "fixed": 500,
      "base": "item",
      "min_price": 10000
     },
     {
      "label": "Payment processing (US, Reverb Payments)",
      "pct": 3.19,
      "fixed": 0.49,
      "base": "item_shipping"
     }
    ],
    "notes": "5% selling fee on item + shipping ($0.50 min, $500 max). Preferred Sellers pay 2.99% + $0.49 processing. No listing fees. Bumps and currency conversion extra."
   }
  },
  {
   "slug": "whatnot",
   "name": "Whatnot",
   "url": "https://www.whatnot.com",
   "category": "Live Shopping & Collectibles",
   "best_for": "Collectible, card and fashion sellers comfortable selling on camera",
   "fee_summary": "8% commission + 2.9% + $0.30 payment processing on order total",
   "regions": [
    "Europe",
    "UK",
    "US"
   ],
   "scores": {
    "reach": 5,
    "fees": 7,
    "ease": 5,
    "protection": 7
   },
   "fit": {
    "cats": [
     "collectibles",
     "sneakers",
     "fashion",
     "vintage",
     "luxury"
    ],
    "bands": [
     "low",
     "mid",
     "high"
    ],
    "local": false,
    "ship": true,
    "effort": "high",
    "seller": [
     "reseller",
     "brand"
    ]
   },
   "fees": {
    "slug": "whatnot",
    "name": "Whatnot",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://help.whatnot.com/hc/en-us/articles/4847069165965-Whatnot-seller-fees",
    "rules": [
     {
      "label": "Commission (most categories)",
      "pct": 8,
      "fixed": 0,
      "base": "item"
     },
     {
      "label": "Payment processing",
      "pct": 2.9,
      "fixed": 0.3,
      "base": "item_shipping"
     }
    ],
    "notes": "8% on sale price (Coins & Money 4%); some collectibles pay 0% above $1,500 for a limited time. Processing also applies to buyer-paid tax. No listing fees."
   }
  },
  {
   "slug": "tiktok-shop",
   "name": "TikTok Shop",
   "url": "https://shop.tiktok.com",
   "category": "Social Commerce",
   "best_for": "Brands and resellers with video-friendly products and a plan to work with creators",
   "fee_summary": "6% referral fee in most categories (official table); affiliate commissions extra",
   "regions": [
    "US"
   ],
   "scores": {
    "reach": 8,
    "fees": 8,
    "ease": 4,
    "protection": 7
   },
   "fit": {
    "cats": [
     "fashion",
     "home",
     "general"
    ],
    "bands": [
     "low",
     "mid"
    ],
    "local": false,
    "ship": true,
    "effort": "high",
    "seller": [
     "brand",
     "reseller"
    ]
   },
   "fees": {
    "slug": "tiktok-shop",
    "name": "TikTok Shop",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://seller-us.tiktok.com/university/essay?knowledge_id=5988482086864682",
    "rules": [
     {
      "label": "Referral fee (most categories)",
      "pct": 6,
      "fixed": 0,
      "base": "item_shipping"
     }
    ],
    "notes": "Official table: 6% most categories, 5% some jewelry/pre-owned; tax excluded. Some 2026 reports cite 8%; confirm in Seller Center. Affiliate commissions excluded."
   }
  },
  {
   "slug": "stockx",
   "name": "StockX",
   "url": "https://stockx.com",
   "category": "Sneakers & Collectibles",
   "best_for": "Sneaker and streetwear resellers selling new, in-demand items at market price",
   "fee_summary": "9% transaction fee (Level 1) + 3% processing; $5 minimum seller fee",
   "regions": [
    "Global"
   ],
   "scores": {
    "reach": 5,
    "fees": 6,
    "ease": 7,
    "protection": 9
   },
   "fit": {
    "cats": [
     "sneakers",
     "luxury",
     "collectibles",
     "electronics"
    ],
    "bands": [
     "mid",
     "high",
     "lux"
    ],
    "local": false,
    "ship": true,
    "effort": "low",
    "seller": [
     "reseller",
     "declutter"
    ]
   },
   "fees": {
    "slug": "stockx",
    "name": "StockX",
    "currency": "USD",
    "verified": "2026-10",
    "source": "https://stockx.com/help/articles/what-are-stockxs-fees-for-sellers",
    "rules": [
     {
      "label": "Transaction fee minimum (Level 1)",
      "pct": 0,
      "fixed": 5,
      "base": "item",
      "max_price": 55.56
     },
     {
      "label": "Transaction fee (Level 1)",
      "pct": 9,
      "fixed": 0,
      "base": "item",
      "min_price": 55.56
     },
     {
      "label": "Payment processing",
      "pct": 3,
      "fixed": 0,
      "base": "item"
     }
    ],
    "notes": "Level 1 rate; drops to 7% at Level 5 with volume. $5 US minimum seller fee (modeled on the transaction fee). Covers the Verified (authenticated) channel only."
   }
  }
 ]
};
