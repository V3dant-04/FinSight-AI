from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.insights import generate_insights

router = APIRouter(prefix="/ai", tags=["AI"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/insights")
def get_financial_insights(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    insights = generate_insights(expenses)

    return {
        "total_records": len(expenses),
        "insights": insights
    }
