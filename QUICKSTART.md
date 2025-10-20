# Quick Start Guide - amazon-scraper-v2

Get started with the Amazon Scraper API in 3 simple steps!

## Step 1: Get Your API Key

Register for a free account and get your API key:

**👉 [https://dash.apiguru.app/register](https://dash.apiguru.app/register)**

✅ Free trial requests included!

## Step 2: Install Dependencies

```bash
pip install requests
```

## Step 3: Run Your First API Call

### Search for Products

1. Open `examples/01_search_products.py`
2. Replace `YOUR_API_KEY_HERE` with your API key
3. Run it:

```bash
python examples/01_search_products.py
```

That's it! You'll see a nicely formatted JSON response.

### Try Other Endpoints

```bash
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

## Need Help?

- **Full Documentation**: [README.md](README.md)
- **Dashboard**: [https://dash.apiguru.app](https://dash.apiguru.app)
- **Example Responses**: Check the `/responses` folder

