"""Speech to Text API (Whisper) — Python example.

Usage:
    RAPIDAPI_KEY=your_key python stt_example.py speech.mp3
    RAPIDAPI_KEY=your_key python stt_example.py --url https://example.com/speech.mp3

Submits a transcription job, polls until it is done, and prints the result.

Get your key by subscribing (free plan available) at:
    https://rapidapi.com/Hitler-HlDevZDwP/api/speech-to-text-api-whisper-transcription
"""

import os
import sys
import time

import requests

HOST = "speech-to-text-api-whisper-transcription.p.rapidapi.com"
BASE = f"https://{HOST}"


def headers(key: str) -> dict:
    return {"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST}


def submit(key: str, args: list[str]) -> str:
    if args[0] == "--url":
        r = requests.post(
            f"{BASE}/transcribe",
            headers=headers(key),
            data={"audio_url": args[1], "format": "json"},
            timeout=60,
        )
    else:
        with open(args[0], "rb") as f:
            r = requests.post(
                f"{BASE}/transcribe",
                headers=headers(key),
                files={"audio": f},
                data={"format": "json"},
                timeout=60,
            )
    r.raise_for_status()
    return r.json()["job_id"]


def poll(key: str, job_id: str) -> dict:
    while True:
        r = requests.get(f"{BASE}/jobs/{job_id}", headers=headers(key), timeout=60)
        r.raise_for_status()
        job = r.json()
        print("status:", job["status"])
        if job["status"] == "done":
            return job
        if job["status"] == "error":
            sys.exit(f"Transcription failed: {job}")
        time.sleep(5)


def main() -> None:
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY first (see the RapidAPI page for your key).")
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    job_id = submit(key, sys.argv[1:])
    print("job_id:", job_id)
    job = poll(key, job_id)
    result = job.get("result", job)
    print("\nTranscript:\n", result.get("text", result))


if __name__ == "__main__":
    main()
