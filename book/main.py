from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Art of Computer Programming",
        "author": "Donald E. Knuth",
        "publisher": "Addison-Wesley",
        "page_count": 3904,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Programming Language Concepts (3rd Edition)",
        "author": "Carlo Ghezzi, Mehdi Jazayeri",
        "publisher": "Wiley",
        "page_count": 448,
        "language": "English"
    },
    {
        "id": 3,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publisher": "Addison-Wesley",
        "page_count": 320,
        "language": "English"
    },
    {
        "id": 4,
        "title": "The Go Programming Language",
        "author": "Alan A. A. Donovan, Brian W. Kernighan",
        "publisher": "Pearson Education",
        "page_count": 400,
        "language": "English"
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

class BookUpdate(BaseModel):
    title: str  
    author: str
    publisher: str
    page_count: int
    language: str


@app.get("/books" , response_model  =List[Book])
async def read_books():
    return books

@app.post("/books" ,status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)  
    return new_book


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book doesn't exist")

