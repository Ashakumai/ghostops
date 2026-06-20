from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "AuthService"}

@app.post("/login")
def login():
    success = random.choice([True, True, True, False])
    if success:
        return {"status": "success", "token": "abc123xyz"}
    return {"status": "failed", "error": "Invalid credentials"}