import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TransactionsPage from "./pages/TransactionsPage";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <nav
          style={{
            background: "#1976d2",
            padding: "1rem",
            marginBottom: "2rem",
            display: "flex",
            gap: "2rem",
          }}
        >
          <Link
            to="/"
            style={{
              color: "#fff",
              textDecoration: "none",
              fontWeight: "bold",
            }}
          >
            Home
          </Link>
          <Link
            to="/transactions"
            style={{
              color: "#fff",
              textDecoration: "none",
              fontWeight: "bold",
            }}
          >
            Transactions
          </Link>
        </nav>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/transactions" element={<TransactionsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
