import requests
import datetime

def get_token_age_from_dexscreener(token_address: str) -> int:
    """
    Fetch token pair info from Dexscreener, parse pairCreatedAt,
    and calculate the token's age (in days).
    """
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if 4xx/5xx
    data = response.json()

    pairs = data.get("pairs", [])
    if not pairs:
        raise ValueError("No pairs found for this token address.")

    # Just take the first pair for simplicity
    first_pair = pairs[0]
    
    pair_created_at = first_pair.get("pairCreatedAt")
    if not pair_created_at:
        raise ValueError("No 'pairCreatedAt' field found in pair data.")

    # If pair_created_at is extremely large (~1.7e12+),
    # it might be in milliseconds, so divide by 1000
    if pair_created_at > 1_000_000_000_000:
        pair_created_at /= 1000.0

    # Convert Unix epoch -> datetime in UTC
    creation_dt = datetime.datetime.fromtimestamp(pair_created_at, tz=datetime.timezone.utc)
    
    # Calculate how many days have passed
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    age_days = (now_utc - creation_dt).days
    return age_days

if __name__ == "__main__":
    # Example usage:
    token_address = "F5hqdbykXuksp8P78CAZenSvpPShAYKrP2U2MiZMdgFN"  # Replace with actual address
    try:
        age = get_token_age_from_dexscreener(token_address)
        print(f"Token Address: {token_address}")
        print(f"Token Age (approx): {age} days")
    except Exception as e:
        print(f"Error: {e}")
