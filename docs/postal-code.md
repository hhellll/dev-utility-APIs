# Worldwide Postal Code API

Look up postal codes **anywhere in the world** — not just the US. The database holds **1.8M postal codes across 122 countries** (GeoNames data): place name, region, and coordinates for every code, plus place search, **radius search**, and **distance between two postal codes**.

**Live on RapidAPI → [Worldwide Postal Code API](https://rapidapi.com/Hitler-HlDevZDwP/api/worldwide-postal-code-api)**

**Gateway host:** `worldwide-postal-code-api.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/postal`

Every call goes to `https://worldwide-postal-code-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `worldwide-postal-code-api.p.rapidapi.com` |

## Endpoints

### `GET /lookup?country=ID&code=10110`

Look up one postal code in one country.

**Response:** JSON like:

```json
{
  "country": "ID",
  "postal_code": "10110",
  "count": 1,
  "results": [
    { "place": "Gambir", "latitude": -6.1778, "longitude": 106.8269 }
  ]
}
```

(Full results also include admin region codes and names.)

### `GET /search?place=Bandung&country=ID&limit=50`

Find postal codes by **place name**. `country` is optional, `limit` defaults to 50.

### `GET /radius?lat=-6.2&lng=106.8&km=5&limit=200`

All postal codes within `km` kilometres of a point (defaults: 10 km, up to 200 results). A 5 km radius around central Jakarta returns 62 codes.

### `GET /distance?from_country=ID&from_code=10110&to_country=ID&to_code=40115`

Straight-line distance between two postal codes (or pass `from_lat`/`from_lng`/`to_lat`/`to_lng` directly). Jakarta 10110 → Bandung 40115 is 121.64 km.

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://worldwide-postal-code-api.p.rapidapi.com/lookup?country=ID&code=10110" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: worldwide-postal-code-api.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $9 / month | 25,000 / month |
| ULTRA | $19 / month | 100,000 / month |
| MEGA | $39 / month | 500,000 / month |

Paid plans are soft limits with per-request overage ($0.001 PRO / $0.0005 ULTRA / $0.0002 MEGA).

Subscribe and manage your plan here: **[Worldwide Postal Code API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/worldwide-postal-code-api)**

## Data license

Postal code data is from [GeoNames](https://www.geonames.org/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: "Postal code data © GeoNames contributors, CC BY 4.0."

Part of the [hhelll API family](../README.md#the-api-catalog).
