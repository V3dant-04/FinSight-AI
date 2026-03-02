from app.core.database import SessionLocal
from app.models.expense import Expense
from app.alerts.alert_engine import run_budget_alert

DAILY_BUDGET_LIMIT = 20000  # change later or make dynamic

def daily_budget_job():
    db = SessionLocal()
    try:
        expenses = db.query(Expense).all()
        run_budget_alert(expenses, DAILY_BUDGET_LIMIT)
    finally:
        db.close()
