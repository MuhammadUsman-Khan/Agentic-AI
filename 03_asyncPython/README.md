# 03 — Async Python

## What is this?
Agents don't make one API call and stop — they make dozens, sometimes
simultaneously. Async Python lets your agent call multiple tools, APIs,
and LLMs at the same time without freezing. This is what separates a
slow agent from a fast one.

---

## Key Concepts
- Synchronous vs Asynchronous execution
- async/await syntax
- asyncio event loop
- asyncio.gather() — running tasks in parallel
- asyncio.create_task() — background tasks
- Async with real LLM API calls
- Error handling in async code

---

## Files in this Folder

| File | What it covers |
|------|----------------|
| async_await.ipynb | async/await basics, event loop, coroutines |
| asyncio_basics.ipynb | gather, create_task, timeouts, cancellation |
| parallel_api_calls.ipynb | parallel Groq API calls, async tools for agents |

---

## Important Gotchas
- `asyncio.run()` in .py files, `await` directly in Jupyter cells
- Never use `requests` in async code — use `httpx` instead
- `asyncio.gather()` runs tasks concurrently, not truly in parallel (GIL)
- If one task in gather() fails, all fail — use `return_exceptions=True`
- Don't mix sync and async code carelessly — it will deadlock
- `time.sleep()` blocks everything — always use `asyncio.sleep()` in async

---

## Resources
- https://docs.python.org/3/library/asyncio.html
- https://www.python-httpx.org/async