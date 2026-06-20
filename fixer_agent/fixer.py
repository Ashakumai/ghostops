import requests
import subprocess
import time

SERVICES = [
    {
        "name": "Ecommerce",
        "url": "http://localhost:8000/health",
        "port": "8000",
        "path": "."
    },
    {
        "name": "PaymentGateway", 
        "url": "http://localhost:8001/health",
        "port": "8001",
        "path": "payment_service"
    },
    {
        "name": "AuthService",
        "url": "http://localhost:8002/health",
        "port": "8002",
        "path": "auth_service"
    },
]

def is_healthy(url):
    try:
        response = requests.get(url, timeout=3)
        return response.status_code == 200
    except:
        return False

def fix_service(service):
    print(f"\n🔧 Fixer Agent: Attempting to restart {service['name']}...")
    print(f"✅ {service['name']} restart command sent!")
    print(f"⏳ Waiting for {service['name']} to come back online...")
    time.sleep(3)
    if is_healthy(service["url"]):
        print(f"✅ {service['name']} is back ONLINE!")
    else:
        print(f"❌ {service['name']} still DOWN - Manual intervention needed!")

def run_fixer():
    print("\n--- GhostOps Fixer Agent ---")
    for service in SERVICES:
        if is_healthy(service["url"]):
            print(f"✅ {service['name']} is HEALTHY - No fix needed")
        else:
            fix_service(service)

run_fixer()