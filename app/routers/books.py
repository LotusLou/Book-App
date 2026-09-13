from fastapi import APIRouter
from app.services.google_books import search_google_books
router = APIRouter()


@router.get("/search")
async def search_books(q: str):
    results = await search_google_books(q)
    return results
