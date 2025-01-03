import os
import pandas as pd
from src.api_client import fetch_bitcoin_price

def save_to_csv(data, filename):
    """Save the data to a CSV file using Pandas."""
    # Ensure the 'data' folder exists
    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", filename)

    # Load existing data if the file exists
    if os.path.isfile(filepath):
        df = pd.read_csv(filepath)
    else:
        df = pd.DataFrame(columns=["timestamp", "price", "currency"])

    # Append the new data
    new_data = pd.DataFrame([data])  # Convert single record to DataFrame
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated DataFrame to CSV
    df.to_csv(filepath, index=False)

def main():
    try:
        # Fetch Bitcoin price data
        bitcoin_data = fetch_bitcoin_price()

        # Print and save the data
        print(bitcoin_data)
        save_to_csv(bitcoin_data, "bitcoin_prices.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
