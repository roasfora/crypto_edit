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



