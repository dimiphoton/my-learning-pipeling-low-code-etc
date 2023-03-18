import warnings
from pycaret.utils import version
from config import *
from data_preprocessing import load_data, process_data

warnings.filterwarnings('ignore')

def main():
    version()
    stocks = load_data(DATA_URL)
    df = process_data(stocks, TARGET)
    exp = TSForecastingExperiment()
    exp.setup(data=df, target=TARGET, coverage=COVERAGE, fold_strategy=FOLD_STRATEGY)
    exp.compare_models(sort='rmse')

if __name__ == "__main__":
    main()
