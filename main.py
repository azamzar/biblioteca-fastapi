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
    return {"message": "Bienvenido/a a esta API de libros!"}

#OBTENER UN LIBRO

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if 0 <= book_id < len(books_db):
        return books_db[book_id]
    return {"error": "Book not found"}

#LISTAR LIBROS

@app.get("/books/")
def list_books():
    return books_db

#INTRODUCIR UN LIBRO

@app.post("/books/")
def create_book(book: Book):
    books_db.append(book)
    return {"message": f"Book '{book.title}' created successfully", "book_id": len(books_db) - 1}

#ACTUALIZAR LIBRO

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if 0 <= book_id < len(books_db):
        books_db[book_id] = book
        return {"message": f"Book '{book.title}' updated successfully"}
    return {"error": "Book not found"}

#BORRAR LIBRO

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if 0 <= book_id < len(books_db):
        deleted_book = books_db.pop(book_id)
        return {"message": f"Book '{deleted_book.title}' deleted successfully"}
    return {"error": "Book not found"}