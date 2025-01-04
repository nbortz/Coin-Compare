import getHoldertoMcap
from getTweetData import get_cashtag_mentions
from getTickerFromMint import get_token_ticker_from_mint_solscan
import coinClass
import requests

# 1. accept user input for the contract address
newMintAdd = input("Please enter a contract address to compare: ")

# 2. run the data collection algos w/ mint address
# set data collection variables here
solRpcUrl = "https://api.mainnet-beta.solana.com"
helius_api_key = "96f8d766-bb4f-4b39-b4b1-8ede9278be60"


holderToMcap = getHoldertoMcap.get_holder_to_marketcap_ratio(newMintAdd, solRpcUrl, helius_api_key)

ticker = get_token_ticker_from_mint_solscan(newMintAdd)
xImpressions = get_cashtag_mentions('$'+ ticker)

# 3. roll data into a coin object
# 4. compare it against our existing coin objects and return correlation score