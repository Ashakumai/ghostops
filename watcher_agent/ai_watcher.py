from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant" ,
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

def ai_analyze(service_name):
    prompt = f"""
    Service '{service_name}' is DOWN in our infrastructure.
    As an SRE expert, provide:
    1. Most likely root cause
    2. Immediate fix steps
    3. Prevention for future
    Keep response concise and technical.
    """
    response = llm.invoke(prompt)
    return response.content

print("\n--- GhostOps AI Watcher Agent ---")
for service in SERVICES:
    if check_service(service):
        print(f"✅ {service['name']} is HEALTHY")
    else:
        print(f"❌ {service['name']} is DOWN - Asking AI...")
        analysis = ai_analyze(service['name'])
        print(f"\n🤖 AI Analysis:\n{analysis}\n")