# Website Security Scanner API

Version history: [CHANGELOG](../CHANGELOG.md).

Free live demo (summary only, no signup): https://149-118-58-54.sslip.io/secscan-demo/ — currently v2.2.0.

**Version:** 2.2.0

One call gives any public website a **passive security audit**: **HTTPS enforcement** and **TLS health** (certificate validity and expiry, negotiated protocol, legacy TLS 1.0/1.1 support), the six critical **security headers**, **cookie flags**, **server version disclosure**, **DNS and email security** (SPF, DMARC, best-effort DKIM selectors, and CAA), **security.txt**, **HSTS preload status**, **TLS cipher detail**, a **Certificate Transparency subdomain surface**, detected **technology and versions** (WordPress, PHP, jQuery, server software) matched against **live CVE intelligence** — NVD and OSV records enriched with EPSS exploit-probability scores and CISA KEV active-exploitation status, publicly **exposed sensitive files** such as `/.env` and `/.git`, and **mixed content**, plus **scan history and change diffs** for repeat scans by the same caller — all rolled into a **0–100 score with an A–F grade** and structured findings with concrete recommendations.

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

**New in v2.2.0:** advanced passive checks now run for **all plans** (they were previously locked behind retired tiers). The PRO full report carries them under `checks`: `checks.dns_email`, `checks.security_txt`, `checks.hsts_preload`, TLS cipher detail inside `checks.tls`, and `checks.subdomains`. The compact BASIC report carries the same advanced results in summary form — `categories.dns_email`, `categories.security_txt`, an `advanced` block, and a compact `subdomains` block. Every `/scan` response also includes a `changes` object (see below).

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan — a domain or a full URL, e.g. `https://example.com` |

**Response:** JSON like (real output for `https://www.spacex.com`, response time ~3.2 s; findings excerpted):

```json
{
  "url": "https://www.spacex.com",
  "score": 67,
  "grade": "C",
  "summary": { "critical": 0, "high": 1, "medium": 2, "low": 3, "info": 2 },
  "findings": [
    { "severity": "high", "title": "Sensitive file exposed: /server-status" },
    { "severity": "medium", "title": "Deprecated TLS protocols enabled" },
    { "severity": "medium", "title": "HTTP traffic is not redirected to HTTPS" },
    { "severity": "low", "title": "Missing X-Content-Type-Options header" },
    { "severity": "low", "title": "Missing Referrer-Policy header" },
    { "severity": "low", "title": "Missing Permissions-Policy header" },
    { "severity": "info", "title": "security.txt published" },
    { "severity": "info", "title": "DKIM record found" }
  ]
}
```

Even spacex.com does not score 100 — a scan of www.spacex.com turned up an exposed /server-status file (a high-severity finding), deprecated TLS protocols still enabled, and HTTP traffic on the www host that is not redirected to HTTPS. Sites with no HTTPS, exposed files, or end-of-life software score much lower and list every issue found.


#### v2.2.0 response fields

- `checks.dns_email` (PRO full report): `{domain, spf_present, dmarc_present, dmarc_policy, caa_present, dkim_selectors_checked, dkim_found}`. DKIM is best-effort: the common selectors `google`, `default`, `mail`, `selector1`, and `selector2` are checked. In the compact BASIC report the DNS/email results appear as `categories.dns_email` plus an `advanced` block: `{spf_present, dmarc_present, dmarc_policy, caa_present, dkim_found, security_txt_present, hsts_preload}`.
- `checks.security_txt` (PRO): `{present, location}`. BASIC exposes `categories.security_txt` and `advanced.security_txt_present`.
- `checks.hsts_preload` (PRO): `{status}`. BASIC exposes `advanced.hsts_preload`.
- `checks.tls` (PRO): negotiated protocol and cipher detail. A weak negotiated cipher is a finding (-5).
- `checks.subdomains` (PRO): `{domain, count, domains, truncated, source, note}` with `domains` capped at 50 and `source` set to `"crt.sh"`. BASIC returns the compact form `{count, domains, truncated}` with `domains` capped at 10. The Certificate Transparency lookup is cached for 1 hour and is fail-soft: if crt.sh is unavailable, the scan still completes without the subdomain section.
- `changes` (all plans, on every `/scan`): `{first_scan, score_delta, new_findings, resolved_findings, cert_expiry_days}`, computed against the same caller's previous scan of the same host. History is keyed per user via the RapidAPI caller headers, so callers only ever see their own scan history.

**Scoring for the new checks:** missing SPF -2; missing DMARC -5; DMARC policy `p=none` -2; missing security.txt -2 (low), while a published security.txt is an info finding ("security.txt published"); missing CAA -2 (low, "No CAA record found"); a found DKIM record is an info finding ("DKIM record found"); a domain on the HSTS preload list is an info finding ("Domain is on the HSTS preload list"); a weak negotiated cipher -5.

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

### `GET /cve/search?product=wordpress&version=5.7.2`

Looks up known vulnerabilities for a product and (optionally) an exact version, matched live against NVD and OSV data and enriched with EPSS scores and CISA KEV exploitation status.

| Parameter | Required | Notes |
|---|---|---|
| `product` | yes | One of: apache_http_server, nginx, wordpress, php, jquery, log4j, openssl, bootstrap, iis, litespeed (common aliases such as apache, httpd, wp and log4j2 are accepted) |
| `version` | no | Exact product version. With a version, results are confirmed matches for that version. Without one, only CISA KEV records for the product family are returned and every result is labelled as a potential finding |

Each result carries the CVE id, CVSS base score (when published), the EPSS exploit-probability score and percentile, a CISA KEV flag (actively exploited, with the date it was added), and a composite risk score (see [CVE intelligence](#cve-intelligence)). All plans return the full result list with scores and detail — the plans differ only in monthly quota.

### `GET /cve/{cve_id}`

Returns one CVE record: summary, CVSS base score and vector, publication date, EPSS score and percentile, the full CISA KEV entry when the CVE is being actively exploited (including known ransomware use and the required action), references, and the composite risk score. All plans receive the full record — the plans differ only in monthly quota.


### `GET /scan/history?host=example.com`

Returns the calling user's previous scans for one host, newest first, at most 20 entries. History is keyed per user via the RapidAPI caller headers.

| Parameter | Required | Notes |
|---|---|---|
| `host` | yes | The host to look up, e.g. `example.com` |

**Response:**

```json
{ "host": "example.com", "plan": "pro", "count": 2, "scans": [ { "scanned_at": "2026-10-27T09:00:00Z", "host": "example.com", "plan": "pro", "score": 76, "grade": "B" } ] }
```

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

### `POST /scan/deep`

Starts an asynchronous **deep scan** — a Nuclei-powered active template scan of one host (exposures, misconfigurations, known-CVE templates) plus a deep TLS analysis (testssl.sh) — and queues it for execution. For domains you have verified as yours (see `/scan/verify` below), the job also crawls the site and runs active DAST checks (XSS, SQL injection, SSRF, including out-of-band detection). Available on the **PRO** plan; each executed scan consumes **1 deep scan credit** (see [Plans and what you get](#plans-and-what-you-get)).

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan — one host per job |
| `auth_cookie` | no | Cookie header value for authenticated DAST (e.g. a session cookie). Only sent to the job's own host, only during the DAST stage, and wiped when the job finishes |
| `auth_headers` | no | JSON object of extra headers for authenticated DAST, same handling as `auth_cookie` |

**Response `202 Accepted`:**

```json
{ "job_id": "ds_9f27c1a4b8", "status": "queued" }
```

Then poll `GET /scan/deep/{job_id}` for the result. The credit is consumed when execution *starts*, and stays consumed even if the target turns out to be unreachable or blocks the scanner — the work was performed. Requests rejected before execution (invalid URL, private/internal target) never consume a credit.

### `GET /scan/deep/{job_id}`

Returns the status of a deep scan job — `queued`, `running`, or `done` with the full findings list. Only the API key that created the job can read it. Polling never consumes deep scan credits.


### `POST /scan/deep/batch`

Queues **deep scans for multiple hosts in one request**. This is a **PRO** feature (BASIC requests return `403`). Each host consumes **1 deep scan credit from the same pool as single deep scans** — 25 per month, max 5 per day. If the remaining quota covers only part of the batch, the covered hosts are accepted and the rest are returned in `rejected[]` with a per-host reason. Poll each accepted job with `GET /scan/deep/{job_id}`.

**Error codes (deep scan endpoints):**

| Code | Meaning |
|---|---|
| `400` | Invalid URL, or the target resolves to a private/internal address — rejected before execution, no credit consumed |
| `403` | Your plan does not include deep scans (BASIC), or the job belongs to a different API key |
| `429` | Deep scan credits for this month are exhausted, or your plan's daily deep scan cap was reached |

### `POST /scan/verify`

Starts **domain ownership verification** (PRO only). Returns a token
plus placement instructions. Verify a domain once to unlock DAST checks
in deep scans of that domain — active testing is only ever run against
domains the caller has proven they control.

| Parameter | Required | Notes |
|---|---|---|
| `domain` | yes | The domain to verify (a full URL works too) |

**Response `200`:**

```json
{
  "domain": "example.com",
  "status": "pending",
  "token": "hhelll-verify-...",
  "methods": {
    "file":    { "url": "https://example.com/.well-known/hhelll-verify.txt", "content": "hhelll-verify-..." },
    "dns_txt": { "host": "example.com", "value": "hhelll-verify-..." }
  }
}
```

### `POST /scan/verify/confirm`

Checks whether the token from `/scan/verify` is live yet — either as
the exact content of the well-known file, or inside a DNS TXT record
for the domain. Returns `{ "verified": true, "method": "file" }` (or
`"dns_txt"`), or `{ "verified": false }` with a hint when the token is
not found yet. Re-calling after success is safe and reports the stored
status.

Deep scan results carry a `tls_deep` block on every job. A `dast`
block appears when DAST ran (crawled endpoints, findings, summary);
for unverified domains it contains a `skipped` note instead. DAST
findings carry a `confidence` label (`confirmed`, `likely`,
`reported`, `unverified`): where a verification strategy exists, the
finding is replayed and compared against a benign control request
before the label is assigned, and `verification` explains the basis.

### `POST /scan/monitor`

Registers a domain for **recurring passive monitoring** (PRO only).
The scanner re-checks the domain on the chosen interval and stores
the score, grade and a change diff for every run.

| Parameter | Required | Notes |
|---|---|---|
| `domain` | yes | The domain to monitor (a full URL works too) |
| `interval_hours` | no | Re-check interval, 1-168 hours (default 24) |

### `GET /scan/monitor` and `GET /scan/monitor/{monitor_id}`

List your monitors / fetch one monitor, including `last_score`,
`last_grade`, `last_run_at` and `last_changes` — the latest run's diff
(`score_delta`, `new_findings`, `resolved_findings`,
`cert_expiry_days`).

### `DELETE /scan/monitor/{monitor_id}`

Stops a monitor (it stays listed with `active: false`).

Every passive scan also includes `checks.malware_reputation`: a
*lite* reputation verdict (`listed`, `suspicious` or `clean`) from the
Spamhaus DBL and SURBL domain blocklists plus URL heuristics. A
blocklist listing adds a high-severity finding. It is a reputation
check, not a full malware scan.

## What gets checked

- **HTTPS & redirects** — is plain HTTP redirected to HTTPS?
- **TLS** — certificate valid and not about to expire, strong negotiated protocol, legacy TLS 1.0/1.1 disabled.
- **Security headers** — Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, frame protection, Referrer-Policy, Permissions-Policy.
- **Cookies** — Secure, HttpOnly, and SameSite flags on every `Set-Cookie`.
- **Disclosure** — version numbers leaked in `Server` / `X-Powered-By` headers.
- **Technology & versions** — WordPress, PHP, jQuery, and server software versions matched live against NVD and OSV vulnerability data, enriched with EPSS scores and CISA KEV exploitation status (see [CVE intelligence](#cve-intelligence)), on top of curated notes such as end-of-life PHP versions.
- **Exposed files** — `/.env`, `/.git/HEAD`, `/.git/config`, `/.DS_Store`, `/phpinfo.php`, `/server-status`, `/.svn/entries`. Only the accessibility status is reported — file contents are never returned.
- **Mixed content & listings** — HTTPS pages loading HTTP resources, and WordPress upload directory listing.
- **DNS & email security** — SPF, DMARC (including its policy), CAA, and best-effort DKIM selector checks.
- **security.txt & HSTS preload** — whether a security.txt file is published, and whether the domain is on the HSTS preload list.
- **Subdomain surface** — subdomains discovered via Certificate Transparency (crt.sh), cached for 1 hour and fail-soft.
- **Change tracking** — repeat scans by the same caller include a `changes` diff (score delta, new and resolved findings, certificate expiry days), and past scans are available via `GET /scan/history`.

## CVE intelligence

Since version 2.1 the scanner does not rely on a hand-written list of known issues. Version 2.2.0 keeps the CVE endpoints unchanged and adds the advanced passive checks, subdomain surface, scan history, and change diffs described in this document. Detected technologies and versions are matched against live vulnerability data, and two lookup endpoints expose the same data directly.

**Data sources**

- **NVD** (National Vulnerability Database) and **OSV** (osv.dev) — the vulnerability records themselves, matched by exact product and version (NVD CPE matching for server and CMS software, OSV for library ecosystems such as Maven and npm).
- **EPSS** (FIRST.org) — a daily probability score (0 to 1) that a CVE will be exploited in the wild, mirrored locally and refreshed every day.
- **CISA KEV** (Known Exploited Vulnerabilities catalog) — the set of CVEs confirmed to be actively exploited, mirrored locally and refreshed every day, including known ransomware use.

**Confidence labels.** A match made with an exact detected version is `exact_version`: the CVE genuinely applies to that version, it appears in the findings, and it lowers the scan score by risk tier (all CVE-related deductions combined are capped). When a product is detected but its version cannot be confirmed, matches are `product_only`: they are listed as potential findings for the product family, are clearly labelled, and never lower the score.

**Composite risk score (secscan-risk-v1).** Every CVE gets one 0 to 100 score:

```
base = 0.6 x (CVSS base score x 10) + 0.4 x (EPSS x 100)
```

When only one of CVSS or EPSS is published, the base is that component alone. A CVE listed in CISA KEV is floored at 85, and at 90 when CISA records known ransomware use. Bands: 90+ critical, 70+ high, 40+ medium, above 0 low.

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
| PRO | $5 / month | 1,000 / month |

The PRO plan is a soft limit with per-request overage of $0.01 per additional request.

Subscribe and manage your plan here: **[Website Security Scanner API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)**

## Plans and what you get

| | **BASIC — Free** | **PRO — $5/mo** |
|---|---|---|
| Passive scans / month | 2 (hard limit) | 1,000 (+$0.01/request overage) |
| Report detail | **Summary only** — score, grade, pass/fail per category, finding counts | **Full report** — every finding with evidence & fix recommendations |
| CVE intelligence (live matching in scan reports, /cve/search, /cve/{cve_id}) | Full records | Full records |
| Deep scan credits / month (Nuclei-powered active template scan, single and batch share this pool) | — | 25 (max 5/day) |
| Scan history & change diffs (`changes` on every `/scan`, `GET /scan/history`) | Included, keyed to the calling user | Included, keyed to the calling user |
| Batch deep scans (`POST /scan/deep/batch`) | — (403) | Available; partial acceptance with `rejected[]` when the deep scan quota is short |

**Deep scan rules:** 1 credit = 1 host scanned. A scan that has been executed consumes its credit even if the target turns out to be unreachable or blocks the scanner — the work was performed. Invalid URLs and private/internal targets are rejected *before* execution and never consume a credit. Checking a job's status or fetching its result never consumes credits.

Part of the [hhelll API family](../README.md#the-api-catalog).
