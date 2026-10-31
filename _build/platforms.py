"""Editorial fit matrix used by Marketplace Match and Compare. Regions/scores come from profile front matter."""

PRODUCT_TYPES = [
    ("fashion", "Clothing & accessories"), ("sneakers", "Sneakers & streetwear"), ("handmade", "Handmade or craft"),
    ("vintage", "Vintage & antiques"), ("electronics", "Electronics & phones"), ("collectibles", "Collectibles, cards & toys"),
    ("home", "Home décor & household"), ("furniture", "Furniture & large items"), ("music", "Musical instruments & gear"),
    ("luxury", "Luxury & designer"), ("media", "Books, media & games"), ("general", "A bit of everything"),
]
BANDS = [("low", "Under $25"), ("mid", "$25 – $200"), ("high", "$200 – $1,000"), ("lux", "$1,000+")]
REGIONS = [("US", "United States"), ("Canada", "Canada"), ("UK", "United Kingdom"), ("Europe", "Europe (EU)"), ("Global", "Elsewhere / worldwide")]
DELIVERY = [("ship", "I'll ship it"), ("local", "Local pickup only"), ("either", "Either works")]
EFFORT = [("low", "Minimal: list it and forget it"), ("mid", "Moderate: a few hours a week"), ("high", "All-in: storefront, ads or live selling")]
SELLER = [("declutter", "Decluttering / occasional"), ("reseller", "Reseller or flipper"), ("brand", "Brand or business")]

FIT = {
    "amazon":               {"cats": ["electronics", "home", "media", "general", "collectibles"], "bands": ["low", "mid", "high"], "local": False, "ship": True, "effort": "high", "seller": ["brand", "reseller"]},
    "ebay":                 {"cats": ["electronics", "collectibles", "vintage", "media", "sneakers", "luxury", "music", "general", "fashion", "home"], "bands": ["low", "mid", "high", "lux"], "local": False, "ship": True, "effort": "mid", "seller": ["declutter", "reseller", "brand"]},
    "etsy":                 {"cats": ["handmade", "vintage", "home"], "bands": ["low", "mid", "high"], "local": False, "ship": True, "effort": "mid", "seller": ["brand", "reseller"]},
    "facebook-marketplace": {"cats": ["furniture", "home", "general", "electronics", "fashion", "collectibles", "media"], "bands": ["low", "mid", "high", "lux"], "local": True, "ship": True, "effort": "low", "seller": ["declutter", "reseller"]},
    "walmart-marketplace":  {"cats": ["general", "electronics", "home", "media"], "bands": ["low", "mid", "high"], "local": False, "ship": True, "effort": "high", "seller": ["brand"]},
    "mercari":              {"cats": ["general", "fashion", "collectibles", "electronics", "media", "home"], "bands": ["low", "mid"], "local": False, "ship": True, "effort": "low", "seller": ["declutter", "reseller"]},
    "poshmark":             {"cats": ["fashion", "luxury", "sneakers", "home"], "bands": ["low", "mid", "high", "lux"], "local": False, "ship": True, "effort": "mid", "seller": ["declutter", "reseller"]},
    "depop":                {"cats": ["fashion", "sneakers", "vintage"], "bands": ["low", "mid"], "local": False, "ship": True, "effort": "low", "seller": ["declutter", "reseller", "brand"]},
    "vinted":               {"cats": ["fashion", "sneakers", "vintage", "media", "home"], "bands": ["low", "mid"], "local": False, "ship": True, "effort": "low", "seller": ["declutter", "reseller"]},
    "offerup":              {"cats": ["furniture", "electronics", "general", "home"], "bands": ["low", "mid", "high", "lux"], "local": True, "ship": False, "effort": "low", "seller": ["declutter", "reseller"]},
    "craigslist":           {"cats": ["furniture", "general", "electronics", "music", "home"], "bands": ["mid", "high", "lux"], "local": True, "ship": False, "effort": "low", "seller": ["declutter"]},
    "kijiji":               {"cats": ["furniture", "general", "electronics", "home", "music"], "bands": ["low", "mid", "high", "lux"], "local": True, "ship": False, "effort": "low", "seller": ["declutter", "reseller"]},
    "reverb":               {"cats": ["music"], "bands": ["mid", "high", "lux"], "local": False, "ship": True, "effort": "mid", "seller": ["declutter", "reseller", "brand"]},
    "whatnot":              {"cats": ["collectibles", "sneakers", "fashion", "vintage", "luxury"], "bands": ["low", "mid", "high"], "local": False, "ship": True, "effort": "high", "seller": ["reseller", "brand"]},
    "tiktok-shop":          {"cats": ["fashion", "home", "general"], "bands": ["low", "mid"], "local": False, "ship": True, "effort": "high", "seller": ["brand", "reseller"]},
    "stockx":               {"cats": ["sneakers", "luxury", "collectibles", "electronics"], "bands": ["mid", "high", "lux"], "local": False, "ship": True, "effort": "low", "seller": ["reseller", "declutter"]},
}
ORDER = list(FIT.keys())
