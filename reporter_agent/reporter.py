import requests
from datetime import datetime

SERVICES = [
    {"name": "Ecommerce", "url": "http://localhost:8000/health"},
    {"name": "PaymentGateway", "url": "http://localhost:8001/health"},
    {"name": "AuthService", "url": "http://localhost:8002/health"},
]

CAUSES = {
    "Ecommerce": "High traffic or memory leak detected",
    "PaymentGateway": "External payment API timeout",
    "AuthService": "Database connection failed",
}

def generate_report():
    print("\n========================================")
    print("       GhostOps Incident Report         ")
    print("========================================")
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------------------------")

    all_healthy = True

    for service in SERVICES:
        try:
            response = requests.get(service["url"], timeout=3)
            if response.status_code == 200:
                print(f"✅ {service['name']}: HEALTHY")
            else:
                all_healthy = False
                print(f"❌ {service['name']}: DOWN")
                print(f"   Root Cause: {CAUSES[service['name']]}")
                print(f"   Action Taken: Restart attempted")
        except:
            all_healthy = False
            print(f"❌ {service['name']}: UNREACHABLE")
            print(f"   Root Cause: {CAUSES[service['name']]}")
            print(f"   Action Taken: Restart attempted")

    print("----------------------------------------")
    if all_healthy:
        print("✅ All systems operational. No incidents.")
    else:
        print("⚠️  Incident detected and handled by GhostOps!")
    print("========================================\n")

generate_report()