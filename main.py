from fastapi import FastAPI, Query
from search_tools import search_serpapi
from llm_chain import generate_answer

app = FastAPI()

@app.get("/ask")
def ask_ai(q: str = Query(..., description="Your question")):
    search_results = search_serpapi(q)
    answer = generate_answer(q, search_results)
    return {"answer": answer}
