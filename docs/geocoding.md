# Geocoding API

Turn **place names into coordinates** and **coordinates back into places**, over a database of **236k populated places in 246 countries** (GeoNames cities500). Forward search with country filtering, reverse geocoding to the nearest named places, and a bonus endpoint for the **nearest postal codes** to any point.

**Live on RapidAPI → [Geocoding API](https://rapidapi.com/Hitler-HlDevZDwP/api/geocoding-api5)**

**Gateway host:** `geocoding-api5.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/geo`

Every call goes to `https://geocoding-api5.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `geocoding-api5.p.rapidapi.com` |

## Endpoints

### `GET /search?q=Semarang&country=ID&limit=10`

Forward geocoding: search places by name. `country` (ISO code) and `limit` are optional.

**Response:** JSON like:

```json
{
  "query": "Semarang",
  "count": 1,
  "results": [
    {
      "geoname_id": 1627896,
      "name": "Semarang",
      "country": "ID",
      "latitude": -6.99306,
      "longitude": 110.42083,
      "feature_code": "PPLA",
      "population": 1694740,
      "timezone": "Asia/Jakarta"
    }
  ]
}
```

(Full results also include admin region codes.)

### `GET /reverse?lat=-6.914&lng=107.609&limit=10&max_km=100`

Reverse geocoding: the nearest named places to a point, each with its distance. A lookup in Bandung returns the city itself 0.89 km away. `limit` defaults to 10; `max_km` caps the search radius (default 100).

### `GET /nearby-postal?lat=-6.2&lng=106.8&limit=10&max_km=25`

The nearest **postal codes** to a point (defaults: 10 results within 25 km) — handy for "which delivery zones cover this location?" questions.

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://geocoding-api5.p.rapidapi.com/search?q=Semarang" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: geocoding-api5.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $5 / month | 50,000 / month |

The PRO plan is a soft limit with per-request overage of $0.001 per additional request.

Subscribe and manage your plan here: **[Geocoding API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/geocoding-api5)**

## Data license

Place data is from [GeoNames](https://www.geonames.org/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: "Geographical data © GeoNames contributors, CC BY 4.0."

Part of the [hhelll API family](../README.md#the-api-catalog).
