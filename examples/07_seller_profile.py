"""
Seller Profile Example
=======================
Get seller information and ratings.

Endpoint: /seller-profile
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/seller-profile",
    headers={"x-api-key": API_KEY},
    params={
        "seller_ids": "A1N19S11406VL4",
        "geo": "US"
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
