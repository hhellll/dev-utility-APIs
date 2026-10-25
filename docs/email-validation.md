# Email Validation API

Validate an email address **before** it lands in your database: syntax check, DNS/MX lookup, **disposable-domain detection** (9,900+ known throwaway domains), **role-based address detection** (admin@, support@, …), **typo suggestions** for common domains (gmial.com → gmail.com), and a **0–100 deliverability score** with a plain-language verdict. Bulk validation for up to 50 addresses per call.

**Live on RapidAPI → [Email Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/email-validation-api44)**

**Gateway host:** `email-validation-api44.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/email`

Every call goes to `https://email-validation-api44.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `email-validation-api44.p.rapidapi.com` |

## Endpoints

### `GET /validate?email=test@gmail.com`

Validate one address.

**Response:** JSON like:

```json
{
  "email": "test@gmail.com",
  "syntax_valid": true,
  "domain": "gmail.com",
  "has_mx": true,
  "score": 100,
  "verdict": "valid",
  "deliverable": true,
  "reason": "all checks passed"
}
```

The full response also reports disposable and role-based flags, a typo suggestion when the domain looks misspelled, and a risk breakdown behind the score. A disposable address (e.g. a mailinator.com inbox) scores low (30 in testing) with `verdict` making the reason obvious.

> **Honest limitation:** this API does **not** probe the remote mail server over SMTP, so the `smtp` and `catch_all` fields report `"not_checked"`. The score is based on syntax, DNS/MX, and list-based checks — which is what most signup-form and list-cleaning jobs actually need.

### `POST /validate`

Same check with a JSON body: `{ "email": "test@gmail.com" }`.

### `POST /bulk`

Validate up to **50** addresses in one call.

JSON body: `{ "emails": ["a@example.com", "b@example.org"] }`

**Response:** a `count` plus a `results` array with one validation object per address.

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://email-validation-api44.p.rapidapi.com/validate?email=test@gmail.com" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: email-validation-api44.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $5 / month | 5,000 / month |
| ULTRA | $15 / month | 25,000 / month |
| MEGA | $29 / month | 100,000 / month |

Paid plans are soft limits with per-request overage ($0.003 PRO / $0.002 ULTRA / $0.001 MEGA).

Subscribe and manage your plan here: **[Email Validation API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/email-validation-api44)**

Part of the [hhelll API family](../README.md#the-api-catalog).
