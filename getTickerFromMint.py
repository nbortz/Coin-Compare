import requests

def get_token_ticker_from_mint_dexscreener(mint_address: str) -> str:
    """
    Fetch the token's ticker (symbol) from the DexScreener API using the Solana token mint address.
    
    :param mint_address: Solana token mint address as a string
    :return: Token ticker (symbol) if found, otherwise None
    """
    url = f"https://api.dexscreener.com/latest/dex/search/?q={mint_address}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 'pairs' is a list of results. Each entry has 'baseToken' and 'quoteToken'.
        pairs = data.get("pairs", [])
        for pair in pairs:
            base = pair.get("baseToken", {})
            quote = pair.get("quoteToken", {})

            # Check if the base token address matches the mint_address:
            if base.get("address") == mint_address:
                return base.get("symbol", None)

            # Or if the quote token address matches the mint_address:
            if quote.get("address") == mint_address:
                return quote.get("symbol", None)

        # If we do not find any match, return None
        return None

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching token data: {e}")
        return None