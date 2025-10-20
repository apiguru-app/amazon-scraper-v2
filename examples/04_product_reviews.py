"""
Product Reviews Example
========================
Get customer reviews for a product.

Endpoint: /v2/product-reviews
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/v2/product-reviews",
    headers={"x-api-key": API_KEY},
    params={
        "asin": "B08C7FBW4N",
        "geo": "US",
        "page": 1
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
