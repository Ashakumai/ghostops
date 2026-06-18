from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "GhostOps"}

@app.get("/products")
def get_products():
    return {"products": ["laptop", "phone", "tablet"]}