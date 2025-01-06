import pytest
from src.web_scraping import fetch_eur_to_usd_rate

def test_fetch_eur_to_usd_rate():
    # Fetch the scraped data
    data = fetch_eur_to_usd_rate()

    # Assertions to validate the data structure
    assert "timestamp" in data, "Timestamp is missing in the data."
    assert "eur_to_usd_rate" in data, "Exchange rate is missing in the data."

    # Additional assertions
    assert isinstance(data["timestamp"], str), "Timestamp must be a string."
    assert isinstance(data["eur_to_usd_rate"], float), "Exchange rate must be a float."
    assert data["eur_to_usd_rate"] > 0, "Exchange rate must be positive."
