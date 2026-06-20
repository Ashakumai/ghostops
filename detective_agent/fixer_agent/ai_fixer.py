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

def ai_fix(service_name):
    prompt = f"""
    You are an autonomous SRE system.
    Service '{service_name}' is DOWN.
    Provide exact terminal commands to fix this service.
    Format your response as:
    DIAGNOSIS: (one line)
    FIX COMMANDS: (exact commands)
    STATUS: (expected result after fix)
    """
    response = llm.invoke(prompt)
    return response.content

print("\n--- GhostOps AI Fixer Agent ---")
for service in SERVICES:
    if check_service(service):
        print(f"✅ {service['name']} - No fix needed")
    else:
        print(f"🔧 Fixing {service['name']}...")
        fix = ai_fix(service['name'])
        print(f"\n🤖 AI Fix Plan:\n{fix}\n")
        print("-" * 50)