from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.alerts.alert_engine import run_budget_alert

router = APIRouter(prefix="/alerts", tags=["Alerts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/budget")
def trigger_budget_alert(budget_limit: float, db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return run_budget_alert(expenses, budget_limit)
