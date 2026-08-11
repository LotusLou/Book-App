from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import books, gamification, pages

app = FastAPI(title="Book App")
app.include_router(pages.router)
app.include_router(books.router, prefix="/api/books", tags=["books"])
app.include_router(gamification.router, prefix="/api/gamification", tags=["gamification"])
app.mount("/static", StaticFiles(directory="static"), name="static")
