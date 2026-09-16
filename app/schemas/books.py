from pydantic import BaseModel
from typing import Optional

class BookBase (BaseModel):
    title: str
    author: Optional[str] = "Unbekannter Autor"
    total_pages: int
    cover_url: Optional[str] = None
    isbn: Optional[str] = None
    status: str = "wishlist"  # z. B. "wishlist", "reading", "completed"

class BookCreate (BookBase):
    pass 

class BookUpdate (BaseModel):
    current_page: Optional[int] = None
    status: Optional[int] = None
    rating: Optional[int] = None

class BookResponse(BookBase):
    id: int
    current_page: int = 0
    rating: Optional[int] = None
    user_id: int

    class Config:
        from_attributes = True  # Erlaubt die Konvertierung von SQLAlchemy-Objekten zu Pydantic