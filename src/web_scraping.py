import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_eur_to_usd_rate():
    """Scrape EUR to USD exchange rate and save to a CSV file."""
    try:
        # URL for scraping
        url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract the exchange rate
            rate_element = soup.find("span", class_="ccOutputRslt")
            if rate_element:
                rate = float(rate_element.text.split()[0])

                # Prepare data for saving
                data = {
                    "timestamp": response.headers.get("Date"),
                    "eur_to_usd_rate": rate
                }

                # Save to CSV
                save_to_csv(data)
                print(f"EUR to USD Rate: {rate}")
            else:
                raise Exception("Could not find the exchange rate on the webpage.")
        else:
            raise Exception(f"Failed to fetch the webpage: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

def save_to_csv(data, filename="eur_to_usd_rates.csv"):
    """Save EUR to USD exchange rate data to a CSV file."""
    os.makedirs("data", exist_ok=True)  # Ensure the 'data' folder exists
    filepath = os.path.join("data", filename)

    # Load existing data if the file exists
    if os.path.isfile(filepath):
        df = pd.read_csv(filepath)
    else:
        df = pd.DataFrame(columns=["timestamp", "eur_to_usd_rate"])

    # Append the new data
    new_data = pd.DataFrame([data])
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated data back to CSV
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

# Run the function if this file is executed
if __name__ == "__main__":
    fetch_eur_to_usd_rate()
