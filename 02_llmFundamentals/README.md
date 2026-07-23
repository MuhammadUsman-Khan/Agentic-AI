# 02 — LLM Fundamentals

## What is this?
Before building agents, you need to understand how LLMs actually work under
the hood — how they read input, generate output, and why they behave the way
they do. This folder covers the core concepts you'll use in every single
project going forward.

---

## Key Concepts
- What is an LLM and how it generates text (tokens, not words)
- Context window — what it is and why it limits your agent
- System prompts — how to control LLM behavior
- Temperature & top_p — controlling randomness
- Groq API — fastest free LLM inference available
- Chat format — roles (system, user, assistant)
- Token counting — why it matters for cost and limits

---

## Files in this Folder

| File | What it covers |
|------|----------------|
| tokens_context.ipynb | Tokens, context window, token counting |
| system_prompts.ipynb | System vs user prompts, roles, behavior control |
| groq_basics.ipynb | Groq API setup, first LLM call, parameters |

---

## Important Gotchas
- LLMs don't "think" — they predict the next token probabilistically
- Context window fills up fast in agent loops — always track token usage
- Temperature 0 = deterministic, Temperature 1 = creative/random
- System prompt is your most powerful tool — don't ignore it
- Groq is free but has rate limits — add delays in loops
- Messages must follow role order: system → user → assistant → user...

---

## Resources
- https://console.groq.com/docs
- https://platform.openai.com/tokenizer (visualize tokens)
- https://tiktokenizer.vercel.app