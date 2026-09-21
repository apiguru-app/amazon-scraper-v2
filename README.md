<div align="center">
  <a href="https://dash.apiguru.app/landing">
    <img src="https://raw.githubusercontent.com/apiguru-app/amazon-scraper-v2/refs/heads/main/service_logo_github.png" alt="apiGURU Amazon Scraper API Logo"/>
  </a>
  <p>
    <a href="https://agent.apiguru.app/llms.txt"><img src="https://img.shields.io/badge/agent--ready-llms.txt-7c3aed" alt="agent-ready: llms.txt"></a>
    <a href="https://registry.modelcontextprotocol.io/v0/servers?search=app.apiguru"><img src="https://img.shields.io/badge/MCP-server-2563eb" alt="MCP server"></a>
    <a href="https://pypi.org/project/apiguru-mcp/"><img src="https://img.shields.io/pypi/v/apiguru-mcp?label=PyPI&color=3775a9" alt="apiguru-mcp on PyPI"></a>
    <a href="https://www.npmjs.com/package/apiguru-mcp"><img src="https://img.shields.io/npm/v/apiguru-mcp?label=npm&color=cb3837" alt="apiguru-mcp on npm"></a>
    <a href="https://agent.apiguru.app/.well-known/x402"><img src="https://img.shields.io/badge/x402-USDC%20on%20Base-0052ff" alt="x402: USDC on Base"></a>
    <a href="https://dash.apiguru.app/openapi.json"><img src="https://img.shields.io/badge/OpenAPI-3.1-6ba539" alt="OpenAPI 3.1"></a>
  </p>
</div>

# amazon-scraper-v2 — the agent-ready Amazon Scraper API

Real-time Amazon data — product details, prices, offers & stock, reviews, search, best sellers, deals and seller data — across 20 marketplaces. Call it from Python in 20 lines (examples below), or hand it to the AI agent you already have open: it reads our docs itself and starts pulling live data. No SDK, no wrapper code, nothing to install.

## Start with your AI

Paste one sentence into Claude Code, Codex, Cursor, Gemini CLI, Copilot, Claude Desktop, ChatGPT — anything that can call HTTP:

```
Use Apiguru for live Amazon data. Read https://agent.apiguru.app/llms.txt first, then call it.
```

That is the whole integration. Three ways in, same URL:

