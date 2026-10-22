"""Background Remover AI — Python example.

Usage:
    RAPIDAPI_KEY=your_key python python_example.py photo.jpg
    RAPIDAPI_KEY=your_key python python_example.py --url https://example.com/photo.jpg

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/background-remover-ai5
"""

import os
import sys

import requests

API_URL = "https://background-remover-ai5.p.rapidapi.com/remove-background"
API_HOST = "background-remover-ai5.p.rapidapi.com"


def remove_background_from_file(path: str, key: str) -> bytes:
    with open(path, "rb") as f:
        r = requests.post(
            API_URL,
            headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": API_HOST},
            files={"image": f},
            timeout=120,
        )
    r.raise_for_status()
    return r.content


def remove_background_from_url(image_url: str, key: str) -> bytes:
    r = requests.post(
        API_URL,
        headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": API_HOST},
        data={"image_url": image_url},
        timeout=120,
    )
    r.raise_for_status()
    return r.content


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    if args[0] == "--url":
        png = remove_background_from_url(args[1], key)
    else:
        png = remove_background_from_file(args[0], key)

    with open("result.png", "wb") as out:
        out.write(png)
    print("Saved result.png")


if __name__ == "__main__":
    main()
