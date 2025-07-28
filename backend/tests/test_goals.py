import pytest
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_create_goal(async_client):
    payload = {
        "goal": "Save for vacation",
        "target_date": (datetime.utcnow() + timedelta(days=180)).isoformat()
    }
    response = await async_client.post("/api/goals/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == payload["goal"]
    assert "id" in data

@pytest.mark.asyncio
async def test_list_goals(async_client):
    # Seed with two goals
    goals = [
        {
            "goal": "Save for vacation",
            "target_date": (datetime.utcnow() + timedelta(days=180)).isoformat()
        },
        {
            "goal": "Emergency fund",
            "target_date": (datetime.utcnow() + timedelta(days=90)).isoformat()
        }
    ]
    for goal in goals:
        await async_client.post("/api/goals/", json=goal)

    response = await async_client.get("/api/goals/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Check that both seeded goals are present
    returned_goals = [g["goal"] for g in data]
    for goal in goals:
        assert goal["goal"] in returned_goals

@pytest.mark.asyncio
async def test_goal_fields(async_client):
    payload = {
        "goal": "Test field validation",
        "target_date": (datetime.utcnow() + timedelta(days=30)).isoformat()
    }
    response = await async_client.post("/api/goals/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "goal" in data
    assert "target_date" in data
