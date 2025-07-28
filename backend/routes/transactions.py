from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models.transaction import Transaction
from models.currency import Currency
from models.category import Category
from datetime import datetime
from pydantic import BaseModel
# Pydantic schema for validation
from typing import List

# Create a new transaction (POST)
from sqlalchemy.future import select

router = APIRouter()

class TransactionCreate(BaseModel):
    amount: float
    description: str
    date: datetime
    currency_id: int
    category_ids: List[int]

class TransactionOut(BaseModel):
    id: int
    amount: float
    description: str
    date: datetime
    currency_id: int
    categories: List[str]

    class Config:
        from_attributes = True

class TransactionsCreate(BaseModel):
    transactions: List[TransactionCreate]


# List all transactions (GET)
@router.get("/", response_model=list[TransactionOut])
async def list_transactions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Transaction).where(Transaction.is_deleted == False))
    transactions = result.scalars().all()
    return [
        TransactionOut(
            id=tx.id,
            amount=tx.amount,
            description=tx.description,
            date=tx.date,
            currency_id=tx.currency_id,
            categories=[cat.name for cat in tx.category]
        )
        for tx in transactions
    ]

@router.post("/", response_model=TransactionOut)
async def create_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    # Validate currency (optional, but recommended)
    currency = await db.get(Currency, transaction.currency_id)
    if not currency:
        raise HTTPException(status_code=400, detail="Currency not found")

    # Fetch categories
    result = await db.execute(select(Category).where(Category.id.in_(transaction.category_ids)))
    categories = result.scalars().all()
    if len(categories) != len(transaction.category_ids):
        raise HTTPException(status_code=400, detail="One or more categories not found")

    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date,
        currency_id=transaction.currency_id,
        category=categories
    )
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return TransactionOut(
        id=db_transaction.id,
        amount=db_transaction.amount,
        description=db_transaction.description,
        date=db_transaction.date,
        currency_id=db_transaction.currency_id,
        categories=[cat.name for cat in db_transaction.category]
    )

# Update a transaction (PUT)
@router.put("/{transaction_id}", response_model=TransactionOut)
async def update_transaction(transaction_id: int, transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    db_transaction = await db.get(Transaction, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db_transaction.amount = transaction.amount
    db_transaction.description = transaction.description
    db_transaction.date = transaction.date
    db_transaction.currency_id = transaction.currency_id

    # Update categories
    result = await db.execute(select(Category).where(Category.id.in_(transaction.category_ids)))
    categories = result.scalars().all()
    if len(categories) != len(transaction.category_ids):
        raise HTTPException(status_code=400, detail="One or more categories not found")
    db_transaction.category = categories

    await db.commit()
    await db.refresh(db_transaction)
    return TransactionOut(
        id=db_transaction.id,
        amount=db_transaction.amount,
        description=db_transaction.description,
        date=db_transaction.date,
        currency_id=db_transaction.currency_id,
        categories=[cat.name for cat in db_transaction.category]
    )

# Soft delete a transaction (DELETE)
@router.delete("/{transaction_id}", status_code=204)
async def delete_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        db_transaction = await db.get(Transaction, transaction_id)
        if db_transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        db_transaction.is_deleted = True
        await db.commit()
        await db.refresh(db_transaction)
    return None

# Create multiple transactions (POST)
@router.post("/bulk", response_model=list[TransactionOut])
async def create_transactions_bulk(transactions_data: TransactionsCreate, db: AsyncSession = Depends(get_db)):
    db_transactions = []
    for tx in transactions_data.transactions:
        result = await db.execute(select(Category).where(Category.id.in_(tx.category_ids)))
        categories = result.scalars().all()
        if len(categories) != len(tx.category_ids):
            raise HTTPException(status_code=400, detail="One or more categories not found")
        db_transaction = Transaction(
            amount=tx.amount,
            description=tx.description,
            date=tx.date,
            currency_id=tx.currency_id,
            category=categories
        )
        db.add(db_transaction)
        db_transactions.append(db_transaction)
    await db.commit()
    for db_transaction in db_transactions:
        await db.refresh(db_transaction)
    return [
        TransactionOut(
            id=db_transaction.id,
            amount=db_transaction.amount,
            description=db_transaction.description,
            date=db_transaction.date,
            currency_id=db_transaction.currency_id,
            categories=[cat.name for cat in db_transaction.category]
        )
        for db_transaction in db_transactions
    ]
