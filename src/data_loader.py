import pandas as pd 
import os 
def load_data(filepath):

    try:
        df = pd.read_csv(filepath)
        print("CSV File Loaded Successfully")
        return df

    except Exception as e:
        print("Error while loading csv:",e)
        return None

def save_data(df, filepath):

    df.to_csv(filepath, index=False)

    print("Saved Cleaned CSV File Successfully")