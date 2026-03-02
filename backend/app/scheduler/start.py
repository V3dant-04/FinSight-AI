from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduler.jobs import daily_budget_job

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(
        daily_budget_job,
        trigger="interval",
        hours=24,
        id="daily_budget_check",
        replace_existing=True
    )
    scheduler.start()
