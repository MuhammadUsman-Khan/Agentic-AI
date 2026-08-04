# 04 — Function Calling / Tool Use

## What is this?
This is where your LLM stops being a chatbot and starts being an AGENT.
Function calling lets the LLM decide WHEN to use a tool, WHICH tool to use,
and WHAT arguments to pass — all by itself. You define the tools, the LLM
decides how and when to use them.

---

## Key Concepts
- What is function calling / tool use
- Defining tool schemas (telling LLM what tools exist)
- LLM decides when to call a tool vs answer directly
- Parsing tool call responses from the LLM
- Executing the actual function in Python
- Feeding results back to the LLM
- Multi-tool use — LLM calling multiple tools in one turn

---

## Files in this Folder

| File | What it covers |
|------|----------------|
| tool_schemas.ipynb | Defining tools, schema structure, JSON format |
| parsing_responses.ipynb | Parsing LLM tool call decisions, executing functions |
| multi_tool_use.ipynb | Multiple tools, LLM choosing between them, loops |

---

## Important Gotchas
- The LLM does NOT run your function — YOU run it and send results back
- Always validate tool arguments before executing — LLM can hallucinate args
- Tool descriptions matter a lot — vague descriptions = wrong tool choices
- Always handle the case where LLM replies directly without calling a tool
- Use temperature=0 for tool calling — you want deterministic decisions
- The loop is: LLM decides → you execute → you send result → LLM continues

---

## Resources
- https://console.groq.com/docs/tool-use
- https://platform.openai.com/docs/guides/function-calling