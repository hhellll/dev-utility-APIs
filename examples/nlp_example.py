"""Text NLP Utilities API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python nlp_example.py

Summarizes a sample text, then runs sentiment, keywords, and language
detection on it.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/text-nlp-utilities-api
"""

import json
import os
import sys

import requests

HOST = "text-nlp-utilities-api.p.rapidapi.com"
BASE = f"https://{HOST}"

TEXT = (
    "The city council announced on Tuesday that a new public library will open "
    "next month in the city center. The library will offer free classes, "
    "computer access, and a large reading room for students. Residents "
    "welcomed the plan and said the library will greatly benefit local "
    "families. The mayor said more community spaces are planned for next year."
)


def post(key: str, path: str, payload: dict) -> dict:
    r = requests.post(
        f"{BASE}{path}",
        headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST},
        json=payload,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    print("Summary:")
    print(json.dumps(post(key, "/summarize", {"text": TEXT, "sentences": 2}), indent=2))

    print("\nSentiment:")
    print(json.dumps(post(key, "/sentiment", {"text": TEXT}), indent=2))

    print("\nKeywords:")
    print(json.dumps(post(key, "/keywords", {"text": TEXT, "top_n": 5}), indent=2))

    print("\nLanguage:")
    print(json.dumps(post(key, "/language", {"text": TEXT}), indent=2))


if __name__ == "__main__":
    main()
