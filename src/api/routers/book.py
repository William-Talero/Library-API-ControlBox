"""BOOK ROUTER"""

# FastAPI
from fastapi import APIRouter

# Controllers
from src.api.controllers.book import create_book, update_book, delete_book, get_all_books, get_book_by_id

router = APIRouter()

@router.post("/create-book")
def create_book_route(name: str, author: str, category: str, resume: str, image: str):
    return create_book(name, author, category, resume, image)

@router.put("/update-book")
def update_book_route(book_id: int, name: str, author: str, category: str, resume: str, image: str):
    return update_book(book_id, name, author, category, resume, image)

@router.delete("/delete-book")
def delete_book_route(book_id: int):
    return delete_book(book_id)

@router.get("/get-all-books")
def get_all_books_route():
    return get_all_books()

@router.get("/get-book-by-id")
def get_book_by_id_route(book_id: int):
    return get_book_by_id(book_id)
