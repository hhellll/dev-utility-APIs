#!/usr/bin/env bash
# Background Remover AI — cURL examples.
# Get your key by subscribing (free plan available) at:
#   https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5
set -euo pipefail

: "${RAPIDAPI_KEY:?Set RAPIDAPI_KEY first}"
HOST="background-remover-ai5.p.rapidapi.com"

# 1) Upload a local file
curl -X POST "https://${HOST}/remove-background" \
  -H "X-RapidAPI-Key: ${RAPIDAPI_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" \
  -F "image=@photo.jpg" \
  --output result-from-file.png

# 2) Send an image URL instead
curl -X POST "https://${HOST}/remove-background" \
  -H "X-RapidAPI-Key: ${RAPIDAPI_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" \
  -F "image_url=https://example.com/photo.jpg" \
  --output result-from-url.png

echo "Done: result-from-file.png, result-from-url.png"