| Mode | The line to paste | What you get |
|---|---|---|
| **No account** | `Use Apiguru for live Amazon data. Read https://agent.apiguru.app/llms.txt first, then call it.` | 3 free calls a day, per machine. No account, no key, no card — enough for an agent to prove the data is what you need. |
| **With a key** | `Use Apiguru for live Amazon data. Read https://agent.apiguru.app/llms.txt first, then call it with the header X-API-KEY: YOUR_API_KEY` | A [free key from the dashboard](https://dash.apiguru.app/register) raises that to 100 requests a month, and every call your agent makes shows up in your usage graph. |
| **With a wallet** | `Use Apiguru for live Amazon data. Read https://agent.apiguru.app/llms.txt first, then call it, and settle the 402 with x402 from my wallet.` | Pays per call in USDC on Base — about a cent a call, still no account. Your agent needs an x402 client and a funded wallet. |

Curious what the agent sees? **[Read what your agent reads →](https://agent.apiguru.app/llms.txt)**

## Or wire it in as permanent tools

The one line above needs nothing installed. If you would rather your client list Apiguru as named tools it can pick from — and remember them between sessions — there is an MCP server too: 12 tools with prices and retry rules written into the descriptions, sign-in from claude.ai or ChatGPT that bills the same account, and the same three ways in.

```bash
# claude.ai / Claude Desktop / ChatGPT: add a connector
https://mcp.apiguru.app/account

# Claude Code
claude mcp add --transport http apiguru https://mcp.apiguru.app/mcp
/plugin marketplace add apiguru-app/agent-kit

# Codex CLI
codex mcp add apiguru --url https://mcp.apiguru.app/mcp

# any local MCP client
uvx apiguru-mcp        # PyPI
npx -y apiguru-mcp     # npm

# keyless HTTP, no signup: 3 free calls/day, then x402
curl "https://agent.apiguru.app/agent/v1/v2/product-details?asin=B09DJLW458"
```

Everything an agent needs lives in the **[Agent Kit on GitHub](https://github.com/apiguru-app/agent-kit)**. Machine-readable: [llms.txt](https://dash.apiguru.app/llms.txt) · [OpenAPI](https://dash.apiguru.app/openapi.json) · [x402 catalogue](https://agent.apiguru.app/.well-known/x402) · [PyPI](https://pypi.org/project/apiguru-mcp/) · [npm](https://www.npmjs.com/package/apiguru-mcp) · [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=app.apiguru)

## Quick Start (Python)

### 1. Get Your API Key for **amazon-scraper-v2**

Register for a free account and get your API key:

**👉 [https://dash.apiguru.app/register](https://dash.apiguru.app/register)**

Free trial requests included with every account!

### 2. Install Dependencies

```bash
pip install requests
```

### 3. Run Examples

Each endpoint has its own simple example file. Just add your API key for **amazon-scraper-v2** and run:

```bash
# Search for products
python examples/01_search_products.py

# Get product details
python examples/02_product_details.py

# Get product offers
python examples/03_product_offers.py

# Get product reviews
python examples/04_product_reviews.py

# Get best sellers
python examples/05_best_sellers.py

# Get today's deals
python examples/06_todays_deals.py

# Get seller profile
python examples/07_seller_profile.py

# Get seller products
python examples/08_seller_products.py

# Get seller reviews
python examples/09_seller_reviews.py

# Batch product details (up to 10 ASINs)
python examples/10_batch_product_details.py
```

## API Endpoints

### Product Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `/search` | Search for products | `query=laptop&geo=US` |
| `/v2/product-details` | Get detailed product info | `asin=B08C7FBW4N&geo=US` |
| `/product` | Batch product details (up to 10 ASINs) | `asins=B08C7FBW4N,B09VR3N1YW&geo=US` |
| `/scrape` | Get product offers & prices | `asins=B08C7FBW4N&geo=US` |
| `/v2/product-reviews` | Get product reviews | `asin=B08C7FBW4N&geo=US` |

### Seller Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `/seller-profile` | Get seller profile | `seller_ids=A2L77EE7U53NWQ&geo=US` |
| `/v2/seller-products` | Get seller's products | `seller_id=A2L77EE7U53NWQ&geo=US` |
| `/v2/seller-reviews` | Get seller reviews | `seller_id=A2L77EE7U53NWQ&geo=US` |

### Discovery Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `/v2/best-sellers` | Get best sellers | `geo=US&page=1` |
| `/v2/deals` | Get today's deals | `geo=US&min_product_star_rating=4` |

## Supported Countries

The API supports the following Amazon marketplaces:

`US`, `CA`, `DE`, `MX`, `UK`, `FR`, `IT`, `ES`, `AU`, `BR`, `IN`, `JP`, `NL`, `AE`, `PL`, `SA`, `SG`, `SE`, `TR`, `BE`

## Authentication

All API requests require an API key passed via the `x-api-key` header:

```bash
curl -H "x-api-key: YOUR_API_KEY" "https://dash.apiguru.app/api/v1/search?query=laptop&geo=US"
```

## Quick Example

Here's a simple example - just 20 lines of code:

```python
import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# Search for products
response = requests.get(
    f"{BASE_URL}/search",
    headers={"x-api-key": API_KEY},
    params={
        "query": "wireless headphones",
        "geo": "US",
        "page": 1
    }
)

# Print the response
print(json.dumps(response.json(), indent=2))
```

That's it! Check the `/examples` folder for more endpoint examples.

## Common Use Cases

### 1. Price Tracking

Monitor product prices across different sellers and countries.

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/scrape",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={"asins": "B08C7FBW4N", "geo": "US", "condition": "new"}
)

offers = response.json()
offer_data = offers['results'][0]['data']

# Get price stats
prices = [offer['price'] for offer in offer_data]
print(f"Lowest Price: ${min(prices)}")
print(f"Highest Price: ${max(prices)}")
print(f"Total Offers: {len(offer_data)}")
```

### 2. Product Research

Find profitable products with good ratings and sales volume.

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/v2/best-sellers",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={"geo": "US", "page": 1}
)

best_sellers = response.json()

# Filter high-rated products
for product in best_sellers['data']:
    if float(product['star_rating']) >= 4.5:
        print(f"{product['title']}")
        print(f"  Price: {product['price']}")
        print(f"  Rating: {product['star_rating']}")
```

### 3. Competitor Analysis

Monitor competitor products and pricing.

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/seller-profile",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={"seller_ids": "A2L77EE7U53NWQ", "geo": "US"}
)

profile = response.json()
seller = profile['data']
lifetime = seller['reviews']['lifetime_reviews']

print(f"Business: {seller['business_name']}")
print(f"Total Reviews: {lifetime['reviews_count']}")
print(f"Positive: {lifetime['positive_percentage']}")
```

### 4. Review Analysis

Analyze customer sentiment and product feedback.

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/v2/product-reviews",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={"asin": "B08C7FBW4N", "geo": "US", "page": 1}
)

data = response.json()['data']

# Analyze sentiment
positive = sum(1 for r in data['reviews'] if float(r['rating'].split()[0]) >= 4.0)
negative = sum(1 for r in data['reviews'] if float(r['rating'].split()[0]) <= 2.0)

print(f"Total Reviews: {data['total_reviews']}")
print(f"Positive: {positive}, Negative: {negative}")
```

### 5. Deal Finder

Find the best deals automatically.

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/v2/deals",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={
        "geo": "US",
        "min_product_star_rating": "4"
    }
)

