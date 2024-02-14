from fastapi import HTTPException
from src.services.book_service import BookService

def create_book(name: str, author: str, category: str, resume: str, image: str):
    try:
        response = BookService.create_book(name, author, category, resume, image)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_book(book_id: int, name: str, author: str, category: str, resume: str, image: str):
    try:
        response = BookService.update_book(book_id, name, author, category, resume, image)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_book(book_id: int):
    try:
        response = BookService.delete_book(book_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_all_books():
    try:
        response = BookService.get_all_books()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_book_by_id(book_id: int):
    try:
        response = BookService.get_book_by_id(book_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))