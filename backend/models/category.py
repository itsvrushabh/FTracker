from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models import Base

class CategoryType(Base):
    __tablename__ = "category_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    type_id = Column(Integer, ForeignKey("category_types.id"))
    is_active = Column(Boolean, default=True)

    type = relationship("CategoryType", back_populates="categories")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}', type_id={self.type_id}, is_active={self.is_active})>"
