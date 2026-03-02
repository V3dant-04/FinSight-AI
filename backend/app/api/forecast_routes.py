from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.forecast import forecast_next

router = APIRouter(prefix="/ai", tags=["AI"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/forecast")
def forecast_spending(db: Session = Depends(get_db)):
    expenses = db.query(Expense).order_by(Expense.date).all()
    amounts = [e.amount for e in expenses]

    prediction = forecast_next(amounts)

    return {
        "next_period_prediction": prediction,
        "method": "moving_average",
        "records_used": len(amounts)
    }
