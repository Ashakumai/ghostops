from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

SERVICES = [
    {"name": "Ecommerce", "url": "http://localhost:8000/health"},
    {"name": "PaymentGateway", "url": "http://localhost:8001/health"},
    {"name": "AuthService", "url": "http://localhost:8002/health"},
]

def check_service(service):
    try:
        response = requests.get(service["url"], timeout=3)
        return response.status_code == 200
    except:
        return False

def ai_diagnose(service_name):
    prompt = f"""
    You are an expert SRE engineer.
    Service '{service_name}' is DOWN.
    Analyze and provide:
    1. Root cause analysis
    2. Step by step fix
    3. How to prevent this in future
    Be specific and technical.
    """
    response = llm.invoke(prompt)
    return response.content

print("\n--- GhostOps AI Detective Agent ---")
for service in SERVICES:
    if check_service(service):
        print(f"✅ {service['name']} - No investigation needed")
    else:
        print(f"🔍 Investigating {service['name']}...")
        diagnosis = ai_diagnose(service['name'])
        print(f"\n🤖 AI Diagnosis:\n{diagnosis}\n")
        print("-" * 50)