import requests

def get_token_ticker_from_mint_solscan(mint_address: str) -> str:
    """
    Fetch the token's ticker (symbol) from Solscan using its public API.

    :param mint_address: Solana token mint address as a string
    :return: Token ticker (symbol) if found, otherwise an empty string or None
    """
    url = f"https://public-api.solscan.io/token/meta?token={mint_address}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # According to Solscan's docs, `symbol` holds the token ticker
        symbol = data.get("symbol", None)
        return symbol
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching token data: {e}")
        return None