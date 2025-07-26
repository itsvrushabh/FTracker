from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    currency = relationship("Currency", back_populates="transactions")
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, description={self.description}, date={self.date})>"
