from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.insights import generate_insights
from app.ai.forecast import forecast_next
from app.report.summary import build_report
from app.report.pdf_report import generate_pdf_report

router = APIRouter(prefix="/report", tags=["Report"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pdf")
def download_pdf_report(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    insights = generate_insights(expenses)
    forecast = forecast_next([e.amount for e in expenses])

    report = build_report(expenses, insights, forecast)

    filepath = "monthly_report.pdf"
    generate_pdf_report(filepath, report)

    return FileResponse(filepath, media_type="application/pdf", filename="FinSight_Report.pdf")
