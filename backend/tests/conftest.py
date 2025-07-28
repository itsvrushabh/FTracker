import os
import pytest
import asyncio

from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from backend.main import app as fastapi_app
from backend.database import get_db
from backend.models import Base

# Use the test database URL
TEST_DATABASE_URL = "postgresql+asyncpg://test-user:password@postgres:15432/test_db"

# Create async engine and sessionmaker for test DB
engine = create_async_engine(TEST_DATABASE_URL, echo=True, future=True)
TestingSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

# Override get_db dependency for all tests
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

fastapi_app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the session."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def setup_test_db():
    """
    Create all tables at the start of the test session and drop them at the end.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def db_session():
    """
    Provide a transactional scope for a test.
    """
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture(scope="function")
async def async_client():
    """
    Provide an HTTPX AsyncClient for FastAPI.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="function")
def client():
    """
    Provide a synchronous TestClient for FastAPI (for file upload/download).
    """
    with TestClient(fastapi_app) as c:
        yield c
