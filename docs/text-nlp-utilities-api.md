# Text NLP Utilities API

Four everyday text tools in one API: **extractive summarization**, **sentiment analysis**, **keyword extraction**, and **language detection** — for English and Indonesian text (summaries and keywords work for both; sentiment is optimized for English).

**Live on RapidAPI → [Text NLP Utilities API](https://rapidapi.com/Hitler-HlDevZDwP/api/text-nlp-utilities-api)**

**Gateway host:** `text-nlp-utilities-api.p.rapidapi.com`

Every call goes to `https://text-nlp-utilities-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `text-nlp-utilities-api.p.rapidapi.com` |

## Endpoints

All endpoints are `POST` with a JSON body.

### `POST /summarize`

Extractive summary: picks the most informative sentences from the text.

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to summarize |
| `sentences` | int | no | Number of sentences to return (default 3) |

**Response:** `{ "summary": "...", "sentences": [...], "sentence_count": 3, "original_sentence_count": 12 }`

### `POST /sentiment`

Sentiment analysis (VADER — optimized for English; a note about this is included in every response).

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to analyze |

**Response:** `{ "label": "positive" | "neutral" | "negative", "scores": { "positive": 0.0, "neutral": 0.0, "negative": 0.0, "compound": 0.0 } }`

### `POST /keywords`

Keyword / keyphrase extraction (YAKE).

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to extract from |
| `top_n` | int | no | Max keywords to return (default 10) |

**Response:** ranked keywords with scores (lower score = more relevant).

### `POST /language`

Detect the language of a text.

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Text to identify |

**Response:** `{ "language": "id", "language_name": "Indonesian", "confidence": 1.0 }`

## Example (cURL)

```bash
curl -X POST "https://text-nlp-utilities-api.p.rapidapi.com/summarize" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: text-nlp-utilities-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long article text here...", "sentences": 2}'
```

A runnable Python example is in [`examples/nlp_example.py`](../examples/nlp_example.py).

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $12 / month | 10,000 / month |
| ULTRA | $35 / month | 50,000 / month |
| MEGA | $99 / month | 200,000 / month |

Subscribe and manage your plan here: **[Text NLP Utilities API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/text-nlp-utilities-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
