from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# Database URL for PostgreSQL (modify this if you're using another DB)
DATABASE_URL = "postgresql+asyncpg://username:password@localhost/dbname"

# Async database connection (SQLAlchemy)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Session factory for async sessions
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Get async session for dependency injection
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
