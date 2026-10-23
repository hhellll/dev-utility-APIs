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

### `POST /scan/deep`

Starts an asynchronous **deep scan** — a Nuclei-powered active template scan of one host (exposures, misconfigurations, known-CVE templates) — and queues it for execution. Available on **PRO, ULTRA and MEGA**; each executed scan consumes **1 deep scan credit** (see [Plans and what you get](#plans-and-what-you-get)).

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan — one host per job |

**Response `202 Accepted`:**

```json
{ "job_id": "ds_9f27c1a4b8", "status": "queued" }
```

Then poll `GET /scan/deep/{job_id}` for the result. The credit is consumed when execution *starts*, and stays consumed even if the target turns out to be unreachable or blocks the scanner — the work was performed. Requests rejected before execution (invalid URL, private/internal target) never consume a credit.

### `GET /scan/deep/{job_id}`

Returns the status of a deep scan job — `queued`, `running`, or `done` with the full findings list. Only the API key that created the job can read it. Polling never consumes deep scan credits.

### `POST /scan/deep/batch`

Starts one deep scan job per URL — up to **20 URLs** in a single call, one credit per host. **MEGA plan only.**

| Parameter | Required | Notes |
|---|---|---|
| `urls` | yes | JSON array of up to 20 URLs |

**Response `202 Accepted`:** a list of `{ "url": ..., "job_id": ... }` entries, one per accepted host.

**Error codes (deep scan endpoints):**

| Code | Meaning |
|---|---|
| `400` | Invalid URL, or the target resolves to a private/internal address — rejected before execution, no credit consumed |
| `403` | Your plan does not include deep scans (BASIC), or the job belongs to a different API key |
| `429` | Deep scan credits for this month are exhausted, or your plan's daily deep scan cap was reached |

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

## Plans and what you get

| | **BASIC — Free** | **PRO — $12/mo** | **ULTRA — $29/mo** | **MEGA — $59/mo** |
|---|---|---|---|---|
| Passive scans / month | 2 (hard limit) | 1,000 (+$0.01/request overage) | 5,000 (+$0.006/request) | 20,000 (+$0.003/request) |
| Report detail | **Summary only** — score, grade, pass/fail per category, finding counts | **Full report** — every finding with evidence & fix recommendations | Full report | Full report |
| Advanced checks (SPF/DMARC, security.txt, HSTS preload, TLS cipher details, extended tech fingerprinting) | — | — | ✓ | ✓ |
| Deep scan credits / month (Nuclei-powered active template scan) | — | 25 (max 5/day) | 100 (max 15/day) | 300 (max 30/day) |
| Passive subdomain enumeration (deep scan) | — | — | ✓ | ✓ |
| Light port check (deep scan) | — | — | — | ✓ |
| Batch deep scan submit | — | — | — | ✓ |
| Queue priority | — | Standard | Priority | Highest |
| Scan result history | — | 7 days | 30 days | 90 days |

**Deep scan rules:** 1 credit = 1 host scanned. A scan that has been executed consumes its credit even if the target turns out to be unreachable or blocks the scanner — the work was performed. Invalid URLs and private/internal targets are rejected *before* execution and never consume a credit. Checking a job's status or fetching its result never consumes credits.

Part of the [hhelll API family](../README.md#the-api-catalog).
