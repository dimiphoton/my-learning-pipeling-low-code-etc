import pandas as pd
import numpy as np

def load_data(url):
    stocks = pd.read_csv(url, index_col=0, header=[0, 1])
    return stocks

def process_data(stocks, target):
    stocks.index = pd.to_datetime(stocks.index).to_period('B')
    df = stocks['Close'][[target]]
    idx = pd.period_range(min(df.index), max(df.index))
    df.index.symmetric_difference(idx)
    df = df.reindex(idx, fill_value=np.nan)
    df = df.fillna(method='ffill')
    return df
