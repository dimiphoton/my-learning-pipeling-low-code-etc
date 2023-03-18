from pycaret.utils import version
version()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from pycaret.time_series import *
warnings.filterwarnings('ignore')
stocks = pd.read_csv("https://raw.githubusercontent.com/PJalgotrader/Deep_forecasting-USU/main/data/yfinance.csv", index_col=0, header=[0,1])
stocks.head()

# if you are working with Pandas, your first job should be changing the type of the index to datetime and then to period! This is a compatibility issue with other packages. 
stocks.index

stocks.index = pd.to_datetime(stocks.index).to_period('B')
stocks.index

df = stocks['Close'][['AAPL']]
df.head()

idx = pd.period_range(min(df.index), max(df.index))
df.index.symmetric_difference(idx)

df = df.reindex(idx, fill_value=np.nan)
df = df.fillna(method = 'ffill')

from sktime.forecasting.model_selection import SlidingWindowSplitter

import numpy as np
from sktime.forecasting.model_selection import SlidingWindowSplitter
ts = np.arange(10)
splitter = SlidingWindowSplitter(fh=np.arange(1,3), window_length=3, step_length=1)
exp = TSForecastingExperiment()
exp.setup(data = df, target='AAPL' ,coverage=0.90, fold_strategy=SlidingWindowSplitter(fh=np.arange(1,23), window_length=130, step_length=130)) # using the past 6 months data to make prediction for the next month and moving half a year forward. 
from sklearn.model_selection import TimeSeriesSplit

exp.compare_models(sort='rmse')
