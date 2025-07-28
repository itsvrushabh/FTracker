import pytest
from datetime import datetime

# All DB setup and client fixtures are now provided by conftest.py

@pytest.mark.asyncio
async def test_create_transaction(async_client):
    payload = {
        "amount": 100.5,
        "description": "Test transaction",
        "date": datetime.utcnow().isoformat()
    }
    response = await async_client.post("/api/transactions/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == payload["amount"]
    assert data["description"] == payload["description"]
    assert "id" in data

@pytest.mark.asyncio
async def test_list_transactions(async_client):
    # Create a transaction first
    payload = {
        "amount": 50.0,
        "description": "List test",
        "date": datetime.utcnow().isoformat()
    }
    await async_client.post("/api/transactions/", json=payload)
    response = await async_client.get("/api/transactions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(tx["description"] == "List test" for tx in data)

@pytest.mark.asyncio
async def test_update_transaction(async_client):
    # Create a transaction
    payload = {
        "amount": 75.0,
        "description": "Update test",
        "date": datetime.utcnow().isoformat()
    }
    create_resp = await async_client.post("/api/transactions/", json=payload)
    tx_id = create_resp.json()["id"]

    # Update it
    update_payload = {
        "amount": 80.0,
        "description": "Updated description",
        "date": datetime.utcnow().isoformat()
    }
    response = await async_client.put(f"/api/transactions/{tx_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == update_payload["amount"]
    assert data["description"] == update_payload["description"]

@pytest.mark.asyncio
async def test_delete_transaction(async_client):
    # Create a transaction
    payload = {
        "amount": 120.0,
        "description": "Delete test",
        "date": datetime.utcnow().isoformat()
    }
    create_resp = await async_client.post("/api/transactions/", json=payload)
    tx_id = create_resp.json()["id"]

    # Delete it
    response = await async_client.delete(f"/api/transactions/{tx_id}")
    assert response.status_code == 204

    # Try to get it again
    list_resp = await async_client.get("/api/transactions/")
    data = list_resp.json()
    assert not any(tx["id"] == tx_id for tx in data)

@pytest.mark.asyncio
async def test_update_nonexistent_transaction(async_client):
    update_payload = {
        "amount": 999.0,
        "description": "Nonexistent",
        "date": datetime.utcnow().isoformat()
    }
    response = await async_client.put("/api/transactions/9999", json=update_payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Transaction not found"

@pytest.mark.asyncio
async def test_delete_nonexistent_transaction(async_client):
    response = await async_client.delete("/api/transactions/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Transaction not found"
