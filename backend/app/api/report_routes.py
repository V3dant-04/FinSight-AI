from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.insights import generate_insights
from app.ai.forecast import forecast_next
from app.report.summary import build_report

router = APIRouter(prefix="/report", tags=["Report"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def generate_summary_report(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    insights = generate_insights(expenses)
    forecast = forecast_next([e.amount for e in expenses])

    report = build_report(expenses, insights, forecast)
    return report
