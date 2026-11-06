#!/usr/bin/env bash
# Website Security Scanner API — cURL examples.
# Get your key by subscribing (free plan available) at:
#   https://rapidapi.com/Hitler-HlDevZDwP/api/website-security-scanner-api
set -euo pipefail

: "${RAPIDAPI_KEY:?Set RAPIDAPI_KEY first}"
HOST="website-security-scanner-api.p.rapidapi.com"
TARGET="https://example.com"

# 1) Full security scan — score, grade, severity summary and findings
curl "https://${HOST}/scan?url=${TARGET}" \
  -H "X-RapidAPI-Key: ${RAPIDAPI_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}"

# 2) Headers only — the six security headers, cookie flags, version disclosure
curl "https://${HOST}/headers?url=${TARGET}" \
  -H "X-RapidAPI-Key: ${RAPIDAPI_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}"

# 3) TLS only — certificate details, protocol and cipher, legacy TLS support
curl "https://${HOST}/ssl?url=${TARGET}" \
  -H "X-RapidAPI-Key: ${RAPIDAPI_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}"

echo "Done"
