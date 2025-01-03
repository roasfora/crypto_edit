# tests/test_api_client.py
import pytest
from pydantic import ValidationError
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import BitcoinPriceModel
from src.api_coinbase import fetch_bitcoin_price

def test_fetch_bitcoin_price():
    # Fetch the data
    data = fetch_bitcoin_price()

    # Validate the data structure using the Pydantic model
    try:
        BitcoinPriceModel(**data)
    except ValidationError as e:
        pytest.fail(f"Data validation failed: {e}")

    # Additional assertions
    assert data["currency"] == "USD", "Currency should be USD"
    assert data["price"] > 0, "Price should be greater than 0"
