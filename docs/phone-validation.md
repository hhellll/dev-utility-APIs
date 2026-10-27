# Phone Number Validation API

Parse and validate **international phone numbers** in any format: get the number back in clean **E.164**, its country, the **carrier** the number block was allocated to, the **line type** (mobile / fixed line / VoIP / toll-free …), and its **timezones**. Numbers are processed **offline** against libphonenumber data, so lookups are fast and consistent. Bulk validation for up to 50 numbers per call.

**Live on RapidAPI → [Phone Number Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/phone-number-validation-api3)**

**Gateway host:** `phone-number-validation-api3.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/phone`

Every call goes to `https://phone-number-validation-api3.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `phone-number-validation-api3.p.rapidapi.com` |

## Endpoints

### `GET /validate?number=%2B6281212345678&region=ID`

Validate one number. `number` can be in international (`+62…`) or national format; `region` (ISO country code) is used to interpret national-format numbers and is optional for `+`-prefixed input.

**Response:** JSON including:

```json
{
  "valid": true,
  "e164": "+6281212345678",
  "country_name": "Indonesia",
  "carrier": "Telkomsel",
  "line_type": "mobile",
  "timezones": ["Asia/Jakarta"]
}
```

### `POST /validate`

Same check with a JSON body: `{ "number": "+6281212345678", "region": "ID" }`.

### `POST /bulk`

Validate up to **50** numbers in one call.

JSON body: `{ "numbers": ["+6281212345678", "+14155552671"], "region": "ID" }` (`region` optional)

**Response:** a `count` plus a `results` array with one validation object per number.

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

> **Honest limitation:** validation is offline (libphonenumber data), **not** a live HLR lookup. The carrier shown is the network the number block was originally allocated to — a ported number may now sit on a different network — and "valid" means the number is correctly formed and in an allocated range, not that a specific handset is currently reachable.

## Example (cURL)

```bash
curl "https://phone-number-validation-api3.p.rapidapi.com/validate?number=%2B6281212345678&region=ID" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: phone-number-validation-api3.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $5 / month | 10,000 / month |

The PRO plan is a soft limit with per-request overage of $0.003 per additional request.

Subscribe and manage your plan here: **[Phone Number Validation API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/phone-number-validation-api3)**

Part of the [hhelll API family](../README.md#the-api-catalog).
