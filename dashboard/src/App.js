import { useState, useEffect } from "react";

const SERVICES = [
  { name: "Ecommerce", port: 8000 },
  { name: "PaymentGateway", port: 8001 },
  { name: "AuthService", port: 8002 },
];

function App() {
  const [statuses, setStatuses] = useState({});

  const checkServices = async () => {
    const results = {};
    for (const service of SERVICES) {
      try {
        const res = await fetch(`http://localhost:${service.port}/health`);
        results[service.name] = res.ok ? "HEALTHY" : "DOWN";
      } catch {
        results[service.name] = "DOWN";
      }
    }
    setStatuses(results);
  };

  useEffect(() => {
    checkServices();
    const interval = setInterval(checkServices, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ background: "#0d1117", minHeight: "100vh", padding: "40px", fontFamily: "monospace" }}>
      <h1 style={{ color: "#58a6ff", textAlign: "center" }}>
        👻 GhostOps Dashboard
      </h1>
      <p style={{ color: "#8b949e", textAlign: "center" }}>
        Real-time Infrastructure Monitor
      </p>
      <div style={{ display: "flex", justifyContent: "center", gap: "20px", marginTop: "40px", flexWrap: "wrap" }}>
        {SERVICES.map((service) => (
          <div key={service.name} style={{
            background: "#161b22",
            border: `2px solid ${statuses[service.name] === "HEALTHY" ? "#3fb950" : "#f85149"}`,
            borderRadius: "10px",
            padding: "30px",
            width: "200px",
            textAlign: "center"
          }}>
            <h2 style={{ color: "white", fontSize: "16px" }}>{service.name}</h2>
            <p style={{
              color: statuses[service.name] === "HEALTHY" ? "#3fb950" : "#f85149",
              fontSize: "20px",
              fontWeight: "bold"
            }}>
              {statuses[service.name] === "HEALTHY" ? "✅ HEALTHY" : "❌ DOWN"}
            </p>
            <p style={{ color: "#8b949e", fontSize: "12px" }}>Port: {service.port}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;