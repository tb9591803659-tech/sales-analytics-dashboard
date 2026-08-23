import pandas as pd


def fix_datatypes(df):

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

    return df

def handle_missing_values(df):

    # Postal Code is not required for our dashboard analysis.
    # Keep rows even when Postal Code is missing.

    return df

def remove_duplicates(df):

    df = df.drop_duplicates()

    return df

def validate_values(df):

    if (df["Sales"] < 0).any():
        print("Warning: Negative sales found.")

    if (df["Sales"] == 0).any():
        print("Warning: Zero sales found.")

    return df

def clean_data(df):

    df = fix_datatypes(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = validate_values(df)

    return df

def validate_cleaned_data(df):

    print("\n========== DATA VALIDATION ==========")

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nNegative Sales:")
    print((df["Sales"] < 0).sum())

    print("\nZero Sales:")
    print((df["Sales"] == 0).sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nRequired Columns:")
    print(df.columns.tolist())

    print("\nDate Validation: ")
    print("Order Date datetime :",pd.api.types.is_datetime64_any_dtype(df["Order Date"]))

    print("Ship Date datetime :",pd.api.types.is_datetime64_any_dtype(df["Ship Date"]))

    required_columns = [
        "Row ID",
        "Order ID",
        "Order Date",
        "Ship Date",
        "Ship Mode",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Postal Code",
        "Region",
        "Product ID",
        "Category",
        "Sub-Category",
        "Product Name",
        "Sales"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    print("\nMissing Required Columns:")
    print(missing_columns)

    print("\nData validation completed successfully.")