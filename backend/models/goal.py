from sqlalchemy import Column, Integer, String, Date
from models import Base
#Create a Goal model
class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    due_date = Column(Date)
    status = Column(String, default="pending")

    def __repr__(self):
        return f"<Goal(id={self.id}, title='{self.title}', description='{self.description}', due_date='{self.due_date}', status='{self.status}')>"
