# Website Security Scanner API


Version history: [CHANGELOG](../CHANGELOG.md).


Free live demo (summary only, no signup): https://scan.hhelll.my.id — the official scanner site.

**Version:** 2.6.0

One call gives any public website a **passive security audit**: **HTTPS enforcement** and **TLS health** (certificate validity and expiry, negotiated protocol, legacy TLS 1.0/1.1 support), the six critical **security headers**, **cookie flags**, **server version disclosure**, **DNS and email security** (SPF, DMARC, best-effort DKIM selectors, CAA, MTA-STS, TLS-RPT, and DNSSEC), **security.txt**, **HSTS preload status**, **TLS cipher detail**, a **Certificate Transparency subdomain surface**, detected **technology and versions** (WordPress, PHP, jQuery, server software) matched against **live CVE intelligence** — NVD and OSV records enriched with EPSS exploit-probability scores and CISA KEV active-exploitation status, publicly **exposed sensitive files** such as `/.env` and `/.git`, and **mixed content**, plus **scan history and change diffs** for repeat scans by the same caller — all rolled into a **0–100 score with an A–F grade** and structured findings with concrete recommendations. Not scored, but visible in the report: the **next-generation header watchlist** (Cross-Origin-Opener-Policy, Cross-Origin-Embedder-Policy, Cross-Origin-Resource-Policy) and the report's **DNS/mail watchlist** entries (MTA-STS and TLS-RPT presence, DNSSEC status). Since v2.6.0, a **limited multi-page crawl** (up to 10 internal pages, PRO detail, not scored) also checks the crawled pages for mixed content and conservative, evidence-based injection signals. (PRO also offers deep scans with active testssl.sh TLS checks and Nuclei DAST — see [Deep scans](#deep-scans-pro).)

![Website Security Scanner API](../assets/website-security-scanner.jpg)

**Live on RapidAPI → [Website Security Scanner API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)**

**Gateway host:** `website-security-scanner-api.p.rapidapi.com`

**Public scanner site:** https://scan.hhelll.my.id — run the free summary scan in the browser, grab an embeddable score badge, or open a host's public report page.

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

**New in v2.2.0:** advanced passive checks now run for **all plans** (they were previously locked behind retired plans). **New in v2.5.0:** the DNS/mail and next-generation header watchlist items (below) are present and do not affect the score.

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

Even spacex.com does not score 100 — a scan of www.spacex.com turned up an exposed /server-status file, deprecated TLS protocols and missing headers.

#### v2.2.0 response fields

- `checks.dns_email` (PRO full report): `{domain, spf_present, spf_record, dmarc_present, dmarc_policy, dmarc_record, dkim, dkim_selectors_checked, caa_present, caa_records, mta_sts_present, tls_rpt_present, tls_rpt_record, dnssec: {ds_present, dnskey_present, signed}}` — all mail/DNS items; MTA-STS, TLS-RPT and DNSSEC are **watchlist entries, not scored** (see [Watchlist](#watchlist-not-scored)).
- `categories.dns_email` (BASIC summary): `{"score": boolean, "details": "SPF/DKIM/DMARC..."}` (a compact summary of the same DNS/email findings).
- `checks.security_txt` (PRO): `{present, url, valid}` — `present` requires an RFC 9116-conformant `security.txt` (responds as `text/plain`, non-HTML, with a `Contact:` line — plain 200 is not enough, since WAF and SPA fallbacks can fake one).
- `checks.hsts_preload` (PRO): `{in_preload, status}` — whether the domain is loaded in the Chromium preload list.
- `checks.tls_detail` (PRO): `{proto, protocols, ciphers, cert}` — finer TLS detail: negotiated protocol, supported protocols (`TLSv1.0`–`TLSv1.3`), exchange cipher, key length and the certificate.
- `checks.next_gen_headers` (PRO; `next_gen` on `/headers`): `{coop, coep, corp, entries}` — Cross-Origin-Opener-Policy, Cross-Origin-Embedder-Policy and Cross-Origin-Resource-Policy; each entry marked `"scored": false`. Also reported as an info finding, so the check is visible in the report.
- `checks.subdomains` (PRO): `{found, count, entries}` — Certificate Transparency subdomains, up to 50 entries; each `{"hostname", "first_seen"}`.
- `categories.accessibility` removed: mobile/font and `robots.txt` checks were dropped from the response (they were not security-relevant; outdated-browser warnings are no longer part of the score).
- `categories.tech`: this block now includes `cve_summary` (with `total`, `critical`, `high`, `exploitable` and `kev` counts) plus `technologies`, `software` and `vulnerable` matching with NVD and OSV correlation and EPSS scoring.
- `checks.malware_reputation` (all plans): `{blocklisted, lists, signals, note}` — Spamhaus DBL and SURBL lookups plus URL heuristics (IP-literal host, punycode, shortener, executable path). A blocklist hit adds a **high** finding. Deliberately described as a reputation check, not a full malware scan.
- `advanced` (BASIC summary): `{spf_present, dmarc_present, dkim_present, caa_present, mta_sts_present, tls_rpt_present, dnssec_signed, security_txt_present, hsts_preload, grade}` — compact boolean values of the same checks. (`mta_sts_present`, `tls_rpt_present` and `dnssec_signed` were added in v2.5.0 — they are watchlist entries and do not affect the score.)
- `changes` (all plans): `{first_scan, previous_score, score_delta, new_findings, resolved_findings, certificate_days_remaining}` — for repeat scans of the same host by the same caller; the first scan returns `first_scan: true`.
- `summary` by severity: use `summary` (`critical`, `high`, `medium`, `low`, `info`) — the old `total` key and `count` key are no longer returned.

#### v2.3.0 response fields

- `checks.header_quality`: PRO-only analysis of the *content* of CSP, HSTS, Referrer-Policy and Permissions-Policy. Missing headers are still reported by `checks.headers` as before — `header_quality` goes further and says when a present header is weak, e.g. a CSP without `default-src` / with `unsafe-inline` becomes a low/medium finding, an HSTS `max-age` under 6 months becomes a low finding, `X-Frame-Options: ALLOWALL` with `frame-ancestors` absent becomes a low finding, and a Permissions-Policy of `*` becomes a medium finding. Each entry has `header`, `present`, `value`, `score`, `issues` and `recommendations`.
- `fix`: a `fix` field is now present on PRO scan findings: ready-to-use configuration snippets for nginx, Apache, Cloudflare, WordPress/PHP, and DNS records, e.g. fix for `missing-header-csp` includes an nginx `add_header Content-Security-Policy "..."` line, and for SPf `fix` includes the DNS record to add. Not every finding has a fix yet — aggregate findings such as `tech-cve` have none by design.
- `changes` (all plans): compare a scan against your previous scan of that host — the *same* blocks as v2.2.0's `changes` (first scan?, score delta, new/resolved findings, certificate expiry) — see v2.2.0 above.
- `badge`: `GET /badge/{host}.svg` — also `GET /badge?host=example.com`.
- `report_url`: the PRO scan response already includes `report_url` to the public report page (scan.hhelll.my.id/report/{host}) — a public page with score, grade, per-category pass/fail, findings and a score history chart (summary-level data only).
- `monitoring` (`POST /scan/monitor`, PRO): creates a monitor for recurring passive scans of a domain: interval 1-168 hours, webhook_url optional. Response includes `{monitor_id, host, interval_hours}`.
- Webhooks: a monitor's webhook POSTs a JSON alert (`alert` `score_drop`, `critical_finding` or `certificate_expiry`) when the scan score drops by ≥5, a new critical or high finding appears, or the certificate expires within 14 days — `POST /scan/monitor/{id}/webhook` sets or updates a monitor's `webhook_url`.

#### v2.4.0 response fields

- `tls_deep` (PRO): `{"protocol_score", "key_exchange_score", "cipher_strength_score", "overall_score", "grade", "vulnerabilities", "heartbleed", "certificate", "forward_secrecy"}` based on testssl.sh, cached per host for 7 days.

#### v2.5.0 response fields

- `checks.dns_email` (PRO): `mta_sts_present`, `tls_rpt_present`, `tls_rpt_record` and `dnssec: { ds_present, dnskey_present, signed }` were newly added (in v2.4.0 only `spf_record`, `dkim_present`, `dmarc_policy` and `caa_present` for mail were available). These are watchlist fields only — informational findings, not scoring.
- `advanced` (BASIC summary): `mta_sts_present`, `tls_rpt_present`, `dnssec_signed` booleans now listed as watchlist fields.
- `next_gen`/`checks.next_gen_headers` (PRO): see the full description in the [v2.2.0 response fields](#v22response-fields) list above — these entries appear as `"scored": false` in the response and in info findings, and do not affect the score.

#### v2.6.0 response fields

- `checks.crawl` (PRO): `{status, scored: false, note, max_pages, budget_seconds, elapsed_ms, pages_discovered, pages_blocked_by_robots, pages_fetched, robots: {fetched, disallow_rules}, pages: [{url, homepage, fetched, status, bytes, signals, mixed_content}], external_script_hosts: [{host, known_good, pages}], findings, findings_count}` — the limited depth-1 crawl of internal pages: same host as the final URL only, robots.txt Disallow rules honoured, cross-host redirects recorded but never followed, hard 11-second total budget, 256 KB per page. Per-page `signals` can include `mixed_content`, `hidden_iframe`, `obfuscated_script`, `spam_links` and `uncommon_external_script`.
- Crawl findings (PRO `findings`, each with `"source": "crawl"` and an `evidence` list of `{page, snippet}`): hidden third-party iframes (medium), heavily obfuscated inline scripts (medium), injected spam-keyword links to external sites (medium when hidden, otherwise low), mixed content on crawled subpages (low), and scripts loaded from uncommon third-party domains (info). They are appended after scoring: they never change the score, the `summary` counts, or any BASIC response.
- `methodology` link (`methodology_url`): https://scan.hhelll.my.id/methodology — the full public page of the scoring rubric.

### `GET|POST /headers?url=https://example.com`

Only the header-related checks: HSTS, CSP, X-Content-Type-Options and related cookies, with the header values as received. From **v2.3.0** the response also includes the `header_quality` content analysis (PRO) — the same grading of header values: weak CSP values, short HSTS `max-age` and `Permissions-Policy: *` become findings with concrete `recommendation` and `fix` fields. From **v2.5.0** the response gains a `next_gen` block: the next-generation headers (COOP, COEP, CORP) as a non-scored watchlist. See the [watchlist](#watchlist-not-scored) — the next-gen block is shown alongside the header results.

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan |

### `GET|POST /ssl?url=https://example.com`

Only TLS checks: certificate expiry date, protocol support, certificate chain details, and redirect behavior.

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to scan |

### `GET /cve/search?product=wordpress&version=6.8`

Searches NVD and OSV for CVEs affecting a given product and version, and enriches hits with EPSS scores and CISA KEV status. Free on both plans; use it to check a specific technology version without a full scan.

| Parameter | Required | Notes |
|---|---|---|
| `product` | yes | Product name, e.g. `wordpress`, `jquery` |
| `version` | no | Version to match, e.g. `6.8` |

### `GET /cve/{cve_id}`

Detail for one CVE id, e.g. `/cve/CVE-2024-1234`, with the severity summary (CVSS), description and reference links. Free on both plans; returns 404 when the CVE id is unknown.

### `POST /scan/verify` (PRO)

Starts a domain verification flow: the API issues a token to place at `/.well-known/hhelll-verify.txt` on the domain or in a DNS `TXT` record (`_hhelll-verify.<domain>`). A domain can be verified under either method. The response contains the token and the exact placement instructions.

### `POST /scan/verify/confirm` (PRO)

Confirms a domain verification: the API checks the token's presence at the well-known URL or in the DNS `TXT` record (whichever method was used when issuing the token). `verify` and `confirm` may be used for unrelated domains (a confirmed domain is recorded with the verification); verification is a prerequisite for DAST deep scans (see [Deep scans](#deep-scans-pro)).

### `POST /scan/deep?url=https://example.com` (PRO)

Runs the deep scan: a testssl.sh TLS sweep and an active Nuclei DAST probe. New in this release: deep scans are the only way to get a `tls_deep` result block — a dedicated TLS sweep (protocol and cipher support, certificate details, and TLS vulnerabilities such as BEAST, BREACH, SWEET32, LUCKY13, Heartbleed, ROBOT and POODLE), and active DAST, which crawls the target (Katana) and runs Nuclei DAST templates with out-of-band (Interactsh) detection — reflected XSS, SQL injection, SSRF and more — returned in a `dast` result block. DAST runs only on domains whose ownership the API caller has verified (see `POST /scan/verify` above); unverified domains receive a `dast.skipped` note instead of a result.

| Parameter | Required | Notes |
|---|---|---|
| `url` | yes | The website to deep-scan |
| `auth_cookie` | no | Cookie header to send to the target during the deep scan |
| `auth_headers` | no | Extra headers (as a JSON object of key/value pairs) to send during the deep scan — forwarded only to the DAST crawl on the target's own host and purged from storage at the job's completion |

Deep scan inputs are validated the same way as `/scan` (same SSRF protection).

### `POST /scan/deep/batch` (PRO)

Queues several deep-scan jobs at once (up to 10). Returns each job's ID and status; each job is then processed independently. Requests are handled in background; retrieve a job's result with the deep-scan retrieval endpoint (`GET /scan/deep/{job_id}`) — use the deep-scan endpoint `GET /scan/deep/{job_id}` to fetch the job's results after it completes.

### `GET /scan/history?host=example.com`

The caller's previous scans of a host — at most 20 entries, keyed to the caller and sorted newest-first. `host` may contain a full URL.

### `GET /scan/monitor` (PRO)

Lists the caller's monitors, with each monitor's `monitor_id`, `host`, `interval_hours` and `created_at`. Each monitor also has a `latest_score` and `last_run` timestamps.

### `GET /scan/monitor/{monitor_id}` (PRO)

Reads one monitor with its score history (each entry: `{score, grade, checked_at, changes}` — the same diff shape as `changes` in a scan response) and a **change diff** for the most recent scan (score delta, new and resolved findings, certificate days remaining).

### `POST /scan/monitor` (PRO)

Registers a domain for recurring passive scans: `host`, `interval_hours` (1–168), optional `webhook_url`. The response includes the monitor id and the host. Values: `interval_hours` from 1 to 168 inclusive.

### `DELETE /scan/monitor/{monitor_id}` (PRO)

Cancels monitoring of that domain.

### `POST /scan/monitor/{monitor_id}/webhook` (PRO)

Sets or updates a monitor's `webhook_url`; webhooks POST a JSON alert on score drops of ≥5, new critical/high findings or certificate expiry within 14 days.

### `GET /badge/{host}.svg`

An embeddable SVG badge for the host's latest score and grade, e.g. `<img src="https://scan.hhelll.my.id/badge/example.com.svg">`; also supports `GET /badge?host=example.com`. Free — no authentication — and public: a badge can be displayed for any host scanned. Response content type is `image/svg+xml`.

### `GET /report/{host}`

A public report page on the scanner site for a given host: score, grade, findings and history (summary-level data only).

### `GET /health`

Simple uptime check. Returns `{"status": "ok"}` — everything responding.

### Response shapes

**Summary of response fields**

| Field | Description |
|---|---|
| **`summary`** | Counts by severity (`critical`, `high`, `medium`, `low`, `info`) |
| **`findings`** | The issues found; each finding has a `severity`, a `title`, a `recommendation`, and a `fix` when available |
| **`score`** | The total score, `0–100`, weighted by severity |
| **`grade`** | Letter grade: `A` to `F` in 5 steps (A, B, C, D, F) |
| **`advanced`** | BASIC compact equivalents of the PRO checks (see v2.2.0 response fields above) |
| **`methodology_url`** | https://scan.hhelll.my.id/methodology — the full public page of the scoring rubric |

## Scoring methodology

The score is the sum of the deductions for these categories:

| Category | Deductions |
|---|---|
| Transport security (HTTPS) | 10 total: no HTTPS redirect (−10), deprecated protocol TLS 1.0/1.1 (−5) |
| Headers | 5 each missing: CSP, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`; HSTS missing (−15) or `max-age` shorter (−5) |
| Cookies | 5 each missing `Secure` or `HttpOnly`; 10 if `SameSite` is missing (PRO also checks `Partitioned`) |
| Info disclosure | 10 exposed server version; 10 exposed PHP version; 20 exposed `.env` file |
| Exposed files | 20 exposed `.env`; 10 exposed `.git/HEAD`; 8 exposed `phpinfo.php`, `.svn/entries`, `.htaccess` or `adminer.php` |
| Mixed content | 10 active mixed content; 5 passive mixed content |
| DNS / mail | 5 missing SPF; 5 missing DMARC; 5 missing CAA; plus (PRO) `security.txt` missing (−5) on the report (the DNS/mail items that do *not* carry deductions are: `advanced.mta_sts_present`, `advanced.tls_rpt_present`, `advanced.dnssec_signed` — see the [watchlist](#watchlist-not-scored) below |
| CVE intelligence | 10 per critical CVE; 5 per high CVE; 3 per medium CVE |
| **Total** | **100** |

Grades: `A` ≥90, `B` ≥75, `C` ≥60, `D` ≥40, `F` <40.

The complete rubric is published at https://scan.hhelll.my.id/methodology.

### Watchlist — not scored

These items are reported but never change the score; they appear as info findings and in the PRO checks, marked `"scored": false` and in the BASIC `advanced` block. The repository's own summary lists the watchlist separately so a reader can tell at a glance what is visible but not scored:

| Item | Where it appears |
|---|---|
| **MTA-STS** (`_mta-sts.<domain>`): whether the domain publishes an MTA-STS policy (`_mta-sts.<domain>`) — the record is checked by querying DNS, not just via headers. A warning is shown when the domain's mail server is not covered. | `checks.dns_email.mta_sts_present` (PRO); BASIC `advanced.mta_sts_present` |
| **TLS-RPT** (`_smtp._tls.<domain>`): whether the domain publishes a TLS-RPT record | `checks.dns_email.tls_rpt_present` and `tls_rpt_record` (PRO); BASIC `advanced.tls_rpt_present` |
| **DNSSEC** status: `ds_present`, `dnskey_present`, `signed` — whether the domain's DNS is signed | `checks.dns_email.dnssec` (PRO); BASIC `advanced.dnssec_signed` |
| **COOP** (Cross-Origin-Opener-Policy) | `checks.next_gen_headers.coop` (PRO); `next_gen` on `/headers` |
| **COEP** (Cross-Origin-Embedder-Policy) | `checks.next_gen_headers.coep` (PRO); `next_gen` on `/headers` |
| **CORP** (Cross-Origin-Resource-Policy) | `checks.next_gen_headers.corp` (PRO); `next_gen` on `/headers` |
| **Page crawl signals** (hidden iframes, obfuscated scripts, spam-keyword links, uncommon third-party script hosts, subpage mixed content) | `checks.crawl` (PRO); findings carry `"source": "crawl"` and evidence snippets |

- The MTA-STS check is extra-careful: it also validates that the domain is not behind a shared mail domain such as gmail.com or outlook.com — a Google Apps domain is not marked as an MTA-STS failure (an MTA-STS policy on a shared mail domain is not expected).
- The TLS-RPT check reports the full record when a domain publishes one: the `rua` destination, `ruf` destination, and policy-level aggregation. The check is exposed as fields `tls_rpt_present` and `tls_rpt_record`; a domain without one still shows the info finding.

## Plans

| | BASIC (free) | PRO ($5/month) |
|---|---|---|
| `/scan`, `/headers`, `/ssl`, `/cve/search`, `/cve/{cve_id}`, `/health` | ✓ | ✓ |
| Deep TLS sub-scores (`tls_deep` on `/scan` and `/ssl`) | — | ✓ |
| Header quality analysis (`checks.header_quality`), fix snippets on findings | — | ✓ |
| Badge endpoint, public report pages | ✓ | ✓ |
| Monitoring webhooks | — | ✓ |
| Deep scans (active testssl.sh + DAST for verified domains) | — | ✓ |
| Monitoring mode with change diffs | — | ✓ |
| Watchlist fields (DNS/mail and next-gen headers) | ✓ (compact `advanced` block) | ✓ (full `checks` blocks) |
| Limited multi-page crawl (`checks.crawl` + crawl findings) | — (BASIC responses unchanged) | ✓ |

Prices and quotas live on the [RapidAPI listing](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api) — that page is the source of truth.

## Rationale for field names (READ THIS)

Field names in this documentation are the ones the API actually returns. In particular, `dns_email` is the field name used in the response even though it says "DNS/email" in the description. Likewise `next_gen_headers` is the literal name used in the response, whereas the header names themselves are `Cross-Origin-Opener-Policy` and `Cross-Origin-Embedder-Policy`; `checks.next_gen_headers` describes them as COOP/COEP/CORP, not as the literal header names. `advanced` is the BASIC compact block; e.g. `advanced.mta_sts_present` is a watchlist entry that does not affect the score. Note the thematic function of watchlist entries — they exist to be *visible* without affecting the score. (`dns_email` description wording is a red herring — in context it means DNS **or** email.)

All response fields on this page are real and returned by the live API. See the [full list of checks](#response-shapes) (**required** to be kept up to date with every release). *Any* change to a response field name in the API requires a documentation change here too (see [Version history](#website-security-scanner-api)). Keep the response fields list in sync with every release — every field name mentioned here has to be one the API actually returns (and of the same type). This is the contract the doc is keeping: field names are contractual in a way that the prose is not, so field names require more care — the prose can say "watchlist" and mean several things, but a field name in the doc has to match the response exactly. Deductions are listed in the Scoring methodology table above; watchlist entries live in the [Watchlist](#watchlist-not-scored) table and are explicitly excluded from deductions. Note this paragraph is for documentation maintainers: the score bands in the scoring methodology table are **fixed** — no changes accepted. Also note that score bands are **fixed** in the rubric: grade bands are part of the public rubric and must not change. (**DO NOT change the grade bands; do not change any values.**)

When checking a returned value against this page, treat the field names as *contractual*. Check that the value type matches: a boolean for `advanced.mta_sts_present`, a string for `checks.dns_email.tls_rpt_record`, the `dnssec` field as an object `{ds_present: bool, dnskey_present: bool, signed: bool}`, and the `checks.malware_reputation` value as an object. The exact field names are contractual — even a typo is a breaking change (the scoring is 0–100 with a computed grade). This consistency is maintained by `docs/website-security-scanner.md` and is the **reason** this doc exists.

## Deep scans (PRO)

Where deep scans are needed: active DAST runs only on domains whose ownership the API caller has verified — `/scan/deep` probes the target with testssl.sh for the `tls_deep` block and crawls it (Katana) to run the Nuclei DAST templates with out-of-band (Interactsh) detection. DAST findings are verified with the finding verification layer (replayed against the target and compared against benign controls): findings are assigned a `confidence` — `confirmed`, `likely`, `reported`, `unverified`. See the [endpoints](#endpoints) section for the related endpoints and parameters: `POST /scan/deep`, `POST /scan/deep/batch`, and `GET /scan/deep/{job_id}` — and the verification endpoints `POST /scan/verify` and `POST /scan/verify/confirm`.

## Version history

- **2.6.0 — 2026-11-07:** limited multi-page crawl (`checks.crawl`, PRO detail, non-scored): mixed content and injection signals on up to 10 internal pages.
- **2.5.0 — 2026-11-07:** DNS/mail watchlist (non-scored), next-generation header watchlist (non-scored), scoring methodology page.
- **2.4.0 — 2026-11-07:** deep TLS sub-scores (`tls_deep`) for PRO; compressed-response fix.
- **2.3.0 — 2026-11-07:** header content-quality analysis, fix snippets, badge endpoint, public report pages, monitoring webhooks.
- **2.2.0 — 2026-11-05:** advanced passive checks for all plans; scan history and change diffs.
- **2.1.0 — 2026-11-02:** CVE lookup endpoints; live CVE intelligence (NVD/OSV + EPSS + CISA KEV).
- **2.0.0 — 2026-11-01:** full versioning and changelog.
- **1.0.0 — 2026-10-24:** Website Security Scanner API release.

Use the version history with `CHANGELOG.md`: the version the API returns is what `CHANGELOG.md` says it should be.

## Links

- Version history: [`CHANGELOG.md`](../CHANGELOG.md)
- Live scanner: [scan.hhelll.my.id](https://scan.hhelll.my.id/)
- RapidAPI: [Website Security Scanner API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)
- Website Security Scanner API: [README](../README.md)
- Changelog: [CHANGELOG](../CHANGELOG.md)

Built and maintained by [hhelll](https://github.com/hhellll). For questions, see the [repository README](../README.md).
