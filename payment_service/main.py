from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "PaymentGateway"}

@app.post("/process-payment")
def process_payment():
    success = random.choice([True, True, True, False])
    if success:
        return {"status": "success", "transaction_id": "TXN12345"}
    return {"status": "failed", "error": "Gateway timeout"}