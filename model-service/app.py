from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
import uvicorn

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.post("/embed")
def embed(input_data: dict):
    text = input_data["text"]
    embedding = model.encode(text).tolist()
    return {"embedding": embedding}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
