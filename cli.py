# CLI interface module
import typer
from rich.console import Console
from rich.panel import Panel
from bot.validators import OrderRequest
from bot.orders import place_trade

app = typer.Typer(help="Binance Futures Testnet Trading Bot")
console = Console()

def run_place(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
):
    """Place a market or limit order on Binance Futures Testnet"""
    
    try:
        order_request = OrderRequest(
            symbol=symbol,
            side=side.upper(),
            order_type=order_type.upper(),
            quantity=quantity,
            price=price,
        )

        console.print(Panel(f"Placing {order_request.side} {order_request.order_type} order", 
                          style="bold cyan"))
        
        place_trade(order_request)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise


# Default command (when no subcommand is given)
@app.command()
def place(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading pair (e.g. BTCUSDT)"),
    side: str = typer.Option(..., "--side", "-S", help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", "-t", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Quantity to trade"),
    price: float = typer.Option(None, "--price", "-p", help="Price (required for LIMIT)"),
):
    """Place a market or limit order on Binance Futures Testnet"""
    run_place(symbol, side, order_type, quantity, price)


# Callback to handle the case when no subcommand is provided (cli.py --symbol ...)
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    symbol: str = typer.Option(None, "--symbol", "-s", help="Trading pair (e.g. BTCUSDT)"),
    side: str = typer.Option(None, "--side", "-S", help="BUY or SELL"),
    order_type: str = typer.Option(None, "--type", "-t", help="MARKET or LIMIT"),
    quantity: float = typer.Option(None, "--quantity", "-q", help="Quantity to trade"),
    price: float = typer.Option(None, "--price", "-p", help="Price (required for LIMIT)"),
):
    """Binance Futures Testnet Trading Bot"""
    # If options are provided, run the place command
    if symbol and side and order_type and quantity is not None:
        run_place(symbol, side, order_type, quantity, price)
    elif ctx.invoked_subcommand is None:
        # Show help if no options and no subcommand
        typer.echo(ctx.get_help())


if __name__ == "__main__":
    app()
