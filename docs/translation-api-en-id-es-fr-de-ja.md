# Translation API - EN ID ES FR DE JA

Offline neural machine translation for six languages — **English, Indonesian, Spanish, French, German, and Japanese** — plus language detection. Models run on our own servers (Argos Translate / OpenNMT), so there is no per-character upstream bill and no text leaves for a third-party cloud translator.

**Live on RapidAPI → [Translation API - EN ID ES FR DE JA](https://rapidapi.com/Hitler-HlDevZDwP/api/translation-api-en-id-es-fr-de-ja)**

**Gateway host:** `translation-api-en-id-es-fr-de-ja.p.rapidapi.com`

Every call goes to `https://translation-api-en-id-es-fr-de-ja.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `translation-api-en-id-es-fr-de-ja.p.rapidapi.com` |

## Endpoints

### `POST /translate`

Translate text. Direct pairs are installed for every language ↔ English (e.g. `en→id`, `id→en`, `en→es`, `es→en`, `en→fr`, `fr→en`, `en→de`, `de→en`, `en→ja`, `ja→en`); other pairs between the six languages are resolved via an English pivot.

JSON body:

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to translate (max 5,000 characters) |
| `from` | string | yes | Source language code: `en`, `id`, `es`, `fr`, `de`, `ja` |
| `to` | string | yes | Target language code |

**Response:** `{ "translated_text": "Selamat pagi, bagaimana kabarmu hari ini?", "from": "en", "to": "id" }`

### `POST /detect`

Detect the language of a text.

JSON body: `{ "text": "..." }`

**Response:** `{ "language": "id" }`

### `GET /languages`

List the supported language codes and translation pairs.

## Example (cURL)

```bash
curl -X POST "https://translation-api-en-id-es-fr-de-ja.p.rapidapi.com/translate" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: translation-api-en-id-es-fr-de-ja.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{"text": "Good morning, how are you today?", "from": "en", "to": "id"}'
```

A runnable Python example is in [`examples/translate_example.py`](../examples/translate_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 10 / month (hard limit) |
| PRO | $10 / month | 1,000 / month |
| ULTRA | $29 / month | 5,000 / month |
| MEGA | $75 / month | 20,000 / month |

Subscribe and manage your plan here: **[Translation API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/translation-api-en-id-es-fr-de-ja)**

Part of the [hhelll API family](../README.md#more-apis-by-hhelll).
