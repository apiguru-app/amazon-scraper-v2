"""
Search Products Example
========================
Search for products on Amazon by keyword.

Endpoint: /search
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request
response = requests.get(
    f"{BASE_URL}/search",
    headers={"x-api-key": API_KEY},
    params={
        "query": "wireless headphones",
        "geo": "US",
        "page": 1
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
