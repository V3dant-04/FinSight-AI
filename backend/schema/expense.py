from pydantic import BaseModel
from datetime import datetime

class ExpenseBase(BaseModel):
    amount: float
    category: str
    description: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseRead(ExpenseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True