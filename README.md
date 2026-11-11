![Website Security Scanner API](assets/banner-dark.png)


# Website Security Scanner API


![Live on RapidAPI](https://img.shields.io/badge/RapidAPI-live-0055ff)![BASIC](https://img.shields.io/badge/BASIC-free-brightgreen) ![PRO](https://img.shields.io/badge/PRO-%245%2Fmonth-blue) ![License](https://img.shields.io/badge/license-MIT-green)
[![Verified on FreeAPI](https://findfreeapi.com/api/badge/dev-utility-apis)](https://findfreeapi.com/en/service/dev-utility-apis)

Scan any public website's security posture in seconds — completely passively, with nothing installed on the target: HTTPS enforcement and TLS health, security headers, cookie flags, server information disclosure, exposed files such as `.env` and `.git`, mixed content, DNS and email authentication checks, Certificate Transparency subdomain surface, scan-to-scan change diffs, and outdated software matched against live CVE intelligence (EPSS exploit probability and CISA KEV active-exploitation data) — all rolled into one 0–100 score and a letter grade.

*This repository previously catalogued the dev-utility APIs family; it now documents a single API — the Website Security Scanner API.*

**Live on RapidAPI → [Website Security Scanner API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)**

**Try it free, no signup → [scan.hhelll.my.id](https://scan.hhelll.my.id/)** — the official live scanner: score, grade, per-category pass/fail and findings, the same shape the free BASIC plan returns.

![Website Security Scanner API](assets/website-security-scanner.jpg)

### What it does

Give the API a URL and it runs a full passive audit: it follows the redirect chain, inspects the TLS certificate and protocol support, checks six security headers and cookie flags, fingerprints the technology stack and matches detected versions against live CVE data, enriched with EPSS scores and CISA KEV status, probes a list of commonly exposed files, and looks for mixed content. It also crawls up to ten internal pages of the site (same host only, robots.txt honoured) and checks each page for mixed content and conservative, evidence-based injection signals — hidden third-party iframes, heavily obfuscated scripts, injected spam links and uncommon third-party script hosts. It also checks DNS and email authentication (SPF, DMARC, DKIM selectors, and CAA), looks for a published security.txt and HSTS preload status, maps the Certificate Transparency subdomain surface, and records each caller's scans so repeat scans show what changed. Private and internal targets are refused (SSRF-protected) — it only scans public sites, and it never includes the contents of any exposed file, only that the path responded.

| | |
|---|---|
| Input | A `url` — as a query parameter (GET) or JSON body (POST) |
| Output | JSON — `score`, `grade`, summary counts by severity, and `findings` with per-check detail |
| Latency | ~2–10 seconds per scan (a real www.spacex.com scan through the gateway took 3.2 s) |
| Endpoints | `GET\|POST /scan`, `GET /headers`, `GET /ssl`, `GET /cve/search`, `GET /cve/{cve_id}`, `GET /scan/history`, `POST /scan/deep`, `POST /scan/deep/batch`, `GET /health` |

### Quick start

Subscribe on the API's [RapidAPI page](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api) to get a key. A runnable version of these calls lives in [`examples/secscan_example.sh`](examples/secscan_example.sh).

#### cURL

```bash
# Run a full security scan (GET with a query parameter)
curl "https://website-security-scanner-api.p.rapidapi.com/scan?url=https://example.com" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: website-security-scanner-api.p.rapidapi.com"

# The same call as POST with a JSON body
curl -X POST "https://website-security-scanner-api.p.rapidapi.com/scan" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: website-security-scanner-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"https://example.com\"}"
```

**Response:**

```json
{
  "url": "https://www.spacex.com",
  "score": 67,
  "grade": "C",
  "summary": { "critical": 0, "high": 1, "medium": 2, "low": 3, "info": 2 },
  "findings": [
    { "severity": "high", "title": "Sensitive file exposed: /server-status" },
    { "severity": "medium", "title": "Missing security header: Content-Security-Policy" }
  ]
}
```

*(Example from a real scan of www.spacex.com through the RapidAPI gateway; findings are shortened.)*

### Plans

Two plans exist on RapidAPI: **BASIC** (free) and **PRO** ($5/month). **BASIC** includes the full passive scan, header and TLS checks and the live CVE results. **PRO** adds: deep TLS sub-scores and chain detail, header content-quality analysis, fix snippets on findings, the badge endpoint, public report pages, the monitoring webhooks, deep scans (active testssl.sh + DAST, domain verification required), monitoring mode with change diffs, and the complete watchlist (DNS/mail + next-generation headers), plus the multi-page crawl detail (`checks.crawl`) and crawl findings, and the WordPress component watchlist (`checks.wp_components`): detected plugins, themes and JavaScript libraries with resolved versions matched against a local Wordfence Intelligence mirror and NVD/OSV. Watchlist results are reported with evidence, state their data freshness openly, and never change the score. Crawl results are reported with evidence and never change the score, so BASIC responses are unchanged. Quotas and prices live on the [RapidAPI listing](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api) — they are the source of truth.

### Scan flow

1. The API fetches the URL and walks the redirect chain.
2. It inspects the TLS certificate (including expiry) and enabled protocols, and follows the chain.
3. It checks the response headers: CSP, HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy. Missing or weak values lower the score.
4. It fingerprints the stack (server, X-Powered-By, meta generator and similar signals), checks detected versions against NVD/OSV and enriches hits with EPSS probability and CISA KEV status, then probes a curated list of exposed files such as `/.env` and `/.git/HEAD` (recording only that the path responded).
5. It verifies the DNS and email authentication records (SPF, DMARC, DKIM selectors, CAA), looks for a published security.txt and queries the HSTS preload list, then maps subdomains from Certificate Transparency logs.
6. It compares the result against the same caller's previous scan of that host and summarizes what changed.
7. It calculates the 0–100 score and the letter grade, and serializes the findings with per-check detail.

The scoring rubric is published in full: [scan.hhelll.my.id/methodology](https://scan.hhelll.my.id/methodology).

### API details

Full API documentation, including authentication, error shapes, endpoint parameters, and response examples, lives in the [docs](docs/website-security-scanner.md). A runnable cURL example lives in [`examples/secscan_example.sh`](examples/secscan_example.sh).

### FAQ

**What does a scan change on the target?**
Nothing: the scan only performs HTTP requests and DNS lookups, and records that a path responded. It never exploits anything and never includes file contents.

**Can it scan my site?**
Yes, any public website. Private and internal addresses are refused (SSRF-protected), and deep scans require ownership verification.

**Where does the version come from?**
The version lives in `CHANGELOG.md`, following Keep a Changelog — the API reports the same version about itself.

## Versioning

- [2.7.0] — 2026-11-07: WordPress component & JavaScript library watchlist — plugins/themes detected from page assets, versions resolved from `readme.txt`/`style.css`, matched against a local Wordfence Intelligence mirror (NVD/OSV for libraries); PRO detail in `checks.wp_components`, non-scored, BASIC unchanged.
- [2.6.0] — 2026-11-07: limited multi-page crawl — up to 10 internal pages checked for mixed content and injection signals; PRO detail in `checks.crawl`, non-scored, BASIC unchanged.
- [2.5.0] — 2026-11-07: DNS/mail watchlist (non-scored), next-generation header watchlist (non-scored), scoring methodology page.
- [2.4.0] — 2026-11-07: deep TLS sub-scores for PRO; compressed-response fix.
- [2.3.0] — 2026-11-07: header content-quality analysis, fix snippets, badge endpoint, public report pages, monitoring webhooks.
- [2.2.0] — 2026-11-05: advanced passive checks for all plans, scan history & change diffs; removed the Website Link Extraction API from the repo; retired plans removed.
- [2.1.0] — 2026-11-02: live CVE intelligence and CVE lookup endpoints.
- [2.0.0] — 2026-11-01: full versioning and changelog.
- [1.0.0] — 2026-10-24: Website Security Scanner API with `GET /scan`, `GET /headers`, `GET /ssl`.

## Links

- Docs: [`docs/website-security-scanner.md`](docs/website-security-scanner.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Website: [scan.hhelll.my.id](https://scan.hhelll.my.id/)
- RapidAPI: [Website Security Scanner API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api)
- License: [MIT](LICENSE)

Built and maintained by [hhelll](https://github.com/hhellll).
