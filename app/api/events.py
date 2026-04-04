from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def events():
    return {
        "events": [
            {"name": "IT konferensiya", "date": "2026-05-01"},
            {"name": "Hackathon", "date": "2026-06-10"}
        ]
    }