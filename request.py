import requests
import json

url = "https://api.myntra.com/v3/layout/shoes/nike/nike-killshot-2-leather-men's-shoes/36555048/buy"

headers = {
    "accept": "application/json; charset=utf-8",
    "accept-language": "en-US,en;q=0.5",
    "at": "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTTJabE0yUTBaRGN0Wkdaak9TMHhNV1l3TFdJNFpERXRPV0UzTXpSbU5UTTRabVl5SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzT0RJd01qTTFPVEFzSW1semN5STZJa2xFUlVFaWZRLjhVNDVfTmlXZTltVUVjT3BsR2FKNnZjd0t4ZHN6eVdGUF81RHZUcGJKZkU=",
    "user-agent": "MyntraRetailAndroid/4.2512.10 (Phone, 420dpi); MyntraAndroid/4.2512.10 (Phone, 420dpi); api;",
    "content-type": "application/json; charset=utf-8"
}

payload = {
    "pageContext": {
        "RequestPayloadData": {
            "pincode": "500001",
            "nonWorkingDays": [],
            "shouldShowInfiniteProductHC": True,
            "isOpenedFromDeeplink": True,
            "immersiveFwdEnabled": True,
            "store": "myntra",
            "customerCohorts": []
        }
    },
    "pageUri": "/v3/layout/shoes/nike/nike-killshot-2-leather-men's-shoes/36555048/buy"
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(payload),
    timeout=30
)

print(response.json()['pageMeta'])