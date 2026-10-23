# Website Security Scanner API

One call gives any public website a **passive security audit**: **HTTPS enforcement** and **TLS health** (certificate validity and expiry, negotiated protocol, legacy TLS 1.0/1.1 support), the six critical **security headers**, **cookie flags**, **server version disclosure**, detected **technology and versions** (WordPress, PHP, jQuery) matched against a curated list of **known issues and CVEs**, publicly **exposed sensitive files** such as `/.env` and `/.git`, and **mixed content** — all rolled into a **0–100 score with an A–F grade** and structured findings with concrete recommendations.

![Website Security Scanner API](../assets/website-security-scanner.jpg)

**Live on RapidAPI → [Website Security Scanner API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)**

**Gateway host:** `website-security-scanner-api.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/secscan`

Every call goes to `https://website-security-scanner-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `website-security-scanner-api.p.rapidapi.com` |

> **Passive by design:** the scanner only makes standard GET/HEAD requests and a TLS handshake — **no port scanning, no exploitation**. Targets on private or internal networks are **refused** (SSRF protection). A full scan typically takes **2–10 seconds** depending on the target.

The scan endpoints accept **GET** (query parameters) or **POST** (JSON body with the same field names).

## Endpoints

### `GET|POST /scan?url=https://example.com`

The full audit: score, grade, severity summary, every individual check, and the findings list.

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan — a domain or a full URL, e.g. `https://example.com` |

**Response:** JSON like (real output for `https://google.com`, response time ~2.6 s; findings excerpted):

```json
{
  "url": "https://google.com",
  "score": 76,
  "grade": "B",
  "summary": { "critical": 0, "high": 0, "medium": 2, "low": 3, "info": 0 },
  "findings": [
    { "severity": "medium", "title": "Deprecated TLS protocols enabled" },
    { "severity": "medium", "title": "Missing Content-Security-Policy header" },
    { "severity": "low", "title": "Missing X-Content-Type-Options header" },
    { "severity": "low", "title": "Missing Referrer-Policy header" },
    { "severity": "low", "title": "Cookies set without the HttpOnly flag" }
  ]
}
```

Even google.com does not score 100 — it still accepts deprecated TLS protocols and sends no CSP header on its homepage. Sites with no HTTPS, exposed files, or end-of-life software score much lower and list every issue found.

### `GET /headers?url=https://example.com`

Just the response-header part of the audit: the six security headers, cookie flags, and version disclosure (`Server` / `X-Powered-By`).

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to check |

### `GET /ssl?url=https://example.com`

Just the TLS part: certificate issuer and subject, validity window, days remaining, negotiated protocol and cipher, and whether legacy TLS 1.0/1.1 are still accepted.

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to check |

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## What gets checked

- **HTTPS & redirects** — is plain HTTP redirected to HTTPS?
- **TLS** — certificate valid and not about to expire, strong negotiated protocol, legacy TLS 1.0/1.1 disabled.
- **Security headers** — Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, frame protection, Referrer-Policy, Permissions-Policy.
- **Cookies** — Secure, HttpOnly, and SameSite flags on every `Set-Cookie`.
- **Disclosure** — version numbers leaked in `Server` / `X-Powered-By` headers.
- **Technology & versions** — WordPress, PHP, and jQuery versions matched against a curated list of known issues (for example jQuery CVE-2015-9251, CVE-2020-11022 and CVE-2020-11023, and end-of-life PHP versions).
- **Exposed files** — `/.env`, `/.git/HEAD`, `/.git/config`, `/.DS_Store`, `/phpinfo.php`, `/server-status`, `/.svn/entries`. Only the accessibility status is reported — file contents are never returned.
- **Mixed content & listings** — HTTPS pages loading HTTP resources, and WordPress upload directory listing.

## Example (cURL)

```bash
curl "https://website-security-scanner-api.p.rapidapi.com/scan?url=https://example.com" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: website-security-scanner-api.p.rapidapi.com"
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 2 / month (hard limit) |
| PRO | $12 / month | 1,000 / month |
| ULTRA | $29 / month | 5,000 / month |
| MEGA | $59 / month | 20,000 / month |

Paid plans are soft limits with per-request overage ($0.01 PRO / $0.006 ULTRA / $0.003 MEGA).

Subscribe and manage your plan here: **[Website Security Scanner API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
