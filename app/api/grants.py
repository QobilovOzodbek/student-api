from fastapi import APIRouter
from app.services.grants_scraper import get_grants_data

router = APIRouter(prefix="/grants", tags=["Grants & Stipendiya"])


@router.get("/")
async def get_grants():
    return await get_grants_data()