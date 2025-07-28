import React, { useState } from "react";

// Mock transaction data
const initialTransactions = [
  {
    id: "1",
    amount: 1200,
    type: "Income",
    category: "Salary",
    date: "2024-06-01",
    note: "June Salary",
    is_active: true,
  },
  {
    id: "2",
    amount: 150,
    type: "Expense",
    category: "Groceries",
    date: "2024-06-03",
    note: "Weekly groceries",
    is_active: true,
  },
  {
    id: "3",
    amount: 80,
    type: "Expense",
    category: "Transport",
    date: "2024-06-04",
    note: "Bus pass",
    is_active: true,
  },
];

function TransactionsPage() {
  const [transactions, setTransactions] = useState(initialTransactions);
  const [editingId, setEditingId] = useState(null);
  const [editForm, setEditForm] = useState({
    amount: "",
    type: "",
    category: "",
    date: "",
    note: "",
  });

  const startEdit = (txn) => {
    setEditingId(txn.id);
    setEditForm({
      amount: txn.amount,
      type: txn.type,
      category: txn.category,
      date: txn.date,
      note: txn.note,
    });
  };

  const cancelEdit = () => {
    setEditingId(null);
    setEditForm({
      amount: "",
      type: "",
      category: "",
      date: "",
      note: "",
    });
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setEditForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const saveEdit = () => {
    setTransactions((prev) =>
      prev.map((txn) =>
        txn.id === editingId
          ? { ...txn, ...editForm }
          : txn
      )
    );
    cancelEdit();
  };

  return (
    <div style={{ maxWidth: 800, margin: "0 auto" }}>
      <h2>Transactions</h2>
      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginBottom: "2rem",
        }}
      >
        <thead>
          <tr style={{ background: "#e3f2fd" }}>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Date</th>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Type</th>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Category</th>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Amount</th>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Note</th>
            <th style={{ padding: "8px", border: "1px solid #bbb" }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((txn) =>
            editingId === txn.id ? (
              <tr key={txn.id} style={{ background: "#fffde7" }}>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <input
                    type="date"
                    name="date"
                    value={editForm.date}
                    onChange={handleEditChange}
                  />
                </td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <select
                    name="type"
                    value={editForm.type}
                    onChange={handleEditChange}
                  >
                    <option value="Income">Income</option>
                    <option value="Expense">Expense</option>
                  </select>
                </td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <input
                    type="text"
                    name="category"
                    value={editForm.category}
                    onChange={handleEditChange}
                  />
                </td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <input
                    type="number"
                    name="amount"
                    value={editForm.amount}
                    onChange={handleEditChange}
                  />
                </td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <input
                    type="text"
                    name="note"
                    value={editForm.note}
                    onChange={handleEditChange}
                  />
                </td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <button onClick={saveEdit} style={{ marginRight: 8 }}>
                    Save
                  </button>
                  <button onClick={cancelEdit}>Cancel</button>
                </td>
              </tr>
            ) : (
              <tr key={txn.id}>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>{txn.date}</td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>{txn.type}</td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>{txn.category}</td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>{txn.amount}</td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>{txn.note}</td>
                <td style={{ padding: "8px", border: "1px solid #bbb" }}>
                  <button onClick={() => startEdit(txn)}>Edit</button>
                </td>
              </tr>
            )
          )}
        </tbody>
      </table>
      <p style={{ color: "#555" }}>
        <strong>Tip:</strong> Click "Edit" to update a transaction. Changes are saved locally.
      </p>
    </div>
  );
}

export default TransactionsPage;
