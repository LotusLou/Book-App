from sqlalchemy.orm import Session
from app.db.models import Book, User
from app.schemas.books import BookCreate, BookUpdate

def create_book(db: Session, book: BookCreate, user_id: int):
    db_book = Book(**book.model_dump(), user_id=user_id)

    db.add(db_book)
    db.commit()
    db.refresh()
    return db_book

def get_book_by_id(db: Session, book_id : int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_users_books(db: Session, user_id: int, status: str == None):
    query = db.query(Book).filter(Book.user_id == user_id)
    if status:
        query = query.filter(Book.status == status)
    return query.all()
##warum keine User id?? 
def update_book(db: Session, book_id :int, book_update: BookUpdate):
    db_book = get_book_by_id(db, book_id)
    if not db_book: 
        return None

    update_data = book_update.model_dump(exclude_unset= True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh()
    return (db_book)

def delete_book(db:Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True