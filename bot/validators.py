# Input validation module
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class OrderRequest(BaseModel):
    symbol: str = Field(..., description="Trading pair (e.g. BTCUSDT)")
    side: str = Field(..., description="BUY or SELL")
    order_type: str = Field(..., description="MARKET or LIMIT")
    quantity: float = Field(..., gt=0, description="Quantity to trade")
    price: Optional[float] = Field(None, gt=0, description="Price (required for LIMIT)")

    @field_validator('side')
    @classmethod
    def validate_side(cls, v):
        if v.upper() not in ['BUY', 'SELL']:
            raise ValueError('Side must be BUY or SELL')
        return v.upper()

    @field_validator('order_type')
    @classmethod
    def validate_order_type(cls, v):
        if v.upper() not in ['MARKET', 'LIMIT']:
            raise ValueError('Order type must be MARKET or LIMIT')
        return v.upper()

    @field_validator('symbol')
    @classmethod
    def validate_symbol(cls, v):
        return v.upper()

    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "BTCUSDT",
                "side": "BUY",
                "order_type": "MARKET",
                "quantity": 0.01
            }
        }
