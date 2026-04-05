from fastapi import APIRouter
from app.services.management_scraper import get_all_management_async

router = APIRouter(prefix="/management", tags=["Management"])


@router.get("/")
async def get_management():
    return await get_all_management_async()