from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "version": os.getenv("APP_VERSION", "v4.0"),
        "status": "謝謝老師，這是我的第一個 ArgoCD Demo！",
    }
