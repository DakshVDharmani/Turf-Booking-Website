from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
model = pipeline('question-answering', model='your-fine-tuned-model')

@app.post("/api/chat")
async def chat(query: dict):
    result = model(question=query['query'], context='your website content')
    return {"answer": result['answer']}