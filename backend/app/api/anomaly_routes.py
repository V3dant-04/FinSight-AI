from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.anomaly import detect_anomalies

router = APIRouter(prefix="/ai", tags=["AI"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/anomalies")
def get_spending_anomalies(db: Session = Depends(get_db)):
    expenses = db.query(Expense).order_by(Expense.date).all()
    amounts = [e.amount for e in expenses]

    anomalies = detect_anomalies(amounts)
    return {
        "total_records": len(amounts),
        "anomalies": anomalies
    }
