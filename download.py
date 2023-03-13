import yfinance as yf
import os

def download_stock_data(name):
    # create data folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # download data using yfinance
    stock_data = yf.download(name)

    # divide volume by the number of shares outstanding to get volume per share
    #shares_outstanding = yf.Ticker(name).info['sharesOutstanding']
    #print(shares_outstanding)
    #stock_data['Volume'] = stock_data['Volume'] / shares_outstanding

    # save the data to a CSV file
    file_name = f"data/stock-{name}.csv"
    stock_data.to_csv(file_name)

    print(f"Data downloaded and saved as {file_name}")

if __name__ == "__main__":
    download_stock_data('^GSPC')