# Domain Health API

One call tells you whether a domain is **set up properly**: live **DNS** records, **SSL certificate** status and expiry, **RDAP/whois** registration data, and **email security** posture (SPF, DMARC, MTA-STS) — rolled up into a **0–100 health score with an A–F grade** and a list of concrete issues. Run the full check or query each part separately.

**Live on RapidAPI → [Domain Health API](https://rapidapi.com/Hitler-HlDevZDwP/api/domain-health-api)**

**Gateway host:** `domain-health-api.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/domain`

Every call goes to `https://domain-health-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `domain-health-api.p.rapidapi.com` |

## Endpoints

### `GET /check?domain=google.com`

The full health check: DNS, SSL, RDAP, and email security, plus the score.

**Response:** JSON including:

```json
{
  "domain": "google.com",
  "health": { "score": 100, "grade": "A", "issues": [] }
}
```

For google.com the full response also shows registrar "MarkMonitor Inc.", registration expiring 2028-09-14, DMARC policy `reject`, MTA-STS present, and an SSL certificate issued by Google Trust Services for `*.google.com`, not expired. Domains with missing DMARC, expiring certificates, or DNS problems score lower and list each issue found.

### `GET /dns?domain=example.com`

DNS records only (A, AAAA, MX, NS, TXT, and more).

### `GET /ssl?domain=example.com`

SSL/TLS certificate only: issuer, subject, SANs, validity window, days left, expiry flag.

### `GET /email-security?domain=example.com`

Email security only: SPF record and validity, DMARC record and policy, MTA-STS presence.

### `GET /rdap?domain=example.com`

Registration data only (RDAP — the modern whois): registrar, created/expires dates, status, nameservers.

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl "https://domain-health-api.p.rapidapi.com/check?domain=google.com" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: domain-health-api.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $10 / month | 30,000 / month |
| ULTRA | $25 / month | 100,000 / month |
| MEGA | $49 / month | 300,000 / month |

Paid plans are soft limits with per-request overage ($0.003 PRO / $0.002 ULTRA / $0.001 MEGA).

Subscribe and manage your plan here: **[Domain Health API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/domain-health-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
