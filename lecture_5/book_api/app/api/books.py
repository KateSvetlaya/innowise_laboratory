from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..schemas import BookCreate, BookResponse
from .. import crud

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/", response_model=List[BookResponse])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@router.delete("/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"detail": "Книга удалена"}

@router.put("/{book_id}", response_model=BookResponse)
def update_book_endpoint(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.get("/search/", response_model=List[BookResponse])
def search_books_endpoint(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return crud.search_books(db, title, author, year)