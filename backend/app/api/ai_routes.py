from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.categorizer import predict_category

router = APIRouter(prefix="/ai", tags=["AI"])

class TextInput(BaseModel):
    description: str

@router.post("/categorize")
def categorize_expense(data: TextInput):
    category = predict_category(data.description)
    return {
        "description": data.description,
        "predicted_category": category
    }
