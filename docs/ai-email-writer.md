# AI Email Writer API

Generate ready-to-send emails with AI: **write** brand-new emails from a short topic, draft **replies** to incoming emails, and brainstorm **subject-line ideas**. You control the **tone** (professional, friendly, formal, casual, or persuasive), the **length**, and the **language** — English and Indonesian are supported.

**Live on RapidAPI → [AI Email Writer API](https://rapidapi.com/Hitler-HlDevZDwP/api/ai-email-writer-api)**

**Gateway host:** `ai-email-writer-api.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/emailwriter`

Every call goes to `https://ai-email-writer-api.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `ai-email-writer-api.p.rapidapi.com` |

> **Latency note:** the generation endpoints run a large language model, so each call typically takes **5–20 seconds**. That is normal — set your client timeout accordingly (60 seconds recommended).

All endpoints accept **GET** (query parameters) or **POST** (JSON body with the same field names).

## Endpoints

### `GET|POST /write`

Write a complete new email — subject and body — from a topic.

| Parameter | Required | Notes |
|---|---|---|
| `topic` | yes | What the email is about, e.g. `Follow up on a job application` |
| `tone` | no | `professional` (default), `friendly`, `formal`, `casual`, `persuasive` |
| `language` | no | `en` (default) or `id` |
| `recipient_name` | no | Greets this person, e.g. `Sarah` |
| `sender_name` | no | Signs off with this name, e.g. `David` |
| `length` | no | `short` (~60 words), `medium` (default, ~130 words), `long` (~230 words) |

**Response:** JSON like (real output for topic `Follow up on a job application`, tone `professional`, language `en`):

```json
{
  "subject": "Following up on my job application",
  "body": "Dear Hiring Manager,\n\nI hope you are doing well. I am writing to follow up on my recent job application and to reiterate my strong interest in the position. I believe my skills and experience would be a great fit for your team, and I would welcome the opportunity to discuss how I can contribute.\n\nPlease let me know if you need any additional information from me. I am available for an interview at your convenience.\n\nThank you for your time and consideration.\n\nBest regards",
  "tone": "professional",
  "language": "en"
}
```

### `GET|POST /reply`

Draft a reply to an email you received.

| Parameter | Required | Notes |
|---|---|---|
| `original` | yes | The full text of the email you are replying to |
| `intent` | no | What your reply should say, e.g. `Accept the price of USD 1,250 including shipping, confirm delivery in 5-7 business days` |
| `tone` | no | Same tones as `/write` (default `professional`) |
| `language` | no | `en` (default) or `id` |

**Response:** the same shape as `/write` — `subject` (usually `Re: ...`), `body`, `tone`, `language` — with every point from your `intent` worked into the reply.

### `GET|POST /subject`

Generate subject-line ideas for a topic.

| Parameter | Required | Notes |
|---|---|---|
| `topic` | yes | What the email is about |
| `count` | no | How many ideas: default 5, maximum 10 |
| `tone` | no | Same tones as `/write` (default `professional`) |
| `language` | no | `en` (default) or `id` |

**Response:** JSON like:

```json
{
  "subjects": [
    "Your application status — a quick follow-up",
    "Following up on my application",
    "Checking in on next steps"
  ]
}
```

### `GET /health`

Returns `{"status": "ok"}` when the service is up.

## Example (cURL)

```bash
curl -X POST "https://ai-email-writer-api.p.rapidapi.com/write" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: ai-email-writer-api.p.rapidapi.com" \
  -H "Content-Type: application/json" \
  -d '{"topic": "Follow up on a job application", "tone": "professional", "language": "en"}'
```

## Pricing

| Plan | Price | Included requests |
|---|---|---|
| BASIC | Free | 5 / month (hard limit) |
| PRO | $5 / month | 2,000 / month |

The PRO plan is a soft limit with per-request overage of $0.005 per additional request.

Subscribe and manage your plan here: **[AI Email Writer API on RapidAPI](https://rapidapi.com/Hitler-HlDevZDwP/api/ai-email-writer-api)**

Part of the [hhelll API family](../README.md#the-api-catalog).
