import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_crypto_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=365&interval=daily&precision=5"
    
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-FsQSSZs89Khq73S2burfkVAW"
    }
    
    response = requests.get(url, headers=headers)
    
    return response.text

def plot_crypto_data(response_text):
    # Convert response text to dictionary
    data = eval(response_text)
    
    # Extract prices data
    prices_data = data['prices']
    
    # Extract timestamps and prices
    timestamps = [item[0] for item in prices_data]
    prices = [item[1] for item in prices_data]
    
    # Convert Unix timestamps to US standard timestamps
    dates = [datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d') for ts in timestamps]
    
    # Debugging output
    print("Dates:", dates[:5])  # Print first 5 dates
    print("Prices:", prices[:5])  # Print first 5 prices
    
    # Plot the data using US standard timestamps
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Cryptocurrency Price Over Time')
    
    # Show only 1 in 20 timestamps on the x-axis
    plt.xticks(dates[::20], rotation=45)
    
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage:
coin_id = "dogecoin"
response_text = get_crypto_data(coin_id)
plot_crypto_data(response_text)
