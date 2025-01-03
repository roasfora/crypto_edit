import os
import pandas as pd
import requests

def fetch_bitcoin_price():
    """Fetch the current Bitcoin price from Coinbase API."""
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "timestamp": response.headers.get("Date"),  # Use server timestamp
            "price": float(data["data"]["amount"]),
            "currency": data["data"]["currency"]
        }
    else:
        raise Exception(f"Failed to fetch Bitcoin price: {response.status_code}")

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

    # Avoid warning by handling empty DataFrame edge case
    if not new_data.empty and not new_data.isna().all(axis=None):
        df = pd.concat([df, new_data], ignore_index=True)

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
    

