from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models.transaction import Transaction
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

# Pydantic schema for validation
class TransactionCreate(BaseModel):
    amount: float
    description: str
    date: datetime
    category_id: int
    currency_id: int

class TransactionOut(BaseModel):
    id: int
    amount: float
    description: str
    date: datetime

    class Config:
        from_attributes = True

class TransactionsCreate(BaseModel):
    transactions: list[TransactionCreate]


# List all transactions (GET)
@router.get("/", response_model=list[TransactionOut])
async def list_transactions(db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(Transaction))
        transactions = result.scalars().all()
    return transactions

# Create a new transaction (POST)
@router.post("/", response_model=TransactionOut)
async def create_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date
    )
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction

# Update a transaction (PUT)
@router.put("/{transaction_id}", response_model=TransactionOut)
async def update_transaction(transaction_id: int, transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        db_transaction = await db.get(Transaction, transaction_id)
        if db_transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        db_transaction.amount = transaction.amount
        db_transaction.description = transaction.description
        db_transaction.date = transaction.date
        db_transaction.category_id = transaction.category_id
        db_transaction.currency_id = transaction.currency_id
        await db.commit()
        await db.refresh(db_transaction)
    return db_transaction

# Soft delete a transaction (DELETE)
@router.delete("/{transaction_id}", status_code=204)
async def delete_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        db_transaction = await db.get(Transaction, transaction_id)
        if db_transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        await db.delete(db_transaction)
        await db.commit()
    return None

# Create multiple transactions (POST)
@router.post("/bulk", response_model=list[TransactionOut])
async def create_transactions_bulk(transactions_data: TransactionsCreate, db: AsyncSession = Depends(get_db)):
    db_transactions = [
        Transaction(
            amount=tx.amount,
            description=tx.description,
            date=tx.date
        )
        for tx in transactions_data.transactions
    ]
    db.add_all(db_transactions)
    await db.commit()
    for db_transaction in db_transactions:
        await db.refresh(db_transaction)
    return db_transactions
