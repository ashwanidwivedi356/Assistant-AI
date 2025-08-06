from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

openrouter_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    openai_api_key=openrouter_key,
    openai_api_base="https://openrouter.ai/api/v1",  
    model="mistralai/mistral-7b-instruct:free",
   
)
prompt_template = PromptTemplate.from_template("""
You are a helpful AI assistant.

Use the following web search results to answer the user's question.

Search Results:
{search_results}

User Question:
{query}

Answer in a simple and clear manner.
""")

def generate_answer(query: str, search_results: str):
    prompt = prompt_template.format(search_results=search_results, query=query)
    return llm.predict(prompt)
