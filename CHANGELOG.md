# Changelog

All notable changes to the **Website Security Scanner API** — the flagship
API documented in this repository. The format follows Keep a Changelog;
versions match the `version` the API reports about itself.

## [Unreleased]

### Added
- **Deep TLS analysis in every deep scan** (testssl.sh): protocol and
  cipher enumeration, TLS vulnerability checks (BEAST, BREACH, SWEET32,
  LUCKY13, Heartbleed, ROBOT, POODLE, and more) and certificate-chain
  details, returned in a `tls_deep` result block. TLS vulnerabilities
  are also folded into the job's findings.
- **Active DAST checks for verified domains**: deep scans now crawl the
  target (Katana) and run Nuclei DAST templates with out-of-band
  (Interactsh) detection — reflected XSS, SQL injection, SSRF and more —
  returned in a `dast` result block. DAST runs only on domains whose
  ownership the API caller has verified; unverified domains receive a
  `dast.skipped` note instead.
- **Domain ownership verification** (PRO): `POST /scan/verify` issues a
  token to place at `/.well-known/hhelll-verify.txt` or in a DNS TXT
  record; `POST /scan/verify/confirm` checks it and unlocks DAST for
  that domain.
- **Finding verification layer**: DAST findings are replayed and
  compared against benign control requests where a strategy exists
  (reflected XSS, error-based SQL injection, out-of-band hits) and now
  carry a `confidence` label — `confirmed`, `likely`, `reported` or
  `unverified` — with the evidence basis in `verification`.
- **Authenticated DAST**: deep scans accept `auth_cookie` /
  `auth_headers`, forwarded only to the DAST crawl and checks on the
  job's own host and wiped from storage when the job finishes.
- **Monitoring mode** (PRO): `POST /scan/monitor` registers a domain
  for recurring passive scans (configurable interval, 1-168 hours);
  every run stores the score/grade and a change diff (score delta, new
  and resolved findings, certificate days remaining), readable via
  `GET /scan/monitor` and `GET /scan/monitor/{id}`; `DELETE` stops it.
- **Malware reputation check (lite)** in every passive scan:
  `checks.malware_reputation` consults the Spamhaus DBL and SURBL
  domain blocklists plus URL heuristics (IP-literal hosts, punycode,
  shorteners, executable paths). A blocklist hit adds a high finding.
  Deliberately a reputation check, not a full malware scan.

### Changed
- **Repository focus**: this repository now documents the Website Security
  Scanner API only. Documentation and examples for the other dev-utility
  APIs were removed from the repo; those APIs themselves are unaffected.

### Fixed
- `security.txt` detection is stricter: a target now counts as publishing
  one only when the file is served as a non-HTML response containing a
  `Contact:` field line (RFC 9116). WAF checkpoint and SPA fallback pages
  returned with HTTP 200 can no longer produce a false "present" result.

## [2.4.0] — 2026-11-07

### Added
- **Deep TLS sub-scores for PRO** — a `tls_deep` block on `GET|POST /scan`
  and `GET /ssl` with SSL Labs-style sub-scores (protocol, key exchange
  and cipher strength, 0–100 each, weighted 30/30/40 into an overall
  TLS score), certificate-chain trust/completeness, OCSP stapling and
  forward-secrecy assessment, computed from testssl.sh enumeration
  data. The analysis runs in the background per host (deep scans fill
  the cache from the testssl run they already perform) and is cached
  for 7 days; while a host's first analysis is outstanding the block
  reports `"status": "pending"` instead of blocking the response.
  BASIC responses are unchanged.

### Fixed
- Deep TLS chain/OCSP parsing now handles multi-certificate hosts
  (RSA + ECDSA), whose testssl results suffix their finding ids per
  certificate.

## [2.3.0] — 2026-11-06

### Added
- **Embeddable SVG score badge**: `GET /badge/{host}.svg` (or
  `?host=`) — grade + score pill for READMEs and site footers,
  reflecting the freshest stored full scan.
- **Public report pages**: `GET /report/{host}` on scan.hhelll.my.id —
  latest summary, per-category pass/fail, findings and a score-history
  chart from all stored scans of the host.
- **Header content-quality analysis**: CSP / HSTS / Referrer-Policy /
  Permissions-Policy values are parsed and graded, not just checked
  for presence (`checks.header_quality` in PRO scans; per-header
  `quality` on PRO `/headers`), with findings for weak values.
- **Fix snippets**: PRO findings carry copy-paste remediation config
  (nginx, Apache, Cloudflare, WordPress/PHP headers, DNS records).
- **Monitor webhooks**: PRO monitors accept `webhook_url` and POST a
  JSON alert on score drops ≥5, new critical/high findings or
  certificates expiring within 14 days (manageable via
  `POST /scan/monitor/{id}/webhook`).

### Fixed
- Registrable-domain extraction now follows the real Public Suffix
  List — multi-part suffixes were mis-resolved before (e.g. a domain
  under `.my.id` inherited the suffix zone's SPF/DMARC records).
- Standard scans are much faster: the Certificate Transparency lookup
  now runs in parallel from the start of the scan with a bounded
  budget and short-lived negative caching (~16 s → ~4 s typical).

## [2.2.0] — 2026-10-27

### Added
- Advanced passive checks on **all plans**: CAA records, DKIM detection,
  HSTS preload status, and `security.txt` presence.
- Certificate Transparency subdomain enumeration (subdomain surface) in
  every scan.
- Scan history per caller with scan-to-scan change diffs (`changes` on
  `/scan`, `GET /scan/history`).
- PRO batch deep scans: `POST /scan/deep/batch` with partial acceptance
  when the deep-scan credit pool runs short.

### Changed
- Pricing simplified to two tiers — BASIC (free, 2 scans/month) and PRO
  ($5/month, 1,000 scans + $0.01 overage). ULTRA/MEGA tiers removed.
- Full CVE records on all plans (previously gated).

## [2.1.0] — 2026-10-27

### Added
- Live CVE intelligence: software detected on a scanned site is matched
  against CVE records enriched with EPSS exploit-probability scores and
  CISA KEV active-exploitation status, with a composite risk score.
- `GET /cve/search` and `GET /cve/{cve_id}` endpoints.
- Daily CVE data sync (CISA KEV + EPSS + OSV/NVD).

## [2.0.0] — 2026-10-24

### Added
- Deep scans for PRO: Nuclei-powered active template scanning
  (`POST /scan/deep`, `GET /scan/deep/{job_id}`), drawn from a monthly
  deep-scan credit pool (25 credits, max 5/day).

## [1.0.0] — 2026-10-23

### Added
- Initial release: fully passive website security audit — HTTPS
  enforcement and TLS health, security headers, cookie flags, server
  information disclosure, exposed files (`.env`, `.git`), and mixed
  content — rolled into a 0–100 score and a letter grade.
- Helper endpoints `GET /headers` and `GET /ssl`.
- Listed on RapidAPI as catalog #1 of the dev-utility APIs family.
