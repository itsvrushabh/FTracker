from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from models import Base
from models.category import Category, CategoryType
import json


# Database URL for PostgreSQL (modify this if you're using another DB)
DATABASE_URL = "postgresql+asyncpg://dev-user:password@postgres:15432/dev_db"
DATABASE_URL = "postgresql+asyncpg://dev-user:password@localhost:15432/dev_db"
# Async database connection (SQLAlchemy)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Session factory for async sessions
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_tables():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()

async def drop_tables():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

async def dump_static_data():
    async with AsyncSessionLocal() as session:
        for category_type in json.load(open('./database/category_types.json'))['category_types']:
            await session.add(CategoryType(**category_type))
        await session.commit()
        for category in json.load(open('./database/categories.json'))['categories']:
            await session.add(Category(**category))
        await session.commit()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
