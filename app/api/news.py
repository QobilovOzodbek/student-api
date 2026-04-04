from fastapi import APIRouter
from app.services.scraper import get_news, get_news_detail

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/")
def news():
    return get_news()


@router.get("/detail")
def news_detail(url: str):
    return get_news_detail(url)