from fastapi import APIRouter, Depends, HTTPException, status
from app.services.google_books import search_google_books
from app.crud import crud_book
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.database import get_db  # Passe den Import an deine DB-Session-Funktion an
from app.schemas.books import BookCreate, BookResponse, BookUpdate
router = APIRouter(prefix="/books", tags=["Books"])
CURRENT_USER_ID = 1 

@router.get("/search")
async def search_books(q: str):
    results = await search_google_books(q)
    return results

@router.post("/", response_model= BookResponse, status_code=status.HTTP_201_CREATED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud_book.create_book(db=db, book=book, user_id=CURRENT_USER_ID)

@router.get("/", response_model=List[BookResponse])
def read_user_books(db: Session = Depends(get_db), status: Optional[str] = None ):
    return crud_book.get_users_books(db=db, user_id=CURRENT_USER_ID, status=status)

@router.get("/{book_id}", response_model= BookResponse)
def read_one_book(book_id: int, db:Session = Depends(get_db)):
    book_by_id = crud_book.get_book_by_id(db=db, book_id=book_id)
    if not book_by_id: 
        raise HTTPException(status_code=404, detail="Book not Found")
    return book_by_id

##braucht es keine user id? 
@router.patch("/{book_id}", response_model= BookResponse)
def update_book(book_id: int, book_update: BookUpdate, db: Session= Depends(get_db)):
    update_book = crud_book.update_book(db=db, book_id=book_id, book_update=book_update,)
    if not update_book:
        raise HTTPException(status_code="404", detail="Book not Found")
    return update_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_entry(book_id: int, db: Session= Depends(get_db)):
    sucess = crud_book.delete_book(db=db, book_id=book_id)
    if not sucess:
        raise HTTPException(status_code=404, detail="Book not Found")
    return None