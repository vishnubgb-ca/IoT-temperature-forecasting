import pandas as pd
from data_analysis import data_analysis
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy import stats

def data_preprocess():
    data = data_analysis()
    data.rename({"noted_date":"date"},inplace=True)
    data.drop(columns=['id','out/in','room_id/id'], inplace=True)
    print(f'dataset shape (rows, columns) - {data.shape}')
    data = data.replace(to_replace = -9999, value = np.nan)
    data.ffill(inplace=True)
    print(data[data.isnull()].count())
    print(data.head())
    return data

data_preprocess()