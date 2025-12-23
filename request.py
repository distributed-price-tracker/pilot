import requests
import json

url = "https://api.myntra.com/auth/v1/token"

headers = {
    "accept": "application/json",
    "user-agent": "MyntraRetailAndroid/4.2512.10",
    "clientid": "myntra-02d7dec5-8a00-4c74-9cf7-9d62dbea5e61",
    "x-myntra-app": "appFamily=MyntraRetailAndroid; appVersion=4.2512.10; deviceCategory=Phone;",
    "x-meta-app": "appFamily=MyntraRetailAndroid; appVersion=4.2512.10; deviceCategory=Phone;",
    "x-myntra-store-context": "myntra",
}

auth_token = requests.get(url, headers=headers).headers.get('at')

url = "https://api.myntra.com/v3/layout/x/x/x/{product_id}/buy"

headers = {
    "accept": "application/json; charset=utf-8",
    "accept-language": "en-US,en;q=0.5",
    "at": auth_token,
    "user-agent": "MyntraRetailAndroid/4.2512.10 (Phone, 420dpi); MyntraAndroid/4.2512.10 (Phone, 420dpi); api;",
    "content-type": "application/json; charset=utf-8"
}

payload = {
    "pageContext": {
        "RequestPayloadData": {
            "pincode": "535001",
            "store": "myntra",
            "customerCohorts": []
        }
    },
}

product_id = "36555048"

response = requests.post(
    url.format(product_id=product_id),
    headers=headers,
    json=payload,
    timeout=30
)

res = response.json()['pageMeta']['gtmData']

print(res)