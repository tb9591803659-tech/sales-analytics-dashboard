import pandas as pd


def fix_column_names(df):

    # Rename Chinese column to English
    df = df.rename(columns={
        "记录数": "Record.Count"
    })

    return df


def fix_datatypes(df):

    # Convert date columns
    df["Order.Date"] = pd.to_datetime(
        df["Order.Date"],
        errors="coerce"
    )

    df["Ship.Date"] = pd.to_datetime(
        df["Ship.Date"],
        errors="coerce"
    )

    return df


def handle_missing_values(df):

    # Check missing values
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Postal Code is not present in this dataset,
    # so no Postal Code handling is required.

    return df


def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print("\nDuplicate Rows Removed:", before - after)

    return df


def validate_values(df):

    # Sales validation
    if (df["Sales"] < 0).any():
        print("Warning: Negative sales found.")

    if (df["Sales"] == 0).any():
        print("Warning: Zero sales found.")

    # Profit validation
    if (df["Profit"] < 0).any():
        print("Warning: Negative profit found.")

    # Quantity validation
    if (df["Quantity"] <= 0).any():
        print("Warning: Zero or negative quantity found.")

    # Discount validation
    if ((df["Discount"] < 0) | (df["Discount"] > 1)).any():
        print("Warning: Invalid discount values found.")

    return df


def clean_data(df):

    df = fix_column_names(df)
    df = fix_datatypes(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = validate_values(df)

    return df


def validate_cleaned_data(df):

    print("\n========== DATA VALIDATION ==========")

    # -------------------------------
    # 1. Dataset Shape
    # -------------------------------
    print("\nShape:")
    print(df.shape)

    # -------------------------------
    # 2. Missing Values
    # -------------------------------
    print("\nMissing Values:")
    print(df.isnull().sum())

    # -------------------------------
    # 3. Duplicate Rows
    # -------------------------------
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # -------------------------------
    # 4. Sales Validation
    # -------------------------------
    print("\nNegative Sales:")
    print((df["Sales"] < 0).sum())

    print("\nZero Sales:")
    print((df["Sales"] == 0).sum())

    # -------------------------------
    # 5. Profit Validation
    # -------------------------------
    print("\nNegative Profit:")
    print((df["Profit"] < 0).sum())

    print("\nZero Profit:")
    print((df["Profit"] == 0).sum())

    # -------------------------------
    # 6. Quantity Validation
    # -------------------------------
    print("\nNegative Quantity:")
    print((df["Quantity"] < 0).sum())

    print("\nZero Quantity:")
    print((df["Quantity"] == 0).sum())

    # -------------------------------
    # 7. Discount Validation
    # -------------------------------
    print("\nDiscount:")
    print(df["Discount"].describe())

    # -------------------------------
    # 8. Data Types
    # -------------------------------
    print("\nData Types:")
    print(df.dtypes)

    # -------------------------------
    # 9. Required Columns
    # -------------------------------
    required_columns = [
        "Category",
        "City",
        "Country",
        "Customer.ID",
        "Customer.Name",
        "Discount",
        "Market",
        "Record.Count",
        "Order.Date",
        "Order.ID",
        "Order.Priority",
        "Product.ID",
        "Product.Name",
        "Profit",
        "Quantity",
        "Region",
        "Row.ID",
        "Sales",
        "Segment",
        "Ship.Date",
        "Ship.Mode",
        "Shipping.Cost",
        "State",
        "Sub.Category",
        "Year",
        "Market2",
        "weeknum"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    print("\nMissing Required Columns:")
    print(missing_columns)

    # -------------------------------
    # 10. Date Validation
    # -------------------------------
    print("\nDate Validation:")

    print(
        "Order Date datetime:",
        pd.api.types.is_datetime64_any_dtype(
            df["Order.Date"]
        )
    )

    print(
        "Ship Date datetime:",
        pd.api.types.is_datetime64_any_dtype(
            df["Ship.Date"]
        )
    )

    # -------------------------------
    # 11. Business Metrics
    # -------------------------------
    print("\n========== BUSINESS METRICS ==========")

    print("\nTotal Sales:")
    print(df["Sales"].sum())

    print("\nTotal Profit:")
    print(df["Profit"].sum())

    print("\nTotal Quantity:")
    print(df["Quantity"].sum())

    print("\nAverage Discount:")
    print(df["Discount"].mean())

    print("\nTotal Shipping Cost:")
    print(df["Shipping.Cost"].sum())

    print("\nTotal Orders:")
    print(df["Order.ID"].nunique())

    print("\nTotal Customers:")
    print(df["Customer.ID"].nunique())

    print("\nTotal Products:")
    print(df["Product.ID"].nunique())

    print("\nData validation completed successfully.")