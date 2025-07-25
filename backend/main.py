import uvicorn
from fastapi import FastAPI
from routes import data, goals, transactions

app = FastAPI()

# Register the transactions router
app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
# Register the data router
app.include_router(data.router, prefix="/api/data", tags=["data"])
# Register the goals router
app.include_router(goals.router, prefix="/api/goals", tags=["goals"])

if __name__ == "__main__":
    from database import create_tables
    print("Creating database tables...")
    import asyncio
    asyncio.run(create_tables())
    print("Database tables created.")
    # uvicorn.run(app, host="0.0.0.0", port=8000)
