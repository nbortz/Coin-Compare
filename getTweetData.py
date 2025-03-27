import requests
import time
import os
# Define the API route and key
api_route = "https://api.tweetbinder.com"
api_key = os.environ.get("TB_API")

# Define the headers with the authorization token
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Function to get balances
def get_balances():
    url = f"{api_route}/me/balances?apiKey={api_key}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        balances = response.json()
        print("Balances:", balances)
    else:
        print(f"Failed to retrieve balances. Status code: {response.status_code}")
        print("Response:", response.text)

# Function to create Twitter count
def create_twitter_count(count_type, query):
    url = f"{api_route}/reports/twitter-count/{count_type}?apiKey={api_key}"
    response = requests.post(url, headers=headers, json=query)
    if response.status_code == 200:
        count = response.json()
        count_id = count.get("resourceId")
        print(f"Twitter Count ({count_type}) Count ID:", count_id)
        return count_id
    else:
        print(f"Failed to create Twitter count. Status code: {response.status_code}")
        print("Response:", response.text)
        return None

# Function to view count data
def view_count_data(count_id):
    url = f"{api_route}/reports/{count_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        count_data = response.json()
        total = count_data.get("total")
        return total
    else:
        print(f"Failed to retrieve count data. Status code: {response.status_code}")
        print("Response:", response.text)
        return(0)

# Get balances
#get_balances()
print(f"API Key: {api_key}")

