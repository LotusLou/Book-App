from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from datetime import date

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    progress_entries = relationship("Progress", back_populates="user")
    books = relationship("Book", backpopulates= "user")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)
    total_pages = Column(Integer, nullable=False)
    genre = Column(String, nullable= True)
    status = Column(String, nullable= False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)

    user = relationship("User", back_populates= "books")
    progress_entries = relationship("Progress", back_populates="book")

    current_page = Column(Integer, default=0)
    rating = Column(Integer, nullable=True)
    cover_url = Column(String, nullable=True)
    isbn = Column(String, nullable=True)

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    pages_read = Column (Integer, default= 0)
    entry_date = Column (Date, default= date.today)

    user = relationship("User", back_populates="progress_entries")
    book = relationship("Book", back_populates="progress_entries")
