import pandas as pd

def extract_data():
    df = pd.read_csv("IOT-temp.csv", index_col='noted_date')
    df.index = pd.to_datetime(df.index,format='mixed')
    print(df.head())
    return df

extract_data()
