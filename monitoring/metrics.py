from prometheus_client import start_http_server, Gauge
import requests
import time

# Metrics define karo
service_health = Gauge('service_health', 'Service health status', ['service'])

SERVICES = [
    {"name": "Ecommerce", "url": "http://localhost:8000/health"},
    {"name": "PaymentGateway", "url": "http://localhost:8001/health"},
    {"name": "AuthService", "url": "http://localhost:8002/health"},
]

def collect_metrics():
    for service in SERVICES:
        try:
            response = requests.get(service["url"], timeout=3)
            if response.status_code == 200:
                service_health.labels(service=service["name"]).set(1)
                print(f"✅ {service['name']}: HEALTHY (1)")
            else:
                service_health.labels(service=service["name"]).set(0)
                print(f"❌ {service['name']}: DOWN (0)")
        except:
            service_health.labels(service=service["name"]).set(0)
            print(f"❌ {service['name']}: UNREACHABLE (0)")

print("🚀 GhostOps Prometheus Metrics Server starting on port 8080...")
start_http_server(8080)

while True:
    print("\n--- Collecting Metrics ---")
    collect_metrics()
    time.sleep(15)