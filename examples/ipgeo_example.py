"""IP Geolocation API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python ipgeo_example.py
    RAPIDAPI_KEY=your_key python ipgeo_example.py 1.1.1.1

Looks up one IP (default 8.8.8.8) and then runs a small batch lookup.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/ip-geolocation-api25
"""

import json
import os
import sys

import requests

HOST = "ip-geolocation-api25.p.rapidapi.com"
BASE = f"https://{HOST}"


def headers(key: str) -> dict:
    return {"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST}


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"

    r = requests.get(f"{BASE}/lookup/{ip}", headers=headers(key), timeout=60)
    r.raise_for_status()
    print(f"Lookup {ip}:")
    print(json.dumps(r.json(), indent=2))

    r = requests.post(
        f"{BASE}/batch",
        headers=headers(key),
        json={"ips": ["8.8.8.8", "1.1.1.1"]},
        timeout=60,
    )
    r.raise_for_status()
    print("\nBatch:")
    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main()
