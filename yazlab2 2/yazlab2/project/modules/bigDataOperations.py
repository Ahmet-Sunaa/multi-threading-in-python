import pandas as pd


def dataOperations():
    columns = ['Product', 'Issue', 'Company',
               'State', 'Complaint ID', 'ZIP code']
    dtypes = {
        "Product": "category",
        "Issue": "category",
        "Company": "category",
        "State": "category",
        "Complaint ID": "uint16",
        "ZIP code": "category"
    }
    df = pd.read_csv('C:/Users/Muham/Desktop/yazlab2/project/data/rows.csv',
                     usecols=columns, low_memory=False, dtype=dtypes)
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.head(100)
    df = df.reset_index(drop=True)
    return df
