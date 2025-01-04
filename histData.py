import requests

response = requests.post(
    "https://api.helius.xyz/v0/webhooks?api-key=1a629aa6-d6b3-4d90-a820-abd2eed91f72",
    headers={"Content-Type":"application/json"},
    json={}
)
data = response.json()
print(data)
