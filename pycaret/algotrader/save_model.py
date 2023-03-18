import os
import warnings
from pycaret.utils import version
from pycaret.time_series import save_model
from config import *
from data_preprocessing import load_data, process_data
from model_selection import main

warnings.filterwarnings('ignore')

def save_best_model(model, model_name, path):
    save_model(model, model_name, path)

def main():
    version()
    stocks = load_data(DATA_URL)
    df = process_data(stocks, TARGET)
    exp = TSForecastingExperiment()
    exp.setup(data=df, target=TARGET, coverage=COVERAGE, fold_strategy=FOLD_STRATEGY)
    best_model = exp.compare_models(sort='rmse')
    
    # Save the best model to disk
    model_name = "best_model"
    model_path = os.path.join(os.getcwd(), model_name)
    save_best_model(best_model, model_name, model_path)
    print(f"Model saved as {model_name} in {model_path}")

if __name__ == "__main__":
    main()
