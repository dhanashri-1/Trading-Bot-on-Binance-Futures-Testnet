from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os
from bot.logger import logger

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET must be set in environment variables")

        self.client = Client(self.api_key, self.api_secret, testnet=True)
        logger.info("Binance Futures Testnet client initialized")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders")
                params.update({
                    "price": price,
                    "timeInForce": "GTC"
                })

            logger.info(f"Placing order: {params}")
            
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order placed successfully: {response['orderId']}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message} | Code: {e.code}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error placing order: {e}")
            raise
