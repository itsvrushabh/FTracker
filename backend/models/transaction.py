from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base

transaction_category = Table(
    "transaction_category",
    Base.metadata,
    Column("transaction_id", Integer, ForeignKey("transactions.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True)
)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    currency = relationship("Currency", back_populates="transactions")
    category = relationship("Category", secondary=transaction_category, back_populates="transactions")
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, description={self.description}, date={self.date})>"
