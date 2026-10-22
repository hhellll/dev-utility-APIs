"""OCR and PDF Tools API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python ocr_example.py scan.png
    RAPIDAPI_KEY=your_key python ocr_example.py document.pdf

Images are sent to /ocr, PDFs to /pdf-to-text; the extracted text is printed.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/ocr-and-pdf-tools-api
"""

import os
import sys

import requests

HOST = "ocr-and-pdf-tools-api.p.rapidapi.com"
BASE = f"https://{HOST}"


def headers(key: str) -> dict:
    return {"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST}


def ocr_image(key: str, path: str) -> dict:
    with open(path, "rb") as f:
        r = requests.post(
            f"{BASE}/ocr",
            headers=headers(key),
            files={"image": f},
            data={"lang": "eng"},
            timeout=120,
        )
    r.raise_for_status()
    return r.json()


def pdf_to_text(key: str, path: str) -> dict:
    with open(path, "rb") as f:
        r = requests.post(
            f"{BASE}/pdf-to-text",
            headers=headers(key),
            files={"file": f},
            data={"lang": "eng"},
            timeout=300,
        )
    r.raise_for_status()
    return r.json()


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    path = sys.argv[1]
    if path.lower().endswith(".pdf"):
        print(pdf_to_text(key, path))
    else:
        print(ocr_image(key, path)["text"])


if __name__ == "__main__":
    main()
