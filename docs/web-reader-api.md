# Web Reader API

Turn any web page into clean, LLM-ready **markdown or plain text**: send a URL and get the readable content with navigation, ads and boilerplate stripped out — plus rich metadata (title, description, author, publish date, site name, language), **word count** and **estimated reading time**. Built for **AI agents, RAG pipelines**, research tools and reading apps. Extraction is powered by trafilatura; the fetcher is SSRF-protected (private and reserved addresses are rejected), with a 5 MB page limit and a 10-minute cache for repeated URLs.

**Live on RapidAPI → [Web Reader API](https://rapidapi.com/Hitler-HlDevZDwP/api/web-reader-api4)**

**Gateway host:** `web-reader-api4.p.rapidapi.com`
**Base URL (origin):** `https://149-118-58-54.sslip.io/webreader`

Every call goes to `https://web-reader-api4.p.rapidapi.com<path>` with these headers:

| Header | Value |
|---|---|
| `X-RapidAPI-Key` | your RapidAPI key |
| `X-RapidAPI-Host` | `web-reader-api4.p.rapidapi.com` |

## Endpoints

### `GET /read?url=https://example.com&format=markdown`

Read one web page. `format` is `markdown` (default) or `text`.

### `POST /read`

Same as above with a JSON body: `{"url": "https://example.com", "format": "markdown"}`.

### `POST /batch` (PRO plan)

Read up to 10 URLs in one call: `{"urls": ["https://example.com", "https://example.org"], "format": "markdown"}`.

**Response:** JSON with `success`, `url`, `final_url`, `title`, `description`, `author`, `published_date`, `site_name`, `language`, `format`, `content`, `word_count`, `reading_time_min`, `cached` and `fetch_ms`.

## Pricing

| Plan | Price | Included requests | Extra requests |
|---|---|---|---|
| BASIC | Free | 100 / month (hard limit) | — |
| PRO | $1 / month | 10,000 / month | $0.001 per request |
