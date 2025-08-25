from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running fine with Phi model!"}

@app.post("/ask")
def ask_question(query: str):
    try:
        response = ollama.chat(
            model="phi",   # yahan phi likhna hai
            messages=[{"role": "user", "content": query}]
        )
        return {"answer": response["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}