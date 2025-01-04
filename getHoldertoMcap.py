from solana.rpc.api import Client
from solana.rpc.api import Pubkey
import requests
import base64
import struct

def get_holder_count(rpc_url: str, token_mint: str) -> int:
    """
    Fetch the number of holders for a given Solana token by querying on-chain data.
    """
    # SPL Token Program ID
    TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"

    filters = [
        {
            "memcmp": {
                "offset": 0,          # Mint field starts at byte 0 in account data
                "bytes": token_mint
            }
        },
        {
            "dataSize": 165        # SPL token account size is always 165 bytes
        }
    ]

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getProgramAccounts",
        "params": [
            TOKEN_PROGRAM_ID,
            {
                "encoding": "base64",
                "filters": filters
            }
        ]
    }

    response = requests.post(rpc_url, json=payload)
    response_json = response.json()

    if "error" in response_json:
        raise Exception(f"RPC Error: {response_json['error']}")

    result = response_json.get("result", [])

    holder_count = 0
    for account in result:
        account_data = account["account"]["data"][0]  # base64-encoded data is at index 0
        data = base64.b64decode(account_data)

        # Data layout for SPL token account:
        # 0-31: Mint
        # 32-63: Owner
        # 64-71: Amount (8 bytes, little-endian)
        amount_bytes = data[64:72]
        amount = struct.unpack("<Q", amount_bytes)[0]  # <Q for little-endian unsigned long long
        if amount > 0:
            holder_count += 1

    return holder_count

def get_price_from_helius(token_mint: str, helius_api_key: str) -> float:
    """
    Fetch the current price of a Solana token using Helius API.
    """
    # Correct Helius endpoint for fetching token price
    helius_price_url = f"https://api.helius.xyz/v0/tokens/{token_mint}/price"
    headers = {
        "x-api-key": helius_api_key
    }
    price_resp = requests.get(helius_price_url, headers=headers)
    print("Helius Price Status Code:", price_resp.status_code)
    print("Helius Price Response Body:", price_resp.text)

    if price_resp.status_code != 200:
        raise Exception(f"Error fetching price data from Helius. Status: {price_resp.status_code}, Response: {price_resp.text}")

    price_data = price_resp.json()
    # Adjust the parsing based on Helius's actual response structure
    # Example assumption: price is located at data["price"]
    current_price = price_data.get("data", {}).get("price", None)
    if current_price is None:
        raise Exception("No valid price data returned from Helius")

    return current_price

def get_holder_to_marketcap_ratio(token_mint: str, solana_rpc_url: str, helius_api_key: str) -> float:
    """
    Calculate the holder-to-marketcap ratio for a given Solana token.
    """
    # Initialize Solana client
    solana_client = Client(solana_rpc_url)
    token_mint_pubkey = Pubkey.from_string(token_mint)

    # Get token supply
    supply_resp = solana_client.get_token_supply(token_mint_pubkey)
    raw_supply = int(supply_resp.value.amount)
    decimals = int(supply_resp.value.decimals)
    total_supply = raw_supply / (10 ** decimals)

    print(f"Total Supply: {total_supply}")

    # 3. Get token holders from Solscan API
    # Note: The Solscan public API for holders might have pagination;
    # here we assume that a single request can give us total holders count,
    # or we sum over multiple pages if needed.
    # Example endpoint (subject to change): https://public-api.solscan.io/token/holders?token={token_mint}
    solscan_url = f"https://public-api.solscan.io/token/holders?token={token_mint}"
    holders_resp = requests.get(solscan_url)
    if holders_resp.status_code != 200:
        raise Exception("Error fetching holders data from Solscan")

    holders_data = holders_resp.json()
    # The holders endpoint returns an array of holder accounts. We count them.
    # Adjust this logic if the API schema differs.
    holders_count = len(holders_data.get('data', []))

    # 4. Get the current token price from Helius (or another price source)
    helius_url = f"https://api.helius.xyz/v0/addresses/{token_mint}/prices?api-key={helius_api_key}"
    price_resp = requests.get(helius_url)
    if price_resp.status_code != 200:
        raise Exception("Error fetching price data from Helius")

    price_data = price_resp.json()
    # Assuming price_data is a list sorted by most recent first:
    # Adjust the logic according to the actual Helius API response structure
    if not price_data or 'price' not in price_data[0]:
        raise Exception("No valid price data returned")

    current_price = price_data[0]['price']

    # 5. Calculate Market Cap: total_supply * current_price
    market_cap = total_supply * current_price

    # 6. Calculate Holder-to-Marketcap Ratio
    if market_cap == 0:
        raise Exception("Market cap is zero, cannot compute ratio")

    ratio = holders_count / market_cap
    return ratio


# Example usage:
if __name__ == "getHoldertoMcap.py":
    token_mint = "F5hqdbykXuksp8P78CAZenSvpPShAYKrP2U2MiZMdgFN"
    solana_rpc_url = "https://api.mainnet-beta.solana.com"
    helius_api_key = "96f8d766-bb4f-4b39-b4b1-8ede9278be60"  # Replace with your actual Helius API ke

    ratio = get_holder_to_marketcap_ratio(token_mint, solana_rpc_url, helius_api_key)
    print(f"Bopcat ratio is {ratio}")