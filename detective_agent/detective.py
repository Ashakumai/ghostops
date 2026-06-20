import requests

SERVICES = [
    {"name": "Ecommerce", "url": "http://localhost:8000/health"},
    {"name": "PaymentGateway", "url": "http://localhost:8001/health"},
    {"name": "AuthService", "url": "http://localhost:8002/health"},
]

def diagnose(service_name):
    print(f"\n🔍 Detective Agent investigating: {service_name}")
    
    causes = {
        "Ecommerce": "Possible cause: High traffic or memory leak detected",
        "PaymentGateway": "Possible cause: External payment API timeout",
        "AuthService": "Possible cause: Database connection failed",
    }
    
    print(f"📋 Root Cause: {causes.get(service_name, 'Unknown error')}")
    print(f"💡 Suggested Fix: Restart {service_name} service")

def check_and_diagnose():
    print("\n--- GhostOps Detective Agent ---")
    for service in SERVICES:
        try:
            response = requests.get(service["url"], timeout=3)
            if response.status_code == 200:
                print(f"✅ {service['name']} is HEALTHY - No action needed")
            else:
                diagnose(service["name"])
        except Exception:
            diagnose(service["name"])

check_and_diagnose()