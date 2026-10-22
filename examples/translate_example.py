"""Translation API (EN ID ES FR DE JA) — Python example.

Usage:
    RAPIDAPI_KEY=your_key python translate_example.py
    RAPIDAPI_KEY=your_key python translate_example.py "Good morning" en id

With no arguments it translates a sample sentence EN -> ID and ID -> EN,
and detects the language of a sample text.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/translation-api-en-id-es-fr-de-ja
"""

import os
import sys

import requests

HOST = "translation-api-en-id-es-fr-de-ja.p.rapidapi.com"
BASE = f"https://{HOST}"


def post(key: str, path: str, payload: dict) -> dict:
    r = requests.post(
        f"{BASE}{path}",
        headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST},
        json=payload,
        timeout=120,
    )
    r.raise_for_status()
    return r.json()


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    if len(sys.argv) == 4:
        text, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
        print(post(key, "/translate", {"text": text, "from": src, "to": dst})["translated_text"])
        return

    out = post(key, "/translate", {"text": "Good morning, how are you today?", "from": "en", "to": "id"})
    print("EN -> ID:", out["translated_text"])

    out = post(key, "/translate", {"text": "Terima kasih banyak atas bantuan Anda", "from": "id", "to": "en"})
    print("ID -> EN:", out["translated_text"])

    print("Detect:", post(key, "/detect", {"text": "Selamat pagi, apa kabar hari ini?"}))


if __name__ == "__main__":
    main()
