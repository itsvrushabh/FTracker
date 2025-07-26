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
    print("Creating database tables...")
    print("Database tables created.")
