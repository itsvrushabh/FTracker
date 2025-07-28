import React from "react";

const HomePage = () => {
  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "2rem" }}>
      <h1>FTracker – Personal Budget & Financial Goals Tracker</h1>
      <p>Welcome to your finance dashboard!</p>
      <section style={{ marginBottom: 40 }}>
        <h2>Transactions Bubble Chart (by Category)</h2>
        <div
          style={{
            width: "100%",
            height: 300,
            background: "#e3f2fd",
            borderRadius: 12,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#1976d2",
            fontSize: 22,
            marginBottom: 10,
          }}
        >
          [Bubble Chart Placeholder]
        </div>
        <p style={{ textAlign: "center", color: "#555" }}>
          Each bubble represents a category. Size = total spent.
        </p>
      </section>
      <section>
        <h2>Income vs Expense Bar Chart</h2>
        <div
          style={{
            width: "100%",
            height: 200,
            background: "#fff3e0",
            borderRadius: 12,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#e65100",
            fontSize: 22,
            marginBottom: 10,
          }}
        >
          [Bar Chart Placeholder]
        </div>
        <p style={{ textAlign: "center", color: "#555" }}>
          Compare your income and expenses visually.
        </p>
      </section>
    </div>
  );
};

export default HomePage;
