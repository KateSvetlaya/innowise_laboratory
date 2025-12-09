from typing import Optional

from sqlalchemy.orm import Session
from . import models, schemas


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book


def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    book.title = updated_book.title
    book.author = updated_book.author
    if updated_book.year is not None:
        book.year = updated_book.year
    db.commit()
    db.refresh(book)
    return book


def search_books(db: Session, title: Optional[str], author: Optional[str], year: Optional[int]):
    query = db.query(models.Book)
    if title:
        query = query.filter(models.Book.title.contains(title))
    if author:
        query = query.filter(models.Book.author.contains(author))
    if year:
        query = query.filter(models.Book.year == year)
    return query.all()
