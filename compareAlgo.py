#Algorithm

#Take in variables from main relating to user coin

#Get data from CSV's related to benchmark coins

#Compare Holder to Mcap ratio

#Compare Market Cap

#Compare Impressions

#Each comparison should check that the data is within a certain threshold
#maybe 10%, then look at the %difference

#We should try to note if the difference is positive or negative for the coin

import pandas as pd

def load_single_csv_up_to_date(file_name, cutoff_date):
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


# Example usage
file_name = 'HistoricalData\Just a chill guy_11_8_2024-1_9_2025_historical_data_coinmarketcap.csv'
cutoff_date = '2025-1-1'
filtered_df = load_single_csv_up_to_date(file_name, cutoff_date)
print(filtered_df)

