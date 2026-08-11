from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "pages/index.html", {"title": "Dashboard"})


@router.get("/books", response_class=HTMLResponse)
def books_page(request: Request):
    return templates.TemplateResponse(request, "pages/books.html", {"title": "Bücher"})


@router.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    return templates.TemplateResponse(request, "pages/profile.html", {"title": "Profil"})
