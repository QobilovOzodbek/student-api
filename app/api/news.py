from fastapi import APIRouter
from app.services.scraper import get_news

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/")
def news():
    return {"news": get_news()}