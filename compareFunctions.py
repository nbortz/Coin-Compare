#Algorithm

#Take in variables from main relating to user coin

#Get data from CSV's related to benchmark coins

#Compare Holder to Mcap ratio

#Compare Market Cap

#Compare Impressions

#We should try to note if the difference is positive or negative for the coin

import pandas as pd


#get benchmark data returns the benchmark data from inception to a given date in a pandas dataframe


def get_benchmark_data(file_name, cutoff_date):
    # Read the CSV file into a dataframe with the correct delimiter
    df = pd.read_csv(file_name, delimiter=';')
    
    # Debugging: Print column names
    print("Column names:", df.columns)
    
    # Set the index to the 'date' column and parse dates
    df.set_index('timestamp', inplace=True)
    df.index = pd.to_datetime(df.index)
    
    # Filter the dataframe to include only rows up to the cutoff date
    filtered_df = df[df.index <= cutoff_date]
    
    print("done")
    return filtered_df


#Compare Mcap returns a percent difference between user coin and benchmark
def compare_mcap(benchmark_df, coin_mCap):
    # Get the last entry in the marketCap column
    last_mCap = benchmark_df['marketCap'].iloc[-1]
    
    # Calculate the percentage difference
    percentage_difference = ((coin_mCap - last_mCap) / last_mCap) * 100
    
    # Return the percentage difference
    return percentage_difference


#Compare impressions from coin inception to present and benchmark inception to certain date
def compare_impressions(benchmark_impressions, coin_impressions):
    # Calculate the percentage difference
    percentage_difference = ((coin_impressions - benchmark_impressions) / benchmark_impressions) * 100

    #calculate numerical diff
    total_diff = coin_impressions - benchmark_impressions
    # Return the percentage difference
    return percentage_difference, total_diff



#Compare holders of coin at present and benchmark at time from inception
def compare_holders(benchmark_holder_count, coin_holder_count):
    
    # Calculate the percentage difference
    percentage_difference = ((coin_holder_count - benchmark_holder_count) / benchmark_holder_count) * 100

    #calculate numerical diff
    total_diff = coin_holder_count - benchmark_holder_count
    # Return the percentage difference
    return percentage_difference, total_diff




#Compare Mcap returns a percent difference between user coin and benchmark
def compare_volume(benchmark_df, coin_vol):
    # Get the last entry in the marketCap column
    last_vol = benchmark_df['volume'].iloc[-1]
    
    # Calculate the percentage difference
    percentage_difference = ((coin_vol - last_vol) / last_vol) * 100
    
    # Return the percentage difference
    return percentage_difference


# Example usage
file_name = 'HistoricalData\Just a chill guy_11_8_2024-1_9_2025_historical_data_coinmarketcap.csv'
cutoff_date = '2025-1-1'
benchmark_df = get_benchmark_data(file_name, cutoff_date)
print(benchmark_df)


# Example coin market cap value for testing
coin_mCap = 9.270706e+08

# Calculate the percentage difference using compare_mcap function
percentage_difference = compare_mcap(benchmark_df, coin_mCap)

print(f"Percentage difference between coin market cap and last benchmark market cap: {percentage_difference:.2f}%")

