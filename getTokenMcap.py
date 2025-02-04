import requests

def get_token_market_cap(mint_address: str) -> float:
    """
    Given a Solana token mint address, queries DexScreener for market data
    and returns the token's FDV (fully diluted valuation) as an approximation 
    of market cap. Returns None if not found.

    :param mint_address: The Solana token mint address as a string.
    :return: Token's approximate market cap (FDV) as a float, or None if not found.
    """
    try:
        url = f"https://api.dexscreener.com/latest/dex/search?q={mint_address}"
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError if the request was unsuccessful
        data = response.json()
        # Filter for pairs on Solana
        solana_pairs = [
            pair for pair in data.get('pairs', [])
            if pair.get('chainId') == 'solana'
        ]

        if not solana_pairs:
            # No pairs found for this token on Solana
            return None
        
        # Pick the first matching pair. Depending on your needs, you may want
        # to iterate over all pairs or pick the one with highest volume/liquidity.
        pair_data = solana_pairs[0]
        # 'fdv' in DexScreener is fully diluted valuation (an approximation of market cap).
        market_cap = pair_data.get('marketCap')
        
        return market_cap

    except requests.RequestException as e:
        print(f"Error accessing DexScreener API: {e}")
        return None

