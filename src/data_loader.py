import pandas as pd
def load_data(filepath):

    try:
        df = pd.read_csv(filepath)

        df["Order.Date"] = pd.to_datetime(
            df["Order.Date"],
            errors="coerce"
        )

        df["Ship.Date"] = pd.to_datetime(
            df["Ship.Date"],
            errors="coerce"
        )

        print("CSV File Loaded Successfully")
        return df

    except Exception as e:
        print("Error while loading csv:", e)
        return None