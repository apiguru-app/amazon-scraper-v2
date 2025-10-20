"""
Best Sellers Example
=====================
Get best-selling products on Amazon.

Endpoint: /v2/best-sellers
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/v2/best-sellers",
    headers={"x-api-key": API_KEY},
    params={
        "geo": "US",
        "page": 1
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
