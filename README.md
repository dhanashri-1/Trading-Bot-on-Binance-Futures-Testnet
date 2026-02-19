# Binance Futures Testnet Trading Bot

Clean, professional trading bot for Binance USDT-M Futures Testnet.

## Features

- Market & Limit orders (BUY/SELL)
- Strong input validation with Pydantic
- Excellent structured logging
- Clean separation of concerns
- Beautiful CLI with Typer + Rich

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API credentials:

   Create a `.env` file in the project root with your Binance Testnet API credentials:
   ```
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   ```

   Get your credentials from: https://testnet.binancefuture.com/en/futures

## How to Run

### Place a MARKET order:
```bash
# Using subcommand
python3 cli.py place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# Without subcommand
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order:
```bash
python3 cli.py place --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 50000
```

### Command Options:
- `--symbol`, `-s`: Trading pair (e.g., BTCUSDT)
- `--side`, `-S`: BUY or SELL
- `--type`, `-t`: MARKET or LIMIT
- `--quantity`, `-q`: Quantity to trade
- `--price`, `-p`: Price (required for LIMIT orders)

## Log Files

Log files are stored in `logs/trading_bot.log` and include:
- Client initialization
- Order placement requests
- Order responses
- API errors

## Project Structure

```
binance-futures-trading-bot/
├── bot/
│   ├── __init__.py      # Package initialization
│   ├── client.py       # Binance API client wrapper
│   ├── logger.py       # Logging configuration
│   ├── orders.py       # Order placement logic
│   └── validators.py   # Input validation with Pydantic
├── logs/               # Log files directory
│   └── trading_bot.log
├── cli.py              # CLI entry point
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Assumptions

1. User has a Binance Futures Testnet account
2. User has generated API credentials with futures trading permissions
3. Orders are placed on USDT-M Futures (testnet)
4. Quantities are in the base currency (e.g., BTC for BTCUSDT)

## Requirements

- Python 3.9+
- python-binance==1.0.19
- typer[all]==0.9.0
- python-dotenv==1.0.0
- pydantic==2.5.3
