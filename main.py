import getHoldertoMcap
from getTweetData import get_cashtag_impressions
from getTickerFromMint import get_token_ticker_from_mint_solscan
from coinClass import Coin
import requests

"""
The main Logic function will intake a mint address from a user. 

Age) Then we will call getTokenAge so we can determine the timestamp we will be looking at for each compare token --> Returns age in days of user token
We need logic in the middle to get compare date for each suuccessful token. Ie Wif launch date plus user token age, repeat for each compare token

Ticker) Then we will call getTickerFrom Mint --> Returns a ticker

Impressions) Then we can call getTweetData with the ticker --> Returns impresssion count
We will also need to call getTweetData for each compare token. Store each reply in a csv with a date/time for future reference

Mcap) Pull user token mcap from dexscreener API, pull compare token mcap from csv files.

Holder to Mcap) Pull holder to mcap for user token with getHoldertoMcap function. Need to buy data for compare tokens

Volume) Pull user token volume from dexscreener, pull compare token vol from csv files



Compare Marketcap, Holder to Marketcap Ratio, Volume, and Impressions at a certain timestamp. 
"""

# 1. accept user input for the contract address
newMintAdd = input("Please enter a contract address to compare: ")

# 2. run the data collection algos w/ mint address
# set data collection variables here
solRpcUrl = "https://api.mainnet-beta.solana.com"
helius_api_key = "96f8d766-bb4f-4b39-b4b1-8ede9278be60"


holderToMcap = getHoldertoMcap.get_holder_to_marketcap_ratio(newMintAdd, solRpcUrl, helius_api_key)

ticker = get_token_ticker_from_mint_solscan(newMintAdd)
xImpressions = get_cashtag_impressions('$'+ ticker)

# 3. roll data into a coin object
    # fill this in when data collection is done
    # newCoin = Coin()
# 4. compare it against our existing coin objects and return correlation score