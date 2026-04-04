from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chatbot import get_response

router = APIRouter(prefix="/chat", tags=["Chat"])

class Message(BaseModel):
    text: str

@router.post("/")
def chat(message: Message):
    response = get_response(message.text)
    return {"response": response}