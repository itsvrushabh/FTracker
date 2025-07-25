from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from models import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    #Currency id to reference the currency associated with the transaction
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, description={self.description}, date={self.date})>"
