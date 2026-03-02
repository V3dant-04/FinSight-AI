from app.ai.budget_agent import check_budget
from app.alerts.emailer import send_email

def run_budget_alert(expenses, budget_limit):
    result = check_budget(expenses, budget_limit)

    if result["status"] in ["warning", "exceeded"]:
        send_email(
            subject="⚠️ FinSight AI Budget Alert",
            content=result["message"]
        )

    return result
