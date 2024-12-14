import requests

url = "https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=365&interval=daily&precision=5"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-FsQSSZs89Khq73S2burfkVAW"
}

response = requests.get(url, headers=headers)

print(response.text)