deals = response.json()

# Display top deals
for deal in deals.get('deals', [])[:5]:
    print(f"{deal['title']}")
    print(f"  Price: {deal['deal_price']}")
```

### 6. Batch Product Details

Get details for multiple products at once (up to 10 ASINs).

```python
import requests

response = requests.get(
    "https://dash.apiguru.app/api/v1/product",
    headers={"x-api-key": "YOUR_API_KEY"},
    params={
        "geo": "US",
        "asins": "B0014BYHJE,B0CP9YB3Q4,B0C59CLN29,B0BNYR7MQV,B0CJF94M8J"
    }
)

products = response.json()

# Display all products
for product in products:
    print(f"ASIN: {product['asin']}")
    print(f"Title: {product.get('title', 'N/A')}")
    print(f"Price: {product.get('price', 'N/A')}")
    print("---")
```

## Parameters Reference

### Common Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `geo` | string | Yes | Country code | `US`, `UK`, `DE` |
| `asin` | string | Varies | Amazon product ID (10 chars) | `B08C7FBW4N` |
| `page` | integer | No | Page number (1-100) | `1` |

### Search Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `query` | string | Yes | Search term | `laptop` |

### Offers Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `asins` | string | Yes | Single or comma-separated ASINs | `B08C7FBW4N,B09VR3N1YW` |
| `condition` | string | No | Product condition | `new`, `used`, `all` |
| `check_inventory` | boolean | No | Check real-time inventory | `true`, `false` |

### Seller Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `seller_id` | string | Yes | Amazon seller ID | `A2L77EE7U53NWQ` |
| `seller_ids` | string | Yes | Comma-separated seller IDs | `A2L77EE7U53NWQ,A3BCD...` |
| `from_rating` | string | No | Filter from rating | `1`, `2`, `3`, `4`, `5` |
| `to_rating` | string | No | Filter to rating | `1`, `2`, `3`, `4`, `5` |

### Deals Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `min_product_star_rating` | string | No | Minimum product rating | `ALL`, `1`, `2`, `3`, `4`, `5` |
| `price_range` | string | No | Price filter | `ALL`, `0-25`, `25-50`, `50-100`, `100-200`, `200+` |
| `discount_range` | string | No | Discount filter | `ALL`, `10-25`, `25-50`, `50-70`, `70+` |

## Error Handling

The API uses standard HTTP status codes:

| Code | Description | Solution |
|------|-------------|----------|
| `200` | Success | Request completed successfully |
| `400` | Bad Request | Check your parameters |
| `401` | Unauthorized | Invalid API key |
| `402` | Payment Required | Insufficient credits or no active subscription |
| `429` | Rate Limit | Wait and retry |
| `500` | Server Error | Retry the request |

### Example Error Handling

```python
try:
    results = await api.search_products("laptop", "US")
