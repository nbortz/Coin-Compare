import getHoldertoMcap
from getTokenAge import get_token_age_from_dexscreener
from getTickerFromMint import get_token_ticker_from_mint_dexscreener
from getTokenMcap import get_token_market_cap
from getTokenVolume import get_token_24h_volume
from tokenAgeAddition import add_age
from coinClass import Coin
import requests
import datetime
from compareFunctions import get_benchmark_data, compare_mcap, compare_volume, percent_and_total_diff

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

Comparision) Compare Marketcap, Holder to Marketcap Ratio, Volume, and Impressions at a certain timestamp, this should be done with compareAlgo

Correlation) Return correlation scores to user on website
"""
# Declare global variables

solRpcUrl = "https://api.mainnet-beta.solana.com"
helius_api_key = "96f8d766-bb4f-4b39-b4b1-8ede9278be60"
bonkLaunchDate = datetime.date(2023,1,5)
wifLaunchDate = datetime.date(2023,11,21)
fartcoinLaunchDate = datetime.date(24,10,19)
fwogLaunchDate = datetime.date(24,7,30)
gigaLaunchDate = datetime.date(24,1,5)
goatLaunchDate = datetime.date(24,10,11)
chillguyLaunchDate = datetime.date(24,11,21)
# Accept user input for the contract address
newMintAdd = input("Please enter a contract address to compare: ")

# Get user token age
userTokenAge = get_token_age_from_dexscreener(newMintAdd)

# Get the ticker
userTicker = get_token_ticker_from_mint_dexscreener(newMintAdd)
# Get user token mcap
userTokenMcap = get_token_market_cap(newMintAdd)
# Get user token vol
userTokenVol = get_token_24h_volume(newMintAdd)
# Get user token Holder to mcap
#userTokenHolders = getHoldertoMcap.get_holder_count(solRpcUrl, newMintAdd)
#userTokenHoldertoMcap = userTokenMcap / userTokenHolders

# TODO: Get user token impression count (lifetime)
#countId = getTweetData.create_twitter_count('historical', userTicker)
#userImpressions = getTweetData.view_count_data(countId)

#Call addAge on each compare token to get the desired conparision date for each
bonkCompareDate = add_age(bonkLaunchDate, userTokenAge)
wifCompareDate = add_age(wifLaunchDate, userTokenAge)
fartcoinCompareDate = add_age(fartcoinLaunchDate, userTokenAge)
fwogCompareDate = add_age(fwogLaunchDate, userTokenAge)
gigaCompareDate = add_age(gigaLaunchDate, userTokenAge)
goatCompareDate = add_age(goatLaunchDate, userTokenAge)
chillguyCompareDate = add_age(chillguyLaunchDate, userTokenAge)

# Integrate calls to compare functions
def compare_token_with_benchmark(benchmark_file, compare_date, user_mcap, user_vol):
    benchmark_data = get_benchmark_data(benchmark_file, compare_date, ',')
    
    mcap_diff = compare_mcap(benchmark_data, user_mcap)
    vol_diff = compare_volume(benchmark_data, user_vol)
    
    return mcap_diff, vol_diff

# Example usage
bonk_mcap_diff, bonk_vol_diff = compare_token_with_benchmark('HistoricalData/bonk-tokenHist.csv', bonkCompareDate, userTokenMcap, userTokenVol)
wif_mcap_diff, wif_vol_diff = compare_token_with_benchmark('HistoricalData/dogwifhatHist.csv', wifCompareDate, userTokenMcap, userTokenVol)
print(fartcoinCompareDate)
fart_mcap_diff, fart_vol_diff = compare_token_with_benchmark('HistoricalData/FartcoinHist.csv', fartcoinCompareDate, userTokenMcap, userTokenVol)
# Repeat for other tokens...

print(f"Bonk Market Cap Difference: {bonk_mcap_diff}%")
print(f"Bonk Volume Difference: {bonk_vol_diff}%")
print(f"Wif Market Cap Difference: {wif_mcap_diff}%")
print(f"Wif Volume Difference: {wif_vol_diff}%")
print(f"Fart Market Cap Difference: {fart_mcap_diff}%")
print(f"Fart Volume Difference: {fart_vol_diff}%")
# Print other comparisons...
