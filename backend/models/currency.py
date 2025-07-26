from sqlalchemy import Column, Integer, String, Boolean

from models import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Currency(id={self.id}, name='{self.name}', code='{self.code}', symbol='{self.symbol}')>"
