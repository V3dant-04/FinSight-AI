from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware

from app.core.logger import logger
from app.core.limiter import limiter
from app.scheduler.start import start_scheduler
from app.api.health_routes import router as health_router
app.include_router(health_router)
from app.core.request_logger import RequestLoggingMiddleware

app.add_middleware(RequestLoggingMiddleware)
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Create app FIRST
app = FastAPI(title="FinSight AI")
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Attach limiter
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

logger.info("FinSight AI starting up...")

# ---------------- ROUTERS ---------------- #

from app.api.auth_routes import router as auth_router
from app.api.expense_routes import router as expense_router
from app.api.ai_routes import router as ai_router
from app.api.anomaly_routes import router as anomaly_router
from app.api.forecast_routes import router as forecast_router
from app.api.chat_routes import router as chat_router
from app.api.chart_routes import router as chart_router
from app.api.budget_routes import router as budget_router
from app.api.insight_routes import router as insight_router
from app.api.report_routes import router as report_router
from app.api.pdf_routes import router as pdf_router
from app.api.alert_routes import router as alert_router

app.include_router(auth_router)
app.include_router(expense_router)
app.include_router(ai_router)
app.include_router(anomaly_router)
app.include_router(forecast_router)
app.include_router(chat_router)
app.include_router(insight_router)
app.include_router(report_router)
app.include_router(chart_router)
app.include_router(pdf_router)
app.include_router(budget_router)
app.include_router(alert_router)

# ---------------- STARTUP EVENT ---------------- #

@app.on_event("startup")
def startup_event():
    start_scheduler()

# ---------------- ROOT ---------------- #

@app.get("/")
def root():
    return {"status": "FinSight AI backend running"}
