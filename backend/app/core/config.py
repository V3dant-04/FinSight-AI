import os
from pydantic import BaseSettings
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
class Settings(BaseSettings):
    APP_NAME: str = "FinSight AI"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY", "")
    ALERT_FROM_EMAIL: str = os.getenv("ALERT_FROM_EMAIL", "")
    ALERT_TO_EMAIL: str = os.getenv("ALERT_TO_EMAIL", "")

settings = Settings()
