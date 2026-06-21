import chromadb
from datetime import datetime

# ChromaDB setup
client = chromadb.Client()
collection = client.create_collection("incidents")

# Past incidents data store karo
past_incidents = [
    {
        "id": "1",
        "service": "Ecommerce",
        "problem": "High CPU usage, service down",
        "solution": "Scaled up instances, cleared cache"
    },
    {
        "id": "2", 
        "service": "PaymentGateway",
        "problem": "API timeout, payment failing",
        "solution": "Restarted payment service, updated API timeout config"
    },
    {
        "id": "3",
        "service": "AuthService", 
        "problem": "Database connection failed",
        "solution": "Restarted database, cleared connection pool"
    },
    {
        "id": "4",
        "service": "Ecommerce",
        "problem": "Memory leak detected",
        "solution": "Restarted service, increased memory limit"
    },
]

# Incidents store karo
collection.add(
    documents=[f"{i['service']}: {i['problem']}" for i in past_incidents],
    ids=[i['id'] for i in past_incidents],
    metadatas=[{"solution": i['solution']} for i in past_incidents]
)

def find_similar_incident(service_name, problem):
    query = f"{service_name}: {problem}"
    results = collection.query(
        query_texts=[query],
        n_results=1
    )
    if results['metadatas'][0]:
        return results['metadatas'][0][0]['solution']
    return "No similar incident found"

# Test karo
print("\n--- GhostOps RAG Pipeline ---")
solution = find_similar_incident("AuthService", "database connection failed")
print(f"🔍 Query: AuthService - database connection failed")
print(f"💡 Similar fix found: {solution}")

solution2 = find_similar_incident("Ecommerce", "high memory usage")
print(f"\n🔍 Query: Ecommerce - high memory usage")
print(f"💡 Similar fix found: {solution2}")