# IP Geolocation API

Look up any IP address and get its **country, region, city, coordinates, timezone, and ASN/organization** — served from a local database, so lookups are fast and there is no per-call upstream. Single lookups, caller-IP lookup, and batch lookups up to 100 IPs per call.

**Live on RapidAPI → [IP Geolocation API](https://rapidapi.com/Hitler-HlDevZDwP/api/ip-geolocation-api25)**

**Gateway host:** `ip-geolocation-api25.p.rapidapi.com`

Every call goes to `https://ip-geolocation-api25.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `ip-geolocation-api25.p.rapidapi.com` |

## Endpoints

### `GET /lookup/{ip}`

Look up one IP address.

**Response:** JSON like:

```json
{
  "ip": "8.8.8.8",
  "country": "United States",
  "country_code": "US",
  "region": null,
  "city": null,
  "postal": null,
  "latitude": 37.751,
  "longitude": -97.822,
  "timezone": "America/Chicago",
  "asn": "AS15169",
  "org": "Google LLC"
}
```

(Some fields are `null` when the database has no finer detail for that IP — normal for anycast/resolver addresses.)

### `GET /lookup`

Look up the **caller's** IP address (honors `X-Forwarded-For`).

### `POST /batch`

Look up many IPs in one call.

JSON body: `{ "ips": ["8.8.8.8", "1.1.1.1"] }` (max 100 IPs)

**Response:** JSON map of IP → the same lookup object as above. Invalid IPs are rejected with `400`.

## Example (cURL)

```bash
curl "https://ip-geolocation-api25.p.rapidapi.com/lookup/8.8.8.8" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: ip-geolocation-api25.p.rapidapi.com"
```

A runnable Python example is in [`examples/ipgeo_example.py`](../examples/ipgeo_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 100 / month (hard limit) |
| PRO | $10 / month | 50,000 / month |
| ULTRA | $29 / month | 300,000 / month |
| MEGA | $79 / month | 1,200,000 / month |

Subscribe and manage your plan here: **[IP Geolocation API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/ip-geolocation-api25)**

Part of the [hhelll API family](../README.md#more-apis-by-hhelll).
