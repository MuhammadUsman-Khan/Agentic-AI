# 05 — LangChain

## What is this?
LangChain is a framework that makes building LLM-powered apps easier.
Instead of writing raw API calls every time, LangChain gives you
ready-made building blocks — for prompts, models, tools, chains, and memory.
It is also the foundation LangGraph is built on top of.

---

## Key Concepts
- LangChain vs raw API — when to use which
- ChatModels — wrapping Groq in LangChain style
- Prompt Templates — reusable dynamic prompts
- Chains — connecting prompts + models + output parsers
- Output Parsers — extracting structured data from LLM responses
- LangChain Tools — wrapping functions as tools
- Memory — adding conversation history to chains
- LCEL — LangChain Expression Language (pipe syntax)

---

## Files in this Folder

| File | What it covers |
|------|----------------|
| langchain_basics.ipynb | ChatModels, prompt templates, first chain |
| chains_parsers.ipynb | LCEL chains, output parsers, structured output |
| langchain_tools_memory.ipynb | Tools, agents, conversation memory |

---

## Important Gotchas
- LangChain updates frequently — always check the version you installed
- LCEL pipe syntax (|) is the modern way — avoid old chain classes
- ChatGroq needs langchain-groq package separately
- Memory is NOT automatic — you must pass history manually or use a memory class
- LangChain tools wrap your functions — but you still write the functions
- Don't over-complicate — raw API is sometimes cleaner for simple tasks

---

## Resources
- https://python.langchain.com/docs
- https://python.langchain.com/docs/expression_language
- https://api.python.langchain.com