import requests

# Define the API route and key
api_route = "https://api.tweetbinder.com"
api_key = "43015a4f-5110-47c4-923d-d8ecfae37b70"

# Construct the full URL
url = f"{api_route}/me/balances"

# Define the headers with the authorization token
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    balances = response.json()
    print("Balances:", balances)
else:
    print(f"Failed to retrieve balances. Status code: {response.status_code}")
    print("Response:", response.text)
