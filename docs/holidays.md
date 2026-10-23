# Holidays and Business Days API

Public holidays and working-day math for **200+ countries**: full-year holiday calendars, **"is this date a holiday?"** and **"is this a workday?"** checks, **business-day counting** between two dates, and **next-holiday** lookup. Built on the python-holidays dataset (MIT), including national subdivisions where the dataset provides them.

**Live on RapidAPI → [Holidays and Business Days API](https://rapidapi.com/Hitler-HlDevZDwP/api/holidays-and-business-days-api)**

**Gateway host:** `holidays-and-business-days-api.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/holidays`

Every call goes to `https://holidays-and-business-days-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `holidays-and-business-days-api.p.rapidapi.com` |

## Endpoints

### `GET /countries`

List all supported countries (and their subdivisions).

### `GET /holidays?country=ID&year=2026`

All public holidays for a country and year. Add `subdiv` for regional calendars where supported.

**Response:** JSON like:

```json
{
  "country": "ID",
  "year": 2026,
  "count": 17,
  "holidays": [
    { "date": "2026-01-01", "name": "Tahun Baru Masehi", "weekday": "Thursday" },
    { "date": "2026-08-17", "name": "Hari Kemerdekaan Republik Indonesia", "weekday": "Monday" }
  ]
}
```

Indonesia has **17 public holidays in 2026** — the full list includes Tahun Baru Imlek, Isra Mikraj, Hari Raya Nyepi, Idul Fitri, Kenaikan Isa Almasih, Idul Adha, Tahun Baru Islam, Maulid Nabi, and Natal, each with its local name and weekday.

### `GET /is-holiday?country=ID&date=2026-08-17`

Is one specific date a public holiday? Returns the holiday name when it is.

### `GET /is-workday?country=ID&date=2026-08-17`

Is one specific date a working day (not a weekend, not a public holiday)?

### `GET /business-days?country=ID&from=2026-01-01&to=2026-01-31`

Count business days between two dates, excluding weekends and public holidays — for SLAs, delivery estimates, and payroll math.

### `GET /next?country=ID&from=2026-08-01`

The next public holiday on or after `from` (defaults to today).

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://holidays-and-business-days-api.p.rapidapi.com/holidays?country=ID&year=2026" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: holidays-and-business-days-api.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $9 / month | 10,000 / month |
| ULTRA | $19 / month | 50,000 / month |
| MEGA | $39 / month | 250,000 / month |

Paid plans are soft limits with per-request overage ($0.003 PRO / $0.002 ULTRA / $0.001 MEGA).

Subscribe and manage your plan here: **[Holidays and Business Days API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/holidays-and-business-days-api)**

## Data license

Holiday data comes from the [python-holidays](https://github.com/workalendar/python-holidays) project, released under the MIT License.

Part of the [hhelll API family](../README.md#the-api-catalog).
