import time
import requests

def create_twitter_count_report(api_key, query_raw, report_type="7-day"):
    """
    Creates a Twitter count report on TweetBinder and returns the resourceId needed to fetch stats.
    
    Args:
        api_key (str): Your TweetBinder API key.
        query_raw (str): The raw query string (e.g., "(Osasuna OR #Osasuna) -@RealMadrid lang:en").
        report_type (str): '7-day' or 'historical'.
    
    Returns:
        str: The resourceId for the created report.
        None: If the request fails or the response is invalid.
    """
    # 1) Construct the POST URL
    url = f"https://api.tweetbinder.com/reports/twitter-count/{report_type}"
    
    # 2) Build the JSON payload as per TweetBinder docs
    payload = {
        "query": {
            "raw": query_raw
        }
    }
    
    # 3) Include the API key either in headers or query string (depends on TweetBinder’s requirements)
    #    The docs are not 100% clear, so here we put it as a query parameter for illustration.
    params = {
        "api_key": api_key
    }
    
    try:
        response = requests.post(url, params=params, json=payload)
        response.raise_for_status()
        
        # Hypothetical response structure:
        # {
        #   "status": "ok",
        #   "data": {
        #       "resourceId": "xyz12345",
        #       ...
        #   }
        # }
        data = response.json()
        resource_id = data.get("data", {}).get("resourceId")
        
        if resource_id:
            return resource_id
        else:
            print("No resourceId found in the response.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error creating Twitter count report: {e}")
        return None


def get_report_stats(api_key, resource_id):
    """
    Retrieves the stats for a previously created Twitter count report.
    
    Args:
        api_key (str): Your TweetBinder API key.
        resource_id (str): The resourceId returned by create_twitter_count_report().
    
    Returns:
        int: The number of posts (tweets) for the query.
        None: If the request fails or the response is invalid.
    """
    # Hypothetical endpoint for retrieving stats:
    url = f"https://api.tweetbinder.com/reports/{resource_id}"
    
    # The docs might require a query parameter or header for the API key.
    params = {
        "api_key": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Example of a possible JSON structure:
        # {
        #   "status": "ok",
        #   "data": {
        #       "tweets": 12345,
        #       ...
        #   }
        # }
        data = response.json()
        tweets = data.get("data", {}).get("tweets")
        
        return tweets

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving report stats: {e}")
        return None


def get_twitter_count(api_key, query_raw, report_type="7-day", max_retries=5, delay=2):
    """
    Combines the creation of a Twitter count report and the retrieval of stats,
    waiting (if necessary) for the report to be generated.
    
    Args:
        api_key (str): Your TweetBinder API key.
        query_raw (str): The raw query string.
        report_type (str): '7-day' or 'historical'.
        max_retries (int): How many times we’ll retry fetching the stats if they’re not ready.
        delay (int): Delay in seconds between retries.
    
    Returns:
        int: The total number of tweets for the query.
        None: If the report fails or stats are never retrieved.
    """
    resource_id = create_twitter_count_report(api_key, query_raw, report_type=report_type)
    if not resource_id:
        return None
    
    # Poll the "Get report stats" endpoint until we get the result or exhaust retries
    for attempt in range(max_retries):
        tweet_count = get_report_stats(api_key, resource_id)
        
        if tweet_count is not None:
            return tweet_count
        
        # If stats are not ready yet, wait and retry
        print(f"Report not ready (attempt {attempt + 1}), waiting {delay}s before retrying...")
        time.sleep(delay)
    
    print("Exceeded maximum retries. Stats could not be retrieved.")
    return None


if __name__ == "__main__":
    # Example usage:
    # Replace these with your actual API key and query
    my_api_key = "43015a4f-5110-47c4-923d-d8ecfae37b70"
    
    # For a cashtag, you might do something like:
    # query = "($AAPL) OR #AAPL"
    # but you can add or remove operators depending on your needs.
    query = "$BTC"
    
    # Decide if you want a 7-day or historical report
    report_type = "historical"
    
    count = get_twitter_count(my_api_key, query, report_type)
    if count is not None:
        print(f"Number of posts (tweets) for the query '{query}': {count}")
    else:
        print("Failed to retrieve the count.")
