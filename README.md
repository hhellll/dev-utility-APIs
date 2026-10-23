# dev-utility-APIs

**17 production APIs on RapidAPI** by **hhelll** — image tools, website screenshots, speech-to-text, text-to-speech, OCR & PDF tools, translation, NLP utilities, IP geolocation, email validation, phone validation, domain health checks, postal codes, geocoding, VAT & IBAN validation, public holidays, and currency/crypto prices. Small, focused, self-hosted APIs — each one does one job well, with a free plan to try it out.

**16 APIs are live now.** The Weather API is built and running, and its listing is **launching soon**.

## The API catalog

| API | What it does | Free plan | Paid plans (PRO / ULTRA / MEGA) |
|---|---|---|---|
| [Background Remover AI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5) | Remove image backgrounds → transparent PNG (plus replace-background, blur-background, and image conversion endpoints) | 5 requests/month | $5 / $15 / $49 |
| [Website Screenshot and PDF API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-screenshot-and-pdf-api) — [docs](docs/website-screenshot-and-pdf-api.md) | Website screenshots, URL → PDF, and Open Graph images | 10 requests/month | $9 / $29 / $79 |
| [Speech to Text API - Whisper Transcription](https://rapidapi.com/Hitler-HlDevZDwP/api/speech-to-text-api-whisper-transcription) — [docs](docs/speech-to-text-api-whisper-transcription.md) | Async audio transcription with subtitles (SRT/VTT), powered by Whisper | 5 requests/month | $10 / $29 / $75 |
| [Text to Speech API - Natural Voices](https://rapidapi.com/Hitler-HlDevZDwP/api/text-to-speech-api-natural-voices) — [docs](docs/text-to-speech-api-natural-voices.md) | Text to speech with natural English (US/GB) and Indonesian voices | 5 requests/month | $10 / $29 / $75 |
| [OCR and PDF Tools API](https://rapidapi.com/Hitler-HlDevZDwP/api/ocr-and-pdf-tools-api) — [docs](docs/ocr-and-pdf-tools-api.md) | OCR for English & Indonesian, PDF text extraction, merge, and compress | 10 requests/month | $12 / $35 / $99 |
| [IP Geolocation API](https://rapidapi.com/Hitler-HlDevZDwP/api/ip-geolocation-api25) — [docs](docs/ip-geolocation-api.md) | IP address → country, city, timezone, and ASN — single or batch lookups | 100 requests/month | $10 / $29 / $79 |
| [Text NLP Utilities API](https://rapidapi.com/Hitler-HlDevZDwP/api/text-nlp-utilities-api) — [docs](docs/text-nlp-utilities-api.md) | Summarize, sentiment analysis, keyword extraction, and language detection | 10 requests/month | $12 / $35 / $99 |
| [Currency and Crypto Prices API](https://rapidapi.com/Hitler-HlDevZDwP/api/currency-and-crypto-prices-api) — [docs](docs/currency-and-crypto-prices-api.md) | Cached fiat exchange rates and crypto spot prices | 100 requests/month | $9 / $25 / $69 |
| [Translation API - EN ID ES FR DE JA](https://rapidapi.com/Hitler-HlDevZDwP/api/translation-api-en-id-es-fr-de-ja) — [docs](docs/translation-api-en-id-es-fr-de-ja.md) | Translation between EN, ID, ES, FR, DE, JA plus language detection | 10 requests/month | $10 / $29 / $75 |
| [Email Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/email-validation-api44) — [docs](docs/email-validation.md) | Validate email addresses: syntax, MX records, disposable & role-based detection, typo suggestions, and a 0–100 deliverability score | 5 requests/month | $9 / $19 / $39 |
| [Worldwide Postal Code API](https://rapidapi.com/Hitler-HlDevZDwP/api/worldwide-postal-code-api) — [docs](docs/postal-code.md) | 1.8M postal codes in 122 countries (GeoNames): lookup, place search, radius search, and distance between codes | 5 requests/month | $9 / $19 / $39 |
| [Phone Number Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/phone-number-validation-api3) — [docs](docs/phone-validation.md) | Parse and validate international phone numbers: carrier, line type, country, and timezones | 5 requests/month | $9 / $19 / $49 |
| [Domain Health API](https://rapidapi.com/Hitler-HlDevZDwP/api/domain-health-api) — [docs](docs/domain-health.md) | Domain health checks: DNS, SSL, RDAP/whois, email security (SPF/DMARC/MTA-STS), and an A–F health score | 5 requests/month | $10 / $25 / $49 |
| [Geocoding API](https://rapidapi.com/Hitler-HlDevZDwP/api/geocoding-api5) — [docs](docs/geocoding.md) | Forward and reverse geocoding over 236k places worldwide (GeoNames), plus nearest postal codes | 5 requests/month | $10 / $25 / $49 |
| [VAT and IBAN Validation API](https://rapidapi.com/Hitler-HlDevZDwP/api/vat-and-iban-validation-api1) — [docs](docs/vat-iban.md) | EU VAT validation via the official VIES service, EU VAT rates, and IBAN validation with bank/BIC lookup | 5 requests/month | $12 / $29 / $59 |
| [Holidays and Business Days API](https://rapidapi.com/Hitler-HlDevZDwP/api/holidays-and-business-days-api) — [docs](docs/holidays.md) | Public holidays for 200+ countries, is-holiday / is-workday checks, and business-day counting | 5 requests/month | $9 / $19 / $39 |
| Weather API - Global Forecast — [docs](docs/weather-api-global-forecast.md) | Current weather, 7-day forecast, and geocoding | *launching soon* | — |

## Get started (any API)

1. Open the API's RapidAPI page from the table above and subscribe to a plan (every API has a free plan).
2. Copy your `X-RapidAPI-Key` from the API playground.
3. Call the API from any language — each API's docs page in [`docs/`](docs/) has endpoints and a cURL example, and the [`examples/`](examples/) folder has runnable code for several of them.

---

## Featured API: Background Remover AI

Remove the background from any image automatically and get a clean **transparent PNG** back. Fast (about 1 second per standard image), simple, and cheap.

**Live on RapidAPI → [Background Remover AI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5)**

![Before and after](assets/comparison.jpg)

### What it does

Send an image (file upload **or** image URL) and the API returns the same image with the background removed and replaced by transparency — ready for product photos, profile pictures, design work, marketplaces, and apps.

| | |
|---|---|
| Input | JPG / PNG image file (max 12 MB) **or** a public image URL |
| Output | PNG with transparent background (RGBA) |
| Speed | ~1 second for a standard-size image |
| Endpoint | `POST /remove-background` |

### Quick start

#### cURL

```bash
# Upload a file
curl -X POST "https://background-remover-ai5.p.rapidapi.com/remove-background" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: background-remover-ai5.p.rapidapi.com" \
  -F "image=@photo.jpg" \
  --output result.png

# Or send an image URL
curl -X POST "https://background-remover-ai5.p.rapidapi.com/remove-background" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: background-remover-ai5.p.rapidapi.com" \
  -F "image_url=https://example.com/photo.jpg" \
  --output result.png
```

#### Python

```python
import requests

url = "https://background-remover-ai5.p.rapidapi.com/remove-background"
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "background-remover-ai5.p.rapidapi.com",
}

with open("photo.jpg", "rb") as f:
    r = requests.post(url, headers=headers, files={"image": f})

r.raise_for_status()
with open("result.png", "wb") as out:
    out.write(r.content)
print("Saved result.png")
```

#### JavaScript (Node.js / fetch)

```js
import { readFile, writeFile } from "node:fs/promises";

const form = new FormData();
form.append("image", new Blob([await readFile("photo.jpg")]), "photo.jpg");

const res = await fetch("https://background-remover-ai5.p.rapidapi.com/remove-background", {
  method: "POST",
  headers: {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "background-remover-ai5.p.rapidapi.com",
  },
  body: form,
});

if (!res.ok) throw new Error(`API error: ${res.status}`);
await writeFile("result.png", Buffer.from(await res.arrayBuffer()));
console.log("Saved result.png");
```

Full runnable examples are in the [`examples/`](examples/) folder.

### API reference

#### `POST /remove-background`

Send **one** of:

| Field | Type | Required | Notes |
|---|---|---|---|
| `image` | file (multipart) | one of the two | JPG/PNG, max 12 MB |
| `image_url` | string (form field) | one of the two | Publicly accessible image URL |

**Response:** `200 OK` with `Content-Type: image/png` — the image with a transparent background.

**Errors:**

| Status | Meaning |
|---|---|
| `400` | No image provided, or the image could not be read |
| `413` | Image larger than 12 MB |
| `429` | Monthly quota for your plan is used up |
| `401/403` | Missing or invalid RapidAPI key |

#### `GET /health`

Returns `{"status": "ok"}` when the service is up.

### Pricing

| Plan | Price | Included requests | Overage |
|---|---|---|---|
| BASIC | Free | 5 / month (hard limit) | — |
| PRO | $5 / month | 1,500 / month | $0.005 / request |
| ULTRA | $15 / month | 6,000 / month | $0.003 / request |
| MEGA | $49 / month | 25,000 / month | $0.002 / request |

Subscribe and manage your plan here: **[Background Remover AI on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5)**

### Sample files

- [`assets/before.jpg`](assets/before.jpg) — original photo
- [`assets/after.png`](assets/after.png) — the API's actual output for that photo

### FAQ

**Which images work best?**
Clear subjects with a visible contrast against the background: people, products, pets, cars, logos.

**Can I use the results commercially?**
Yes — the output images are yours to use, including for commercial projects.

**How large can the output be?**
The output keeps the input's dimensions (very large images are downscaled so the longest side is at most 3000 px).

**Where do I get help?**
Use the Discussion tab on the RapidAPI page, or open an issue in this repository.

## License

The example code in this repository is released under the [MIT License](LICENSE). The APIs themselves are hosted services provided via RapidAPI under their plan terms.
