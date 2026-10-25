# Speech to Text API - Whisper Transcription

Transcribe audio to text with OpenAI's **Whisper** model. The API is **asynchronous**: submit a file (or an audio URL), get a job id, then poll for the result — plain text, timestamped segments, or ready-made **SRT/VTT subtitles**.

**Live on RapidAPI → [Speech to Text API - Whisper Transcription](https://rapidapi.com/Hitler-HlDevZDwP/api/speech-to-text-api-whisper-transcription)**

**Gateway host:** `speech-to-text-api-whisper-transcription.p.rapidapi.com`

Every call goes to `https://speech-to-text-api-whisper-transcription.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `speech-to-text-api-whisper-transcription.p.rapidapi.com` |

## Endpoints

### `POST /transcribe`

Submit a transcription job. Send the audio **one** of two ways (multipart form):

| Field | Type | Required | Notes |
|---|---|---|---|
| `audio` | file | one of the two | Audio file upload (max 25 MB) |
| `audio_url` | string | one of the two | Publicly accessible audio URL |
| `language` | string | no | Language code hint (e.g. `en`, `id`); auto-detected when omitted |
| `format` | string | no | `json` (default), `srt`, or `vtt` |

**Response:** `202 Accepted` with `{ "job_id": "...", "status": "queued" }`.

### `GET /jobs/{job_id}`

Poll a job until it finishes.

**Response:** JSON with `status` — `queued` / `running` / `done` / `error`. When `done`, the result contains the transcript `text`, detected `language`, audio `duration`, and timestamped `segments` (for `format=json`), or the subtitle file content (for `format=srt` / `vtt`).

## Example (cURL)

```bash
# 1) Submit
curl -X POST "https://speech-to-text-api-whisper-transcription.p.rapidapi.com/transcribe" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: speech-to-text-api-whisper-transcription.p.rapidapi.com" \
  -F "audio=@speech.mp3" \
  -F "format=srt"
# → {"job_id": "abc123", "status": "queued"}

# 2) Poll for the result
curl "https://speech-to-text-api-whisper-transcription.p.rapidapi.com/jobs/abc123" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: speech-to-text-api-whisper-transcription.p.rapidapi.com"
```

A runnable Python example (submit + poll) is in [`examples/stt_example.py`](../examples/stt_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $9 / month | 500 / month |
| ULTRA | $29 / month | 2,000 / month |
| MEGA | $75 / month | 8,000 / month |

Subscribe and manage your plan here: **[Speech to Text API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/speech-to-text-api-whisper-transcription)**

Part of the [hhelll API family](../README.md#the-api-catalog).
