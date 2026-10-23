# Weather API - Global Forecast

> **Status: launching soon.** The service is built and running; the RapidAPI listing is not public yet. This page documents the API as it will launch — endpoints and (draft) pricing below.

Current conditions and a **7-day forecast** for any coordinates on Earth, plus a **geocoding** search that turns place names into coordinates. Data comes from Open-Meteo and is cached server-side for 30 minutes, so repeated lookups for the same area are fast.

## Endpoints

### `GET /weather?lat=-6.2&lon=106.8`

Current weather + 7-day daily forecast (temperatures in °C) for a location.

| Parameter | Required | Notes |
|---|---|---|
| `lat` | yes | Latitude |
| `lon` | yes | Longitude |

**Response:** JSON with `location` (including `timezone`), `current` conditions (temperature, humidity, apparent temperature, weather code, wind), a `daily` array (date, max/min temperature, sunrise, sunset, precipitation probability), and a `cached` flag.

### `GET /geocode?q=Jakarta`

Search for a place by name — returns up to 5 matches with `name`, `country`, `admin1`, `latitude`, `longitude`, and `timezone`. Feed the coordinates straight into `/weather`.

## Example (cURL, as it will work at launch)

```bash
curl "https://<gateway-host>/weather?lat=-6.2&lon=106.8" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: <gateway-host>"
```

(The RapidAPI gateway host will be published here when the listing goes live.)

## Pricing (draft)

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | — (at launch) |
| PRO | $10 / month | 10,000 / month |
| ULTRA | $29 / month | 100,000 / month |
| MEGA | $75 / month | 500,000 / month |

Part of the [hhelll API family](../README.md#the-api-catalog).
