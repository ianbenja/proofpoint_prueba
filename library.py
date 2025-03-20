import pandas as pd
from datetime import datetime

# Read the CSV file
try:
    df = pd.read_csv("library_collection.csv")

    # Verify that the required columns are present
    required_columns = ["Title", "Author", "Publication Year"]
    if not all(column in df.columns for column in required_columns):
        missing_columns = [col for col in required_columns if col not in df.columns]
        raise ValueError(f"The following columns are missing in the CSV file: {missing_columns}")

    # Convert titles and authors to lowercase
    df["Title"] = df["Title"].str.lower()
    df["Author"] = df["Author"].str.lower()

    # Remove rows without "Title"
    initial_count = len(df)
    df = df.dropna(subset=["Title"])
    removed_books_without_title = initial_count - len(df)
    print(f"Books without title removed: {removed_books_without_title}")

    # Fix missing authors
    unknown_author_count = df["Author"].isna().sum()
    df["Author"] = df["Author"].fillna("author unknown")
    print(f"Unknown authors replaced: {unknown_author_count}")

    # Fix invalid publication years
    df["Publication Year"] = pd.to_numeric(df["Publication Year"], errors="coerce")
    current_year = datetime.now().year
    invalid_years_count = (df["Publication Year"].isna().sum() + (df["Publication Year"] < 0).sum() + (df["Publication Year"] > current_year).sum())
    df["Publication Year"] = df["Publication Year"].fillna(0).clip(lower=0, upper=current_year).astype(int)
    print(f"Invalid publication years corrected: {invalid_years_count}")

    # Remove duplicates
    initial_count_before_dedup = len(df)
    df.drop_duplicates(inplace=True)
    removed_duplicates_count = initial_count_before_dedup - len(df)
    print(f"Duplicate books removed: {removed_duplicates_count}")

    # Sort by author and publication year
    df = df.sort_values(by=["Author", "Publication Year"])

    # Save the cleaned and sorted catalog
    df.to_csv("corrected_library_collection.csv", index=False)
    print("Cleaned and sorted catalog saved to 'corrected_library_collection.csv'")

except FileNotFoundError:
    print("Error: The file 'library_collection.csv' does not exist.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: The CSV file is not valid.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")