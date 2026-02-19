# Order management module
from bot.client import BinanceClient
from bot.validators import OrderRequest
from bot.logger import logger

client = BinanceClient()

def place_trade(order: OrderRequest):
    try:
        response = client.place_order(
            symbol=order.symbol,
            side=order.side,
            order_type=order.order_type,
            quantity=order.quantity,
            price=order.price
        )

        print("\n" + "="*60)
        print("✅ ORDER PLACED SUCCESSFULLY")
        print("="*60)
        print(f"Symbol     : {response['symbol']}")
        print(f"Side       : {response['side']}")
        print(f"Type       : {response['type']}")
        print(f"Order ID   : {response['orderId']}")
        print(f"Status     : {response['status']}")
        print(f"Quantity   : {response.get('origQty')}")
        if response.get('avgPrice'):
            print(f"Avg Price  : {response.get('avgPrice')}")
        print(f"Executed   : {response.get('executedQty')}")
        print("="*60)

        return response

    except Exception as e:
        print(f"\n❌ Failed to place order: {e}")
        raise
