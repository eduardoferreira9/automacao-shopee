import requests
from config import settings

def buscar_produtos(limit=5):
    url = "https://open-api.affiliate.shopee.com.br/api/v1/product/search"
    headers = {
        "Authorization": f"Bearer {settings.SHOPEE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "limit": limit,
        "offset": 0,
        "sort_type": 1,
        "category_id": settings.CATEGORY_ID
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("data", {}).get("list", [])
