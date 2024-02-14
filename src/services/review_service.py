from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from src.models.reviews_model import Review
from src.models.books_model import Book
from src.database.database_connection import get_db
from datetime import date

class ReviewService:
    @staticmethod
    def create_review(starts: int, review_text: str, date: date, book_id: int, user_id: int):
        db = next(get_db())
        review = Review(starts=starts, review=review_text, date=date, book_id=book_id, user_id=user_id)
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def update_review(review_id: int, starts: int, review_text: str, date: date):
        db = next(get_db())
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            return None
        review.starts = starts
        review.review = review_text
        review.date = date
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def delete_review(review_id: int):
        db = next(get_db())
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            return False
        db.delete(review)
        db.commit()
        return True
    
    @staticmethod
    def get_all_reviews():
        db = next(get_db())
        reviews = db.query(Review).all()
        return reviews
    
    @staticmethod
    def get_review_by_id(review_id: int):
        db = next(get_db())
        review = db.query(Review).options(joinedload(Review.book)).options(joinedload(Review.user)).filter(Review.id == review_id).first()
        return review
    
    @staticmethod
    def get_reviews_by_book(book_id: int):
        db = next(get_db())
        reviews = db.query(Review).options(joinedload(Review.book)).options(joinedload(Review.user)).filter(Review.book_id == book_id).all()
        return reviews
    
    @staticmethod
    def get_reviews_by_user(user_id: int):
        db = next(get_db())
        reviews = db.query(Review).options(joinedload(Review.book)).options(joinedload(Review.user)).filter(Review.user_id == user_id).all()
        return reviews