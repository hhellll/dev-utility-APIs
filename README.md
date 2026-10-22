# Background Remover AI — API

Remove the background from any image automatically and get a clean **transparent PNG** back. Fast (about 1 second per standard image), simple, and cheap.

**Live on RapidAPI → [Background Remover AI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5)**

![Before and after](assets/comparison.jpg)

## What it does

Send an image (file upload **or** image URL) and the API returns the same image with the background removed and replaced by transparency — ready for product photos, profile pictures, design work, marketplaces, and apps.

| | |
|---|---|
| Input | JPG / PNG image file (max 12 MB) **or** a public image URL |
| Output | PNG with transparent background (RGBA) |
| Speed | ~1 second for a standard-size image |
| Endpoint | `POST /remove-background` |

## Get started

1. Subscribe to a plan on RapidAPI (the free plan includes 5 requests/month):
   **[rapidapi.com — Background Remover AI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5)**
2. Copy your `X-RapidAPI-Key` from the API playground.
3. Call the API from any language.

## Quick start

### cURL

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

### Python

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

### JavaScript (Node.js / fetch)

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

## API reference

### `POST /remove-background`

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

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Pricing

| Plan | Price | Included requests | Overage |
|---|---|---|---|
| BASIC | Free | 5 / month (hard limit) | — |
| PRO | $5 / month | 1,500 / month | $0.005 / request |
| ULTRA | $15 / month | 6,000 / month | $0.003 / request |
| MEGA | $49 / month | 25,000 / month | $0.002 / request |

Subscribe and manage your plan here: **[Background Remover AI on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5)**

## Sample files

- [`assets/before.jpg`](assets/before.jpg) — original photo
- [`assets/after.png`](assets/after.png) — the API's actual output for that photo

## FAQ

**Which images work best?**
Clear subjects with a visible contrast against the background: people, products, pets, cars, logos.

**Can I use the results commercially?**
Yes — the output images are yours to use, including for commercial projects.

**How large can the output be?**
The output keeps the input's dimensions (very large images are downscaled so the longest side is at most 3000 px).

**Where do I get help?**
Use the Discussion tab on the RapidAPI page, or open an issue in this repository.

## License

The example code in this repository is released under the [MIT License](LICENSE). The API itself is a hosted service provided via RapidAPI under its plan terms.
