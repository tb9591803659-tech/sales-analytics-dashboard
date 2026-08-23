from src.data_loader import load_data, save_data
from src.cleaner import clean_data,validate_cleaned_data

import os


filepath = input("Enter file name: ")

if not filepath.endswith(".csv"):
    filepath += ".csv"

filepath = os.path.join("data", filepath)

df = load_data(filepath)

if df is not None:

    df = clean_data(df)

    output_path = os.path.join("data", "cleaned_data.csv")

    save_data(df, output_path)

    validate_cleaned_data(df)