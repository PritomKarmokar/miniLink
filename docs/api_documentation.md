## `miniLink` API documentation

- This document provides the currently implemented endpoints.

Base paths
- Shortener endpoints are available at the project root (see [shortener/urls.py](shortener/urls.py)).
- The Django admin is available under /miniLink/admin/ (see [miniLink/urls.py](miniLink/urls.py)).

`Endpoints`

1. Generate short URL
- Method: `POST`
- Path: `/api/generate-short-url/`

`Request`
- Content-Type: application/json
- Body schema:
```json
{
  "url": "string (required, max length 2048)"
}
```
- `Example request (curl)`
```sh
curl -X POST "http://localhost:8000/api/generate-short-url/" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/very/long/path"}'
```

- `Example successful response (HTTP 201)`
```json
{
  "code": "MINILINK_SGS_200",
  "lang": "en",
  "message": "Short url generated successfully.",
  "data": {
    "short_url": "http://localhost:8000/01F3...token"
  }
}
```
2. Redirect short URL
- Method: `GET`
- Path: /`<token>`/

- `Example Request`: `GET` http://localhost:8000/01F3...token/

- If found: HTTP 302 redirect to the original URL.