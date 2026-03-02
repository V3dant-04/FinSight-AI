from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.budget_agent import check_budget

router = APIRouter(prefix="/ai", tags=["AI"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/budget-check")
def budget_check(budget_limit: float, db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return check_budget(expenses, budget_limit)
