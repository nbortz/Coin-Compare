from solana.rpc.api import Client
from solana.publickey import PublicKey
import datetime
import requests

#Need to pass CA/token_mint in from main (user input)
token_mint = "F5hqdbykXuksp8P78CAZenSvpPShAYKrP2U2MiZMdgFN"
helius_api_key = "96f8d766-bb4f-4b39-b4b1-8ede9278be60"
solana_rpc_url = "https://api.mainnet-beta.solana.com"
def get_holder_to_marketcap_ratio(token_mint: str, solana_rpc_url: str, helius_api_key: str) -> float:
    # 1. Initialize Solana Client
    solana_client = Client(solana_rpc_url)

    #Get token supply
    supply_resp = solana_client.get_token_supply(token_mint)
    if not supply_resp.get('result'):
        raise Exception("Error fetching token supply from Sol RPC")
    
    supply_info = supply_resp['result']['value']
    raw_supply = int(supply_info['amount'])
    decimals = int(supply_info['decimals'])
    total_supply = raw_supply / (10 ** decimals)

    solscan_url = f"https://public-api.solscan.io/token/holders?token={token_mint}"
    holders_resp = requests.get(solscan_url)
    if holders_resp.status_code != 200:
        raise Exception("Error fetching holder data from solscan")
    # This should return an array of holder accounts
    holders_data = holders_resp.json()
    holder_count = len(holders_data.get('data', []))

    # Use helius to get current token price
    helius_url = f"https://api.helius.xyz/v0/addresses/{token_mint}/prices?api-key={helius_api_key}"
    price_resp = requests.get(helius_url)
    if price_resp.status_code != 200:
        raise Exception("Error fetching price data from Helius")
    
    price_data = price_resp.json()

    # Most recent price is at index 0, ensure array has values
    if not price_data or 'price' not in price_data[0]:
        raise Exception("No valid price data returned")
    current_price = price_data[0]['price']

    # Calc holder to mcap ratio
    market_cap = total_supply * current_price
    if market_cap == 0:
        raise Exception("Error, market cap reads 0")
    ratio = holder_count / market_cap
    return ratio

ratio = get_holder_to_marketcap_ratio(token_mint, solana_rpc_url, helius_api_key)
print(f"Bopcat holder to mcap ratio is {ratio}")