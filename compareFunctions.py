#Algorithm

#Take in variables from main relating to user coin

#Get data from CSV's related to benchmark coins

#Compare Holder to Mcap ratio

#Compare Market Cap

#Compare Impressions

#We should try to note if the difference is positive or negative for the coin



#Handle case where user token is older than benchmark

import pandas as pd


#get benchmark data returns the benchmark data from inception to a given date in a pandas dataframe


def get_benchmark_data(file_name, cutoff_date, delim):
    # Read the CSV file into a dataframe with the correct delimiter
    df = pd.read_csv(file_name, delimiter=delim)
    
    # Debugging: Print column names
    print("Column names:", df.columns)
    
    # Rename columns if necessary
    df.columns = [col.strip() for col in df.columns]  # Remove any leading/trailing whitespace
    
    # Set the index to the 'timeOpen' column and parse dates
    df.set_index('timeOpen', inplace=True)
    df.index = pd.to_datetime(df.index)
    
    # Convert cutoff_date to datetime64[ns] type
    cutoff_date = pd.to_datetime(cutoff_date)
    
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


#Compare data from coin and benchmark
def percent_and_total_diff(benchmark_value, coin_value):
    # Calculate the percentage difference
    percentage_difference = ((coin_value - benchmark_value) / benchmark_value) * 100

    #calculate numerical diff
    total_diff = coin_value - benchmark_value
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




