from flask import Flask, request, render_template, jsonify
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import io
import base64

app = Flask(__name__)

def get_crypto_data(coin_id, days):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily&precision=5"
    
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-FsQSSZs89Khq73S2burfkVAW"
    }
    
    response = requests.get(url, headers=headers)
    
    return response.json()

def plot_crypto_data(prices_data):
    timestamps = [item[0] for item in prices_data]
    prices = [item[1] for item in prices_data]
    dates = [datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d') for ts in timestamps]
    
    plt.figure(figsize=(15, 8))  # Increase the figure size
    plt.plot(dates, prices, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Cryptocurrency Price Over Time')
    
    # Show only 1 in 20 timestamps on the x-axis
    plt.xticks(dates[::20], rotation=45)
    
    plt.grid(True)
    plt.tight_layout()
    
    # Ensure the entire x-axis is displayed
    plt.gca().set_xlim(left=dates[0], right=dates[-1])
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/plot', methods=['POST'])
def plot():
    coin_id = request.form['coin_id']
    days = request.form['days']
    data = get_crypto_data(coin_id, days)
    
    # Debugging output to check the structure of the response
    print(data)
    
    if 'prices' in data:
        plot_url = plot_crypto_data(data['prices'])
        return jsonify({'plot_url': plot_url})
    else:
        return jsonify({'error': 'No price data found for the given coin ID and days.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
