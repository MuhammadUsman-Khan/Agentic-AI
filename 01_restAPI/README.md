# 01 — REST APIs

## What is this?
Before talking to any LLM or building any agent, you need to know how to
communicate over the web. REST APIs are how every modern service talks to
each other — and your agents will rely on them heavily.

---

## Key Concepts
- What is an API and why agents need them
- HTTP methods — GET, POST, PUT, DELETE
- Request structure — headers, body, params
- Response structure — status codes, JSON parsing
- Error handling — timeouts, retries, bad responses
- Async HTTP requests — why speed matters for agents

---

## Files in this Folder

| File | What it covers |
|------|----------------|
| basics.ipynb | HTTP methods, requests library, JSON parsing |
| error_handling.ipynb | Status codes, retries, exception handling |
| async_requests.ipynb | httpx async client, parallel requests |

---

## Important Gotchas
- Always check `response.status_code` before parsing — never assume 200
- `response.json()` will crash if the response isn't valid JSON — wrap it
- Async requests need `httpx` not `requests` — `requests` is blocking
- Never hardcode API keys — use `.env` and `python-dotenv`
- Rate limits are real — always add delays or retry logic for agent loops

---

## Resources
- https://docs.python-requests.org
- https://www.python-httpx.org
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status