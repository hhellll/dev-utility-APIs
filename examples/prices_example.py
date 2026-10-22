"""Currency and Crypto Prices API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python prices_example.py

Converts USD -> IDR, fetches the BTC spot price, and a small multi-symbol
snapshot. Prices are cached/delayed reference data (see the `updated_at`
field in every response).

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/currency-and-crypto-prices-api
"""

import json
import os
import sys

import requests

HOST = "currency-and-crypto-prices-api.p.rapidapi.com"
BASE = f"https://{HOST}"


def get(key: str, path: str, params: dict) -> dict:
    r = requests.get(
        f"{BASE}{path}",
        headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST},
        params=params,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    print("Convert 10 USD -> IDR:")
    print(json.dumps(get(key, "/fiat/convert", {"from": "USD", "to": "IDR", "amount": 10}), indent=2))

    print("\nBTC price:")
    print(json.dumps(get(key, "/crypto/price", {"symbol": "BTC"}), indent=2))

    print("\nBTC, ETH, SOL:")
    print(json.dumps(get(key, "/crypto/prices", {"symbols": "BTC,ETH,SOL"}), indent=2))


if __name__ == "__main__":
    main()
