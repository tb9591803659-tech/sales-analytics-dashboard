from src.data_loader import load_data
from src.cleaner import clean_data, validate_cleaned_data


RAW_DATA_PATH = "data/superstore.csv"
CLEANED_DATA_PATH = "data/cleaned_data.csv"


def main():

    print("Loading raw dataset...")

    df = load_data(RAW_DATA_PATH)

    if df is None:
        print("Failed to load raw dataset.")
        return

    print("\nCleaning dataset...")

    cleaned_df = clean_data(df)

    print("\nValidating cleaned dataset...")

    is_valid = validate_cleaned_data(cleaned_df)

    if not is_valid:
        print("\nData validation failed.")
        return

    cleaned_df.to_csv(
        CLEANED_DATA_PATH,
        index=False
    )

    print("\nCleaned dataset saved successfully.")
    print(f"File: {CLEANED_DATA_PATH}")
    print(f"Shape: {cleaned_df.shape}")


if __name__ == "__main__":
    main()