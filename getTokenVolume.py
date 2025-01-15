import requests

def get_token_24h_volume(mint_address: str) -> float:
    """
    Given a Solana token mint address, queries DexScreener for market data
    and returns the token's 24-hour trading volume. Returns None if not found.

    :param mint_address: The Solana token mint address as a string.
    :return: 24-hour volume as a float, or None if not found.
    """
    try:
        url = f"https://api.dexscreener.io/latest/dex/search?q={mint_address}"
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError if the request was unsuccessful
        data = response.json()
        
        # Filter for pairs on Solana
        solana_pairs = [
            pair for pair in data.get('pairs', [])
            if pair.get('chainId') == 'sol'
        ]

        if not solana_pairs:
            # No pairs found for this token on Solana
            return None
        
        # Pick the first matching pair. Depending on your needs, 
        # you might want to choose the pair with the highest liquidity or volume.
        pair_data = solana_pairs[0]
        
        # DexScreener typically provides volume in the 'volume' dict with sub-keys 
        # like 'h24' for 24-hour volume, 'h1' for 1-hour volume, etc.
        volume_24h = pair_data.get('volume', {}).get('h24')
        
        return volume_24h

    except requests.RequestException as e:
        print(f"Error accessing DexScreener API: {e}")
        return None
