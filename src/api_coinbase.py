import os
import pandas as pd
from datetime import datetime
import requests

def fetch_bitcoin_price():
    """Fetch the current Bitcoin price from Coinbase API."""
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "timestamp": datetime.strptime(response.headers.get("Date"), "%a, %d %b %Y %H:%M:%S %Z"),  # Convert timestamp
            "price": float(data["data"]["amount"]),
            "currency": data["data"]["currency"]
        }
    else:
        raise Exception(f"Failed to fetch Bitcoin price: {response.status_code}")

def save_to_csv(data, filename):
    """Save the data to a CSV file using Pandas."""
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)

    if os.path.isfile(filepath):
        df = pd.read_csv(filepath)
    else:
        df = pd.DataFrame(columns=["timestamp", "price", "currency"])

    new_data = pd.DataFrame([data])
    if not new_data.empty and not new_data.isna().all(axis=None):
        df = pd.concat([df, new_data], ignore_index=True)

    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")


    # Save the updated DataFrame to CSV
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

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
    

