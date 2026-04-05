from fastapi import APIRouter
from app.services.management_scraper import (
    get_all_management,
    parse_management_page
)

router = APIRouter(prefix="/management", tags=["Management"])


@router.get("/")
def get_management():
    return get_all_management()


@router.get("/detail")
def get_one(url: str):
    return parse_management_page(url)