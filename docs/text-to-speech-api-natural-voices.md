# Text to Speech API - Natural Voices

Convert text into natural-sounding **WAV audio** with fast, CPU-friendly neural voices. English (US and GB) and Indonesian voices are included, with adjustable speaking speed — and no per-minute pricing surprises: every call handles up to 2,000 characters.

**Live on RapidAPI → [Text to Speech API - Natural Voices](https://rapidapi.com/Hitler-HlDevZDwP/api/text-to-speech-api-natural-voices)**

**Gateway host:** `text-to-speech-api-natural-voices.p.rapidapi.com`

Every call goes to `https://text-to-speech-api-natural-voices.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `text-to-speech-api-natural-voices.p.rapidapi.com` |

## Endpoints

### `GET /voices`

List the available voices.

**Response:** JSON array of `{ id, language, name }`. Current voices:

| Voice id | Language |
|---|---|
| `en_US-lessac-medium` | English (US) |
| `en_GB-alan-medium` | English (GB) |
| `id_ID-news_tts-medium` | Indonesian |

### `POST /tts`

Synthesize speech from text.

JSON body:

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to speak (max 2,000 characters) |
| `voice` | string | no | Voice id from `GET /voices` (default: `en_US-lessac-medium`) |
| `speed` | number | no | Speaking speed multiplier (default 1.0) |

**Response:** `200 OK` with `Content-Type: audio/wav` — the synthesized audio bytes.

## Example (cURL)

```bash
curl -X POST "https://text-to-speech-api-natural-voices.p.rapidapi.com/tts" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: text-to-speech-api-natural-voices.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello! This is a test of the text to speech API.", "voice": "en_US-lessac-medium"}' \
  --output speech.wav
```

A runnable Python example is in [`examples/tts_example.py`](../examples/tts_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $10 / month | 500 / month |
| ULTRA | $29 / month | 2,000 / month |
| MEGA | $75 / month | 10,000 / month |

Subscribe and manage your plan here: **[Text to Speech API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/text-to-speech-api-natural-voices)**

Part of the [hhelll API family](../README.md#more-apis-by-hhelll).
