from sqlalchemy.orm import Session
from src.models.books_model import Book
from src.database.database_connection import get_db

class BookService:
    @staticmethod
    def create_book(name: str, author: str, category: str, resume: str, image: str):
        db = next(get_db())
        book = Book(name=name, author=author, category=category, resume=resume, image=image)
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def update_book(book_id: int, name: str, author: str, category: str, resume: str, image: str):
        db = next(get_db())
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None
        book.name = name
        book.author = author
        book.category = category
        book.resume = resume
        book.image = image
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def delete_book(book_id: int):
        db = next(get_db())
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return False
        db.delete(book)
        db.commit()
        return True
    
    @staticmethod
    def get_all_books():
        db = next(get_db())
        books = db.query(Book).all()
        return books
    
    @staticmethod
    def get_book_by_id(book_id: int):
        db = next(get_db())
        book = db.query(Book).filter(Book.id == book_id).first()
        return book