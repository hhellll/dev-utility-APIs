# Changelog

All notable changes to the **Website Security Scanner API** — the API documented in this repository. The format follows Keep a Changelog; versions match the `version` the API reports about itself.

## [Unreleased]

### Added

- **Deep TLS analysis in every deep scan** (testssl.sh): protocol and cipher enumeration, TLS vulnerability checks (BEAST, BREACH, SWEET32, LUCKY13, Heartbleed, ROBOT, POODLE, and more) and certificate-chain details, returned in a `tls_deep` result block. TLS vulnerabilities are also folded into the job's findings.
- **Active DAST checks for verified domains**: deep scans now crawl the target (Katana) and run Nuclei DAST templates with out-of-band (Interactsh) detection — reflected XSS, SQL injection, SSRF and more — returned in a `dast` result block. DAST runs only on domains whose ownership the API caller has verified; unverified domains receive a `dast.skipped` note instead.
- **Domain ownership verification** (PRO): `POST /scan/verify` issues a token to place at `/.well-known/hhelll-verify.txt` or in a DNS TXT record; `POST /scan/verify/confirm` checks it and unlocks DAST for that domain.
- **Finding verification layer**: DAST findings are replayed and compared against benign control requests where a strategy exists (reflected XSS, error-based SQL injection, out-of-band hits) and now carry a `confidence` label — `confirmed`, `likely`, `reported` or `unverified` — with the evidence basis in `verification`.
- **Authenticated DAST**: deep scans accept `auth_cookie`/`auth_headers`, forwarded only to the DAST crawl and checks on the job's own host and wiped from storage when the job finishes.
- **Monitoring mode** (PRO): `POST /scan/monitor` registers a domain for recurring passive scans (configurable interval, 1-168 hours); every run stores the score/grade and a change diff (score delta, new and resolved findings, certificate days remaining), readable via `GET /scan/monitor` and `GET /scan/monitor/{id}`; `DELETE` stops it.
- **Malware reputation check (lite)** in every passive scan: `checks.malware_reputation` consults the Spamhaus DBL and SURBL domain blocklists plus URL heuristics (IP-literal hosts, punycode, shorteners, executable paths). A blocklist hit adds a high finding. Deliberately a reputation check, not a full malware scan.

### Changed

- **Repository focus**: this repository now documents the Website Security Scanner API only. Documentation and examples for the other dev-utility APIs were removed from the repo; those APIs themselves are unaffected.

### Fixed

- `security.txt` detection is stricter: a target now counts as publishing one only when the file is served as a non-HTML response containing a `Contact:` field line (RFC 9116). WAF checkpoint and SPA fallback pages returned with HTTP 200 can no longer produce a false "present" result.

## [2.7.0] — 2026-11-07

### Added

- **WordPress component & JavaScript library watchlist (PRO detail, non-scored)**: every scan now detects the WordPress plugins and themes a site actually loads — from asset URLs on the homepage and on the pages fetched by the multi-page crawl — and resolves their installed versions from asset `?ver=` parameters and, with the highest confidence, from each plugin's own `readme.txt` (`Stable tag:`) and each theme's `style.css` (`Version:`). Detected versions are matched against a local mirror of the **Wordfence Intelligence** vulnerability feed (daily sync, PHP-style version-range comparison); Wordfence records are reproduced with their record links and Defiant/MITRE attribution, as the feed licence requires. Popular JavaScript libraries (Lodash, Moment, jQuery UI, Select2, Swiper, Slick, Owl Carousel, DataTables, Fancybox) are detected the same way and matched against NVD/OSV. Results live in `checks.wp_components` with per-component version source and confidence, an open statement of the mirror's freshness (`data.fetched_at`, `data_age_days`), and `"scored": false`; matched vulnerabilities also appear as info findings with `"source": "wp_components"`, appended after scoring. While the Wordfence mirror is not populated yet, the block reports `"status": "no_data"` instead of guessing. Watchlist results never change the score — BASIC responses are byte-for-byte identical to v2.6.0.

## [2.6.0] — 2026-11-07

### Added

- **Limited multi-page crawl (PRO detail, non-scored)**: every scan now also crawls up to 10 internal pages of the target — depth 1, same host only, robots.txt honoured, cross-host redirects recorded but never followed, under a hard 11-second budget with a per-page size cap. Each crawled page is checked for mixed content and for conservative, evidence-based injection signals: hidden iframes loading third-party content, heavily obfuscated inline scripts (eval/unescape-style execution combined with a long encoded payload), spam-keyword links pointing to external sites, and scripts loaded from uncommon third-party domains. Results live in `checks.crawl` with per-page status and the exact snippets that triggered each signal; aggregated crawl findings are appended to PRO reports with `"source": "crawl"`. Crawl results never change the score — BASIC responses are byte-for-byte identical to v2.5.0.

## [2.5.0] — 2026-11-07

### Added

- **DNS/mail watchlist (non-scored)**: DNSSEC status (`ds_present`, `dnskey_present`, `signed`), MTA-STS presence (`_mta-sts.<domain>`) and TLS-RPT presence/record (`_smtp._tls.<domain>`) — each item produces an info finding so it is visible in the report, and none of them ever changes the score. Full entries live in `checks.dns_email` (PRO); BASIC summaries expose `advanced.mta_sts_present`, `advanced.tls_rpt_present` and `advanced.dnssec_signed`.
- **Next-generation header watchlist (non-scored)**: `checks.next_gen_headers` (PRO; `next_gen` on `/headers`) reports `Cross-Origin-Opener-Policy`, `Cross-Origin-Embedder-Policy` and `Cross-Origin-Resource-Policy`, marked `"scored": false`.
- **Scoring methodology page on the scanner site**: the complete rubric — every deduction, the grade bands and the watchlist — is published at https://scan.hhelll.my.id/methodology.

## [2.4.0] — 2026-11-07

### Added

- **Deep TLS sub-scores for PRO** — a `tls_deep` block on `GET|POST /scan` and `GET /ssl` with SSL Labs-style sub-scores (protocol, key exchange, cipher strength) plus chain, OCSP and forward-secrecy detail, computed in the background per host from testssl.sh data and cached for 7 days.

### Fixed

- Compressed responses: `Accept-Encoding` gzip/deflate is sent on every probe, and response bodies are decompressed before detection (versions and security.txt), so servers that compress no longer look empty.

## [2.3.0] — 2026-11-07

### Added

- **Header content-quality analysis for PRO**: `checks.header_quality` grades not just the presence of CSP, HSTS, Referrer-Policy and Permissions-Policy, but the content of their values (CSP directives, HSTS `max-age`/`includeSubDomains`, policy values) — weak values now raise findings.
- **Fix snippets on scan findings**: PRO scan findings carry a `fix` field — ready-to-use configuration for nginx, Apache, Cloudflare, WordPress/PHP, and DNS records, matched to each finding.
- **Badge endpoint**: `GET /badge/{host}.svg` — an embeddable SVG score badge for a host (also `GET /badge?host=example.com`).
- **Public report pages**: `GET /report/{host}` — a public page on the scanner site with the host's score, grade, pass/fail per category and findings, plus a score-history chart (summary-level data only).
- **Monitoring webhooks**: monitors can carry a `webhook_url` that receives a JSON alert on score drops of 5+, new critical/high findings, or certificate expiry within 14 days (set it on `POST /scan/monitor`, update with `POST /scan/monitor/{id}/webhook`).

### Changed

- Deep scan results now mirror the deep TLS block (`tls_deep`) already computed in the deep scan itself.

## [2.2.0] — 2026-11-05

### Added

- **Advanced passive checks for all plans**: DNS/email security (SPF, DMARC, DKIM, CAA, MTA-STS, TLS-RPT, DNSSEC), security.txt, HSTS preload status, TLS cipher detail, and a Certificate Transparency subdomain surface. PRO reports carry them under `checks`; the BASIC summary carries compact equivalents (`categories.dns_email`, `categories.security_txt`, an `advanced` block, and a compact `subdomains` block). These checks were previously only available on retired plans.
- **Scan history and change diffs**: every `/scan` response includes a `changes` object (first scan?, score delta, new and resolved findings, certificate expiry days), computed against the same caller's previous scan of the same host. History is readable via `GET /scan/history?host=example.com` (at most 20 entries, keyed to the caller).

### Changed

- Removed the old **Website Link Extraction API** — it is still live on the site; only its URL remains in the README.
- Retired plans (starter, growth, enterprise, custom) are gone; BASIC and PRO remain.

## [2.1.0] — 2026-11-02

### Added

- **Live CVE intelligence**: detected technologies and versions are matched against NVD and OSV records, enriched with EPSS exploit-probability scores and CISA KEV active-exploitation status.
- **CVE lookup endpoints**: `GET /cve/search?product=...&version=...`, `GET /cve/{cve_id}`.

### Fixed

- Also corrected the `v2.0.0` header ordering after a bad export.

## [2.0.0] — 2026-11-01

### Added

- Full versioning and changelog.

## [1.0.0] — 2026-10-24

### Added

- **Website Security Scanner API** with these endpoints: `GET /scan`, `GET /headers`, `GET /ssl`.
- **RapidAPI listing** and usage dashboard.
