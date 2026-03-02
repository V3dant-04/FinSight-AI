from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.ai.chatbot import finance_chat

router = APIRouter(prefix="/ai", tags=["AI"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat")
def chat_with_finance(question: str, db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    summary = "\n".join([f"{e.date}: {e.category} - {e.amount}" for e in expenses[:50]])

    answer = finance_chat(summary, question)

    return {"question": question, "answer": answer}
