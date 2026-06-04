import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from rich import print

load_dotenv()

app_env = os.getenv("APP_ENV")
openai_api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/debug/env")
def debug_env():
    return {
        "APP_ENV": app_env,
        "OPENAI_API_KEY_EXISTS": openai_api_key is not None,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)