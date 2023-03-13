import pandas as pd
from pycaret import *

def create_pd():
    # read the csv file

    data = pd.read_csv('../../data/demand-forecasting-kernels-only/train.csv')
    data['date'] = pd.to_datetime(data['date'])

    # combine store and item column as time_series**
    data['store'] = ['store_' + str(i) for i in data['store']]
    data['item'] = ['item_' + str(i) for i in data['item']]
    data['time_series'] = data[['store', 'item']].apply(lambda x: '_'.join(x), axis=1)
    data.drop(['store', 'item'], axis=1, inplace=True)

    # extract features from date**
    data['month'] = [i.month for i in data['date']]
    data['year'] = [i.year for i in data['date']]
    data['day_of_week'] = [i.dayofweek for i in data['date']]
    data['day_of_year'] = [i.dayofyear for i in data['date']]

    return data

def find_model(df,column):
    """returs best model

    Args:
        df (_dataframe_): dataframe to be trained
        column (_string_): column name with data
    """

    all_ts=data['time_series']
