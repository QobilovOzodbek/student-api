from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/feedback", tags=["Feedback"])

class Feedback(BaseModel):
    text: str
    anonymous: bool = False

@router.post("/")
def send_feedback(feedback: Feedback):
    return {
        "message": "Fikr qabul qilindi ✅",
        "data": feedback
    }