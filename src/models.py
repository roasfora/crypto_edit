from pydantic import BaseModel, Field
from datetime import datetime

class BitcoinPriceModel(BaseModel):
    timestamp: datetime = Field(..., description="The timestamp when the price was fetched")
    price: float = Field(..., gt=0, description="The current price of Bitcoin in the specified currency")
    currency: str = Field(..., min_length=3, max_length=3, description="The 3-letter currency code (e.g., 'USD')")

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2025-01-03T15:36:32",
                "price": 97387.9,
                "currency": "USD",
            }
        }
