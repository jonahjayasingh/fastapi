from fastapi import status,HTTPException , APIRouter,Depends
from book_data import books
from schemas import Book, BookUpdate
from typing import List
from db import *
from sqlalchemy.orm import Session

book_router = APIRouter()

@book_router.get("")
async def read_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books

@book_router.post("" ,status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book, db:Session = Depends(get_db)):
    new_book = BookModel(
        title = book_data.title,
        author = book_data.author,
        publisher = book_data.publisher,
        page_count = book_data.page_count,
        language = book_data.language
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@book_router.get("/{book_id}" , response_model=Book)
async def read_book(book_id: int, db:Session = Depends(get_db) ):
    book = db.query(BookModel).get(book_id)
    print(book)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    


@book_router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(BookModel).get(book_id)
    if book:
        for key, value in book_data.dict().items():
            print(key, value)
            if value:
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 


@book_router.delete("{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).get(book_id)
    if book:
        db.delete(book)
        db.commit()
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")