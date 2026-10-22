# OCR and PDF Tools API

One API for everyday document work: **OCR** (text recognition for English and Indonesian), **PDF text extraction** (with OCR fallback for scanned pages), **PDF merge**, and **PDF compress**.

**Live on RapidAPI → [OCR and PDF Tools API](https://rapidapi.com/Hitler-HlDevZDwP/api/ocr-and-pdf-tools-api)**

**Gateway host:** `ocr-and-pdf-tools-api.p.rapidapi.com`

Every call goes to `https://ocr-and-pdf-tools-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `ocr-and-pdf-tools-api.p.rapidapi.com` |

## Endpoints

All endpoints accept `multipart/form-data` uploads.

### `POST /ocr`

Extract text from an image.

| Field | Type | Required | Notes |
|---|---|---|---|
| `image` | file | yes | Image file (PNG, JPG, …) |
| `lang` | string | no | `eng` (default) or `ind` |

**Response:** JSON `{ "text": "...", "language": "eng" }`.

### `POST /pdf-to-text`

Extract text from a PDF, page by page. Pages with embedded text are read directly; scanned/image-only pages are rendered and OCR'd automatically.

| Field | Type | Required | Notes |
|---|---|---|---|
| `file` | file | yes | PDF file |
| `lang` | string | no | OCR language: `eng` (default) or `ind` |

**Response:** JSON with one entry per page: `{ "page": 1, "text": "...", "source": "embedded" | "ocr" }`.

### `POST /pdf-merge`

Merge two or more PDFs into one, in upload order.

| Field | Type | Required | Notes |
|---|---|---|---|
| `files` | file (repeat the field) | yes | One PDF per `files` part |

**Response:** `200 OK` with `Content-Type: application/pdf` (page count in the `x-page-count` header).

### `POST /pdf-compress`

Compress a PDF (garbage collection, dedup, deflate).

| Field | Type | Required | Notes |
|---|---|---|---|
| `file` | file | yes | PDF file |

**Response:** `200 OK` with `Content-Type: application/pdf` (original/compressed sizes in the `x-original-size` / `x-compressed-size` headers).

Uploads are capped at 20 MB (larger uploads return `413`).

## Example (cURL)

```bash
curl -X POST "https://ocr-and-pdf-tools-api.p.rapidapi.com/ocr" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: ocr-and-pdf-tools-api.p.rapidapi.com" \
  -F "image=@scan.png" \
  -F "lang=eng"
```

A runnable Python example is in [`examples/ocr_example.py`](../examples/ocr_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 10 / month (hard limit) |
| PRO | $12 / month | 2,000 / month |
| ULTRA | $35 / month | 10,000 / month |
| MEGA | $99 / month | 40,000 / month |

Subscribe and manage your plan here: **[OCR and PDF Tools API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/ocr-and-pdf-tools-api)**

Part of the [hhelll API family](../README.md#more-apis-by-hhelll).
