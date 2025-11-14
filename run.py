python
import argparse
from llama_cpp import Llama
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
model = None

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temp: float = 0.7

@app.post("/generate")
async def generate(request: GenerateRequest):
    output = model(
        request.prompt,
        max_tokens=request.max_tokens,
        temperature=request.temp,
        stop=["</s>"]
    )
    return {"text": output["choices"][0]["text"]}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--temp", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()

    model = Llama(model_path=args.model, n_ctx=4096)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
