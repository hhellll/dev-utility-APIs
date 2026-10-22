"""Website Screenshot and PDF API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python screenshot_example.py https://example.com

Saves screenshot.png and og-image.png next to this script's working directory.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/website-screenshot-and-pdf-api
"""

import os
import sys

import requests

HOST = "website-screenshot-and-pdf-api.p.rapidapi.com"
BASE = f"https://{HOST}"


def headers(key: str) -> dict:
    return {"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST}


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"

    # 1) Screenshot
    r = requests.post(
        f"{BASE}/screenshot",
        headers=headers(key),
        json={"url": url, "width": 1280, "height": 800, "format": "png"},
        timeout=120,
    )
    r.raise_for_status()
    with open("screenshot.png", "wb") as out:
        out.write(r.content)
    print("Saved screenshot.png")

    # 2) Open Graph image
    r = requests.post(
        f"{BASE}/og",
        headers=headers(key),
        json={"title": "My Page Title", "subtitle": "Generated with the OG endpoint"},
        timeout=120,
    )
    r.raise_for_status()
    with open("og-image.png", "wb") as out:
        out.write(r.content)
    print("Saved og-image.png")


if __name__ == "__main__":
    main()
