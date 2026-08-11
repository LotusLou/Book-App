from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
def stats():
    return {"streak": 0, "xp": 0, "rank": "Beginner"}