except Exception as e:
    if "402" in str(e):
        print("Please add funds at https://dash.apiguru.app/top-up")
    elif "429" in str(e):
        print("Rate limit - waiting 60 seconds...")
        await asyncio.sleep(60)
    else:
        print(f"Error: {e}")
```

## Rate Limits

Rate limits depend on your subscription plan:

- **Free Trial**: Limited requests to test the API
- **Pay-as-you-go**: Based on account balance
- **Subscription Plans**: Higher limits with better rates

Check your current usage at [https://dash.apiguru.app/profile](https://dash.apiguru.app/profile)

## Installation

Just install requests:

```bash
pip install requests
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

That's it!

## Project Structure

```
amazon-scraper-v2/
├── README.md                          # This file
├── QUICKSTART.md                      # Three steps to a first call
├── requirements.txt                   # Python dependencies (just requests)
└── examples/                          # Simple Python examples
    ├── 01_search_products.py         # Search for products
    ├── 02_product_details.py         # Get product details
    ├── 03_product_offers.py          # Get product offers
    ├── 04_product_reviews.py         # Get product reviews
    ├── 05_best_sellers.py            # Get best sellers
    ├── 06_todays_deals.py            # Get today's deals
    ├── 07_seller_profile.py          # Get seller profile
    ├── 08_seller_products.py         # Get seller products
    ├── 09_seller_reviews.py          # Get seller reviews
    └── 10_batch_product_details.py   # Batch product details (up to 10)
```

Example response shapes for every endpoint are in the [OpenAPI spec](https://dash.apiguru.app/openapi.json).

## Tips

1. **Reuse the session** - Create one `requests.Session()` for multiple requests
2. **Use the right endpoint** - Choose the endpoint that returns only what you need
3. **Check rate limits** - Monitor your usage in the dashboard

## Support for **amazon-scraper-v2**.

- **Documentation**: [llms.txt](https://agent.apiguru.app/llms.txt) (what your agent reads) · [OpenAPI](https://dash.apiguru.app/openapi.json) · [Agent Kit](https://github.com/apiguru-app/agent-kit)
- **Dashboard**: [https://dash.apiguru.app](https://dash.apiguru.app)
- **API Status**: Check your usage and limits in the dashboard
- **Something wrong or missing?** Open an issue on the [Agent Kit](https://github.com/apiguru-app/agent-kit/issues), or post to the [feedback wall](https://dash.apiguru.app/feedback) — no account needed. The agents and developers who report are the ones this API gets fixed for.


## License

These code examples are provided as-is for use with the Amazon API service.

## Get Started Now!
To use **amazon-scraper-v2**:
1. **Register**: [https://dash.apiguru.app/register](https://dash.apiguru.app/register)
2. **Get your API key**: Free trial included!
3. **Copy examples**: Choose your language
4. **Start building**: Fast, modern, simple
