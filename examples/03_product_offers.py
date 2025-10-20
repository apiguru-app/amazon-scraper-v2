"""
Product Offers Example
=======================
Get offers and prices from different sellers.

Endpoint: /scrape
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/scrape",
    headers={"x-api-key": API_KEY},
    params={
        "asins": "B08C7FBW4N",
        "geo": "US",
        "condition": "new"
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
