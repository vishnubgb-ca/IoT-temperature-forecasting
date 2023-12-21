import pandas as pd
import numpy as np
from data_preprocessing import data_preprocess
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_numeric_dtype

def feature_engineering():

    data = data_preprocess()
    le=LabelEncoder()
    def remove_outliers(data,par):
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data=data.drop(index=i,inplace=True)
        return data 
    data.drop_duplicates()
    for j in data.columns:
        if is_numeric_dtype(data[j]): 
            data = remove_outliers(data,j)
    # data.set_index('noted_date',inplace = True)
    data = data.resample('T').mean().fillna(method='ffill')
    print(data.head())
    data.to_csv("iot_temp_series.csv",index=True)
    return data

feature_engineering()