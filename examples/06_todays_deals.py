"""
Today's Deals Example
======================
Get current deals and discounts.

Endpoint: /v2/deals
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/v2/deals",
    headers={"x-api-key": API_KEY},
    params={
        "geo": "US",
        "min_product_star_rating": "4"
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
