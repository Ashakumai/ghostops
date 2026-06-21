import { useState, useEffect } from "react";

const SERVICES = [
  { name: "Ecommerce API", port: 8000, icon: "🛒" },
  { name: "Payment Gateway", port: 8001, icon: "💳" },
  { name: "Auth Service", port: 8002, icon: "🔐" },
];

function App() {
  const [statuses, setStatuses] = useState({});
  const [lastUpdated, setLastUpdated] = useState("");

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
    setLastUpdated(new Date().toLocaleTimeString());
  };

  useEffect(() => {
    checkServices();
    const interval = setInterval(checkServices, 10000);
    return () => clearInterval(interval);
  }, []);

  const healthyCount = Object.values(statuses).filter(s => s === "HEALTHY").length;

  return (
    <div style={{
      background: "#0a0e1a",
      minHeight: "100vh",
      padding: "30px",
      fontFamily: "'Segoe UI', sans-serif",
      color: "white"
    }}>
      {/* Header */}
      <div style={{
        borderBottom: "1px solid #1e2d4a",
        paddingBottom: "20px",
        marginBottom: "30px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <div>
          <h1 style={{ margin: 0, fontSize: "24px", color: "#4d9fff" }}>
            👻 GhostOps
          </h1>
          <p style={{ margin: "5px 0 0", color: "#5a7a9a", fontSize: "13px" }}>
            Autonomous AI SRE Platform
          </p>
        </div>
        <div style={{
          background: "#0d1f35",
          padding: "8px 16px",
          borderRadius: "20px",
          fontSize: "12px",
          color: "#5a7a9a"
        }}>
          🕐 Last updated: {lastUpdated}
        </div>
      </div>

      {/* Stats Bar */}
      <div style={{
        display: "flex",
        gap: "15px",
        marginBottom: "30px"
      }}>
        <div style={{
          background: "#0d1f35",
          border: "1px solid #1e2d4a",
          borderRadius: "10px",
          padding: "15px 25px",
          flex: 1,
          textAlign: "center"
        }}>
          <p style={{ margin: 0, color: "#5a7a9a", fontSize: "12px" }}>TOTAL SERVICES</p>
          <h2 style={{ margin: "5px 0 0", color: "white", fontSize: "28px" }}>{SERVICES.length}</h2>
        </div>
        <div style={{
          background: "#0d1f35",
          border: "1px solid #1e3a2a",
          borderRadius: "10px",
          padding: "15px 25px",
          flex: 1,
          textAlign: "center"
        }}>
          <p style={{ margin: 0, color: "#5a7a9a", fontSize: "12px" }}>HEALTHY</p>
          <h2 style={{ margin: "5px 0 0", color: "#3fb950", fontSize: "28px" }}>{healthyCount}</h2>
        </div>
        <div style={{
          background: "#0d1f35",
          border: "1px solid #3a1e1e",
          borderRadius: "10px",
          padding: "15px 25px",
          flex: 1,
          textAlign: "center"
        }}>
          <p style={{ margin: 0, color: "#5a7a9a", fontSize: "12px" }}>DOWN</p>
          <h2 style={{ margin: "5px 0 0", color: "#f85149", fontSize: "28px" }}>{SERVICES.length - healthyCount}</h2>
        </div>
      </div>

      {/* Service Cards */}
      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        {SERVICES.map((service) => {
          const isHealthy = statuses[service.name] === "HEALTHY";
          return (
            <div key={service.name} style={{
              background: "#0d1f35",
              border: `1px solid ${isHealthy ? "#1e3a2a" : "#3a1e1e"}`,
              borderRadius: "12px",
              padding: "25px",
              flex: "1",
              minWidth: "200px",
              position: "relative",
              overflow: "hidden"
            }}>
              <div style={{
                position: "absolute",
                top: 0,
                left: 0,
                right: 0,
                height: "3px",
                background: isHealthy ? "#3fb950" : "#f85149"
              }} />
              <div style={{ fontSize: "30px", marginBottom: "10px" }}>{service.icon}</div>
              <h3 style={{ margin: "0 0 5px", fontSize: "16px", color: "white" }}>{service.name}</h3>
              <p style={{ margin: "0 0 15px", color: "#5a7a9a", fontSize: "12px" }}>Port: {service.port}</p>
              <div style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "6px",
                background: isHealthy ? "#1a3a2a" : "#3a1a1a",
                padding: "5px 12px",
                borderRadius: "20px"
              }}>
                <div style={{
                  width: "6px",
                  height: "6px",
                  borderRadius: "50%",
                  background: isHealthy ? "#3fb950" : "#f85149"
                }} />
                <span style={{
                  color: isHealthy ? "#3fb950" : "#f85149",
                  fontSize: "12px",
                  fontWeight: "bold"
                }}>
                  {isHealthy ? "OPERATIONAL" : "INCIDENT"}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;