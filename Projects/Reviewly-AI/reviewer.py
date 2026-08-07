import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts import prompt

load_dotenv()

llm = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

chain = prompt | llm | StrOutputParser()

def review_code(code: str, language: str, review_type: str, experience_level: str):
    results = chain.invoke({
        "code": code,
        "language": language,
        "review_type": review_type,
        "experience_level": experience_level
    })
    return results

