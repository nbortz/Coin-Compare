import requests
import time
# Define the API route and key
api_route = "https://api2.tweetbinder.com"
api_key = "43015a4f-5110-47c4-923d-d8ecfae37b70"

# Define the headers with the authorization token
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Function to get balances
def get_balances():
    url = f"{api_route}/me/balances"
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
        print("Count Data:", count_data)
        print("/n Total: ", total)
    else:
        print(f"Failed to retrieve count data. Status code: {response.status_code}")
        print("Response:", response.text)

# Get balances
get_balances()

# Create Twitter count for historical type with the specified query which uses Unix time for dates
query = {
    "query": {
        "raw": "$btc",
        "startDate": 1672531200,
        "endDate": 1704067200
    }
}

#Change historical to 7-day to change report type
count_id = create_twitter_count("historical", query)
time.sleep(15)
# If count ID is obtained, view the count data
if count_id:
    view_count_data(count_id)
