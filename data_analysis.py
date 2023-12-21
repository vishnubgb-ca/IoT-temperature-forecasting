from loading_data import extract_data

def data_analysis():
    data=extract_data()
    print(data.head())
    print(data.tail())
    print(data.describe())
    print ("Rows     : " ,data.shape[0])
    print ("Columns  : \n" ,data.shape[1])
    print ("Features : \n" ,data.columns.tolist())
    print ("Missing values\n\n",data.isnull().any(),sep='')
    print ("Unique values\n\n",data.nunique(),sep='')
    print (data.info())
    return data

data_analysis()