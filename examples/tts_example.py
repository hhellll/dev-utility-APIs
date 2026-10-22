"""Text to Speech API — Python example.

Usage:
    RAPIDAPI_KEY=your_key python tts_example.py "Hello from the TTS API"
    RAPIDAPI_KEY=your_key python tts_example.py "Selamat pagi!" id_ID-news_tts-medium

Saves the synthesized audio to speech.wav.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/text-to-speech-api-natural-voices
"""

import os
import sys

import requests

HOST = "text-to-speech-api-natural-voices.p.rapidapi.com"
BASE = f"https://{HOST}"


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")

    text = sys.argv[1] if len(sys.argv) > 1 else "Hello! This is a test of the text to speech API."
    voice = sys.argv[2] if len(sys.argv) > 2 else "en_US-lessac-medium"

    headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST}

    # Optional: list the available voices first
    voices = requests.get(f"{BASE}/voices", headers=headers, timeout=60)
    voices.raise_for_status()
    print("Voices:", [v["id"] for v in voices.json()])

    r = requests.post(
        f"{BASE}/tts",
        headers=headers,
        json={"text": text, "voice": voice, "speed": 1.0},
        timeout=120,
    )
    r.raise_for_status()
    with open("speech.wav", "wb") as out:
        out.write(r.content)
    print("Saved speech.wav")


if __name__ == "__main__":
    main()
