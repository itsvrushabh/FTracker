from fastapi import FastAPI
from routes import transactions

app = FastAPI()

# Register the transactions router
app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
