# Reviewly AI — AI-Powered Code Reviewer

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-F54F31?style=for-the-badge&logo=groq&logoColor=white)
![LLM](https://img.shields.io/badge/Model-LLaMA3.3--70B-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Review Types](https://img.shields.io/badge/Review%20Types-4-blue?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-8+-orange?style=for-the-badge)
![Experience Levels](https://img.shields.io/badge/Experience%20Levels-3-teal?style=for-the-badge)

---

## Overview

Reviewly AI is a professional AI-powered code review tool built with LangChain and Streamlit.
It takes your code, analyzes it based on your chosen review type and experience level,
and returns structured, actionable feedback — instantly.

Designed for developers who want fast, honest, and specific code reviews
without waiting for a senior engineer to be available.

---

## What it does

- Detects bugs, logical errors and edge cases in your code
- Suggests improvements based on language-specific best practices
- Rewrites a complete improved version with inline comments explaining every change
- Gives an honest overall quality assessment with a clear next step
- Adjusts feedback depth and technicality based on your experience level

---

## Tech Stack

![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Inference-F54F31?style=for-the-badge&logo=groq&logoColor=white)
![LLaMA](https://img.shields.io/badge/Model-LLaMA3.3--70B%20Versatile-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DotEnv](https://img.shields.io/badge/.ENV-Dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)


---

## Project Structure

```
Reviewly-AI/
│
├── app.py ← Streamlit UI — input, layout, display
├── reviewer.py ← LangChain chain — LLM setup and invocation
├── prompts.py ← Prompt templates — system prompt and human prompt
├── requirements.txt ← Python dependencies
├── demo.mp4 ← Demo video
├── .env ← API keys (not pushed to GitHub)
├── README.md ← Project documentation
└── .gitignore ← ignoring .env files
```

---

## Setup & Run

### 1. Clone the Repository

```
git clone https://github.com/MuhammadUsman-Khan/Reviewly-AI.git
cd Reviewly-AI
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env` File
```
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free API key at https://console.groq.com

### 4. Run the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## Features

| Feature | Details |
|---------|---------|
| Languages | Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, Other |
| Review Types | Bug Detection, Code Quality, Performance, Security |
| Experience Levels | Beginner, Intermediate, Senior |
| Output Sections | Issues Found, Suggestions, Improved Code, Summary |
| Download | Export full review as `.md` file |
| Live Stats | Real-time line and character count |

---

## Review Type Guidelines

| Review Type | Focus Areas |
|-------------|-------------|
| Bug Detection | Logical errors, runtime exceptions, edge cases, null handling |
| Code Quality | Readability, naming conventions, DRY, SOLID principles |
| Performance | Time complexity, space complexity, memory leaks, optimization |
| Security | Injection risks, authentication flaws, input validation, data exposure |

---

## How it Works

```
User Input (code + settings)
            │
            ▼
ChatPromptTemplate
├── System Prompt — senior reviewer persona + guidelines per review type + experience level
└── Human Prompt — language, review type, experience level, code block
            │
            ▼
ChatGroq (LLaMA3.3-70B-Versatile)   
            │
            ▼
StrOutputParser
            │
            ▼
Structured Output
├── ## Issues Found
├── ## Suggestions
├── ## Improved Code
└── ## Summary
            │
            ▼
Streamlit UI Display + Download Button
```

---

## Key Files Explained

**`prompts.py`**
Contains the system prompt that establishes the LLM's reviewer persona as a senior software
engineer with 15+ years of experience. Includes specific guidelines per review type and per
experience level to ensure feedback is always relevant and appropriately technical.

**`reviewer.py`**
Builds the LangChain LCEL chain using the pipe operator:
`prompt | llm | StrOutputParser()` and exposes a single `review_code()` function
that `app.py` calls with four parameters.

**`app.py`**
Pure Streamlit UI. Handles all user input via sidebar and text area,
calls `review_code()` on submit, and displays structured markdown results
with a download option. No LangChain logic here.

---

## Demo

> A walkthrough of Reviewly AI reviewing a Python performance issue.

https://github.com/MuhammadUsman-Khan/Reviewly-AI/blob/main/demo.mp4

---

## Future Improvements

- [ ] Add support for file upload (.py, .js, .ts etc)
- [ ] Add review history — save past reviews locally
- [ ] Add line-by-line inline comments on the original code
- [ ] Support multiple files in one review session
- [ ] Deploy to Streamlit Cloud for public access
- [ ] Add token usage tracker to monitor API consumption

---

## Author

**Muhammad Usman Khan**

[![GitHub](https://img.shields.io/badge/GitHub-MuhammadUsman--Khan-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuhammadUsman-Khan)

---

*If you found this project useful, consider giving it a ⭐ — it helps others discover it!*