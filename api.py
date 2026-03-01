from fastapi import FastAPI
from pydantic import BaseModel

from router import route_query

app = FastAPI(
    title="Medical AI Assistant",
    description="MedGemma-powered local medical QnA system",
    version="1.0"
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Medical AI API is running"}

@app.post("/ask")
def ask_medical_ai(query: Query):

    user_question = query.question

    response = route_query(user_question)

    return {
        "question": user_question,
        "answer": response
    }