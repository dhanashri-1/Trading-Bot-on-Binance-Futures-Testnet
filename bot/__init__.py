"""
Binance Futures Trading Bot Package
"""

__version__ = "1.0.0"
__author__ = "Trading Bot Developer"

from bot.client import BinanceClient
from bot.orders import place_trade
from bot.validators import OrderRequest
from bot.logger import logger

__all__ = [
    "BinanceClient",
    "place_trade",
    "OrderRequest",
    "logger",
]
