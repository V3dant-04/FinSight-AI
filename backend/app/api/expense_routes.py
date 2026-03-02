from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.schemas.expense import ExpenseCreate, ExpenseRead
from app.services.expense_service import create_expense, get_all_expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ExpenseRead)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense)


@router.get("/", response_model=List[ExpenseRead])
def list_expenses(db: Session = Depends(get_db)):
    return get_all_expenses(db)