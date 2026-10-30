# Changelog

All notable changes to the **Website Security Scanner API** — catalog #1 of
dev-utility APIs. The format follows Keep a Changelog; versions match the
`version` the API reports about itself.

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

### Fixed
- `security.txt` detection is stricter: a target now counts as publishing
  one only when the file is served as a non-HTML response containing a
  `Contact:` field line (RFC 9116). WAF checkpoint and SPA fallback pages
  returned with HTTP 200 can no longer produce a false "present" result.

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
