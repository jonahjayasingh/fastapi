from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[int]
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

class BookUpdate(BaseModel):
    title: Optional[str] 
    author: Optional[str] 
    publisher: Optional[str] 
    page_count: Optional[int] 
    language: Optional[str] 