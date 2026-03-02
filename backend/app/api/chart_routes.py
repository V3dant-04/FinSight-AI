from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.report.charts import category_chart_data, time_series_data

router = APIRouter(prefix="/charts", tags=["Charts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/overview")
def charts_overview(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()

    return {
        "category_chart": category_chart_data(expenses),
        "time_series": time_series_data(expenses)
    }
