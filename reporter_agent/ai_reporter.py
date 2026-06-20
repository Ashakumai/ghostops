from langchain_groq import ChatGroq
from dotenv import load_dotenv
from datetime import datetime
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

def generate_ai_report(down_services):
    services_list = ", ".join(down_services)
    prompt = f"""
    You are GhostOps AI Reporter.
    Generate a professional incident report for these down services: {services_list}
    
    Include:
    1. Incident Summary
    2. Impact Assessment
    3. Root Cause
    4. Actions Taken
    5. Resolution Status
    6. Prevention Recommendations
    
    Keep it professional and concise.
    """
    response = llm.invoke(prompt)
    return response.content

print("\n" + "="*50)
print("     GhostOps AI Incident Report")
print("="*50)
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-"*50)

down_services = []
for service in SERVICES:
    if check_service(service):
        print(f"✅ {service['name']}: HEALTHY")
    else:
        print(f"❌ {service['name']}: DOWN")
        down_services.append(service['name'])

print("-"*50)

if down_services:
    print("\n🤖 Generating AI Incident Report...\n")
    report = generate_ai_report(down_services)
    print(report)
else:
    print("✅ All systems operational. No incidents!")

print("="*50)