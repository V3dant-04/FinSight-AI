from app.core.database import engine, Base
from app.models import expense

Base.metadata.create_all(bind=engine)
