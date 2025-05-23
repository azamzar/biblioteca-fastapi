from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None
    pages: int

# Almacén temporal en memoria
books_db: List[Book] = []

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if 0 <= book_id < len(books_db):
        return books_db[book_id]
    return {"error": "Book not found"}

@app.get("/books/")
def list_books():
    return books_db

@app.post("/books/")
def create_book(book: Book):
    books_db.append(book)
    return {"message": f"Book '{book.title}' created successfully", "book_id": len(books_db) - 1}
