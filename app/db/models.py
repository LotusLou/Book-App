from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from datetime import date

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    progress_entries = relationship("Progress", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)
    total_pages = Column(Integer, nullable=False)
    genre = Column(String, nullable= False)

    progress_entries = relationship("Progress", back_populates="book")


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    pages_read = Column (Integer, default= 0)
    entry_date = Column (Date, default= date.today)

    user = relationship("User", back_populates="progress_entries")
    book = relationship("Book", back_populates="progress_entries")
