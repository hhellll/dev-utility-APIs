# Website Screenshot and PDF API

Render any web page with a real headless browser and get back a **screenshot**, a **PDF**, or a ready-made **Open Graph image** — no browser infrastructure to run yourself.

**Live on RapidAPI → [Website Screenshot and PDF API](https://rapidapi.com/Hitler-HlDevZDwP/api/website-screenshot-and-pdf-api)**

**Gateway host:** `website-screenshot-and-pdf-api.p.rapidapi.com`

Every call goes to `https://website-screenshot-and-pdf-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `website-screenshot-and-pdf-api.p.rapidapi.com` |

## Endpoints

### `POST /screenshot`

Render a URL and return a screenshot image.

JSON body:

| Field | Type | Required | Notes |
|---|---|---|---|
| `url` | string | yes | Page to render |
| `width` | int | no | Viewport width in px (default 1280) |
| `height` | int | no | Viewport height in px (default 800) |
| `full_page` | bool | no | Capture the full scrollable page instead of the viewport |
| `format` | string | no | `png` (default) or `jpg` |

**Response:** `200 OK` with the image bytes (`image/png` or `image/jpeg`).

### `POST /url-to-pdf`

Render a URL and return it as a PDF document.

JSON body: `{ "url": "https://example.com" }`

**Response:** `200 OK` with `Content-Type: application/pdf`.

### `POST /og`

Generate a 1200×630 Open Graph / social-share image from text.

JSON body:

| Field | Type | Required | Notes |
|---|---|---|---|
| `title` | string | yes | Main headline |
| `subtitle` | string | no | Smaller line under the title |

**Response:** `200 OK` with `Content-Type: image/png`.

## Example (cURL)

```bash
curl -X POST "https://website-screenshot-and-pdf-api.p.rapidapi.com/screenshot" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: website-screenshot-and-pdf-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "width": 1280, "height": 800}' \
  --output screenshot.png
```

A runnable Python example is in [`examples/screenshot_example.py`](../examples/screenshot_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 10 / month (hard limit) |
| PRO | $9 / month | 2,000 / month |
| ULTRA | $29 / month | 15,000 / month |
| MEGA | $79 / month | 50,000 / month |

Subscribe and manage your plan here: **[Website Screenshot and PDF API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/website-screenshot-and-pdf-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
