import requests
import time

SERVICES = [
    {"name": "Ecommerce", "url": "http://localhost:8000/health"},
    {"name": "PaymentGateway", "url": "http://localhost:8001/health"},
    {"name": "AuthService", "url": "http://localhost:8002/health"},
]

def check_services():
    print("\n--- GhostOps Watcher Agent ---")
    for service in SERVICES:
        try:
            response = requests.get(service["url"], timeout=3)
            if response.status_code == 200:
                print(f"✅ {service['name']} is HEALTHY")
            else:
                print(f"❌ {service['name']} is DOWN!")
        except Exception as e:
            print(f"❌ {service['name']} is UNREACHABLE!")

while True:
    check_services()
    print("Waiting 10 seconds...")
    time.sleep(10)