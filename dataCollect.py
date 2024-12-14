import requests
from solana.rpc.api import Client
import datetime

url = "https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=365&interval=daily&precision=5"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-FsQSSZs89Khq73S2burfkVAW"
}

response = requests.get(url, headers=headers)

print(response.text)

def getHoldertoMcap(contract):
    #initiialize Sol client
    solana_client = Client("https://api.mainnet-beta.solana.com")
