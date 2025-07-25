from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import SessionLocal
from models.goal import Goal  # Assuming you have a Goal model

router = APIRouter()

# Pydantic schema for goal validation
class GoalCreate(BaseModel):
    goal: str
    target_date: datetime

class GoalOut(BaseModel):
    id: int
    goal: str
    target_date: datetime

    class Config:
        orm_mode = True

# Get all goals
@router.get("/", response_model=list[GoalOut])
async def get_goals(db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(Goal))
        goals = result.scalars().all()
    return goals

# Create a goal
@router.post("/", response_model=GoalOut)
async def create_goal(goal: GoalCreate, db: AsyncSession = Depends(get_db)):
    db_goal = Goal(goal=goal.goal, target_date=goal.target_date)
    db.add(db_goal)
    await db.commit()
    await db.refresh(db_goal)
    return db_goal
