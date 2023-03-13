import pandas as pd
import requests
import os

def download_stock_data(name):
    # Define the URL for downloading the data
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{name}?period1=0&period2=9999999999&interval=1d&events=history&includeAdjustedClose=true"

    # Send a GET request to the URL and save the response content as a CSV file
    response = requests.get(url)
    if response.status_code == 200:
        data_folder = "data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        filename = os.path.join(data_folder, f"stock-{name}.csv")
        with open(filename, "wb") as f:
            f.write(response.content)
        
        # Load the data from the CSV file into a Pandas DataFrame
        df = pd.read_csv(filename)

        # Compute the volume divided by the market capitalization
        df["volume/market_cap"] = df["Volume"] / df["Market Cap"]

        # Save the updated DataFrame back to the CSV file
        df.to_csv(filename, index=False)

        print(f"Stock data for {name} downloaded and saved to {filename}")
    else:
        print(f"Error downloading stock data for {name}")

if __name__ == "__main__":
    download_stock_data("AAPL")