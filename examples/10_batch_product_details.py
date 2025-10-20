"""
Batch Product Details Example
==============================
Get details for multiple products at once (up to 10 ASINs).

Endpoint: /product
"""

import requests
import json

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://dash.apiguru.app/api/v1"

# API Request - Get details for multiple products at once
response = requests.get(
    f"{BASE_URL}/product",
    headers={"x-api-key": API_KEY},
    params={
        "geo": "US",
        "asins": "B0014BYHJE,B0CP9YB3Q4,B0C59CLN29,B0BNYR7MQV,B0CJF94M8J"
    }
)

# Print response
print(json.dumps(response.json(), indent=2))
