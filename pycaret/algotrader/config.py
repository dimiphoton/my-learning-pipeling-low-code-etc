import numpy as np
from pycaret.time_series import *
from sktime.forecasting.model_selection import SlidingWindowSplitter

# Config settings and global variables
DATA_URL = "https://raw.githubusercontent.com/PJalgotrader/Deep_forecasting-USU/main/data/yfinance.csv"
TARGET = 'AAPL'
COVERAGE = 0.90
WINDOW_LENGTH = 130
STEP_LENGTH = 130
FOLD_STRATEGY = SlidingWindowSplitter(fh=np.arange(1, 23), window_length=WINDOW_LENGTH, step_length=STEP_LENGTH)
