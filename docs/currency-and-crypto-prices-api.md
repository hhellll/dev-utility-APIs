# Currency and Crypto Prices API

Simple, cheap access to **fiat exchange rates** (30+ currencies) and **crypto spot prices** (BTC, ETH, SOL, and any other Binance USDT pair). Responses are **cached server-side** (fiat: 1 hour, crypto: 60 seconds) and honestly labeled — every response carries `cached`, `updated_at`, and `source` fields, so you always know how fresh the number is. This is delayed reference data, not a real-time trading feed.

**Live on RapidAPI → [Currency and Crypto Prices API](https://rapidapi.com/Hitler-HlDevZDwP/api/currency-and-crypto-prices-api)**

**Gateway host:** `currency-and-crypto-prices-api.p.rapidapi.com`

Every call goes to `https://currency-and-crypto-prices-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `currency-and-crypto-prices-api.p.rapidapi.com` |

## Endpoints

### `GET /fiat/rates?base=USD`

Exchange rates for one base currency against 30+ currencies (rates sourced from the European Central Bank reference data via Frankfurter).

**Response:** JSON with a `rates` map, plus `cached` / `updated_at` / `source` fields.

### `GET /fiat/convert?from=USD&to=IDR&amount=10`

Convert an amount between two currencies.

| Parameter | Required | Notes |
|---|---|---|
| `from` | yes | Source currency code |
| `to` | yes | Target currency code |
| `amount` | yes | Amount to convert |

**Response:** `{ "rate": 18076.0, "result": 180760.0, "cached": true, ... }`

### `GET /crypto/price?symbol=BTC`

Spot price (USDT pair) plus 24h change, high, and low for one symbol.

**Response:** `{ "price": 81222.01, "price_change_percent_24h": -4.136, "high_24h": 84847.31, "low_24h": 80939.54, "source": "binance", "cached": false, ... }`

### `GET /crypto/prices?symbols=BTC,ETH,SOL`

Spot prices for several symbols in a single call (one bulk upstream fetch).

## Example (cURL)

```bash
curl "https://currency-and-crypto-prices-api.p.rapidapi.com/fiat/convert?from=USD&to=IDR&amount=10" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: currency-and-crypto-prices-api.p.rapidapi.com"
```

A runnable Python example is in [`examples/prices_example.py`](../examples/prices_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $9 / month | 25,000 / month |
| ULTRA | $25 / month | 150,000 / month |
| MEGA | $69 / month | 600,000 / month |

Subscribe and manage your plan here: **[Currency and Crypto Prices API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/currency-and-crypto-prices-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
