"""
Seller Products Example
========================
Get all products from a specific seller.

Endpoint: /v2/seller-products
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/v2/seller-products",
    headers={"x-api-key": API_KEY},
    params={
        "seller_id": "A1N19S11406VL4",
        "geo": "US",
        "page": 1
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
