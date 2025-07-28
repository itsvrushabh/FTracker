import pytest
from datetime import datetime
import io

@pytest.mark.asyncio
async def test_import_csv(client, async_client):
    # Prepare sample CSV data
    csv_content = (
        "amount,description,date\n"
        "100.5,Groceries,2024-06-01T10:00:00\n"
        "250.0,Rent,2024-06-02T09:00:00\n"
    )
    files = {"file": ("sample.csv", csv_content, "text/csv")}

    # Use synchronous client for file upload
    response = client.post("/api/data/import", files=files)
    assert response.status_code == 200
    assert response.json()["message"] == "Data imported successfully"

    # Verify transactions imported
    get_resp = await async_client.get("/api/transactions/")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert any(tx["description"] == "Groceries" for tx in data)
    assert any(tx["description"] == "Rent" for tx in data)

@pytest.mark.asyncio
async def test_export_csv(async_client):
    # First, import sample data
    csv_content = (
        "amount,description,date\n"
        "100.5,Groceries,2024-06-01T10:00:00\n"
        "250.0,Rent,2024-06-02T09:00:00\n"
    )
    files = {"file": ("sample.csv", csv_content, "text/csv")}
    # Use synchronous client for file upload
    # The async_client can't do file upload, so we use the sync client fixture
    # This test assumes test_import_csv ran before, but we re-import for isolation
    # pytest runs tests independently, so we need to import again
    from fastapi.testclient import TestClient
    from backend.main import app as fastapi_app
    with TestClient(fastapi_app) as sync_client:
        sync_client.post("/api/data/import", files=files)

    # Export CSV
    response = await async_client.get("/api/data/export")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    content = response.text
    assert "Groceries" in content
    assert "Rent" in content
    assert "amount,description,date" in content
