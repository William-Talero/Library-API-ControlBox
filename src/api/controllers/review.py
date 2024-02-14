from fastapi import HTTPException
from src.services.review_service import ReviewService
from datetime import date

def create_review(starts: int, review_text: str, date: date, book_id: int, user_id: int):
    try:
        response = ReviewService.create_review(starts, review_text, date, book_id, user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_review(review_id: int, starts: int, review_text: str, date: date):
    try:
        response = ReviewService.update_review(review_id, starts, review_text, date)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_review(review_id: int):
    try:
        response = ReviewService.delete_review(review_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_all_reviews():
    try:
        response = ReviewService.get_all_reviews()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_review_by_id(review_id: int):
    try:
        response = ReviewService.get_review_by_id(review_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_reviews_by_book(book_id: int):
    try:
        response = ReviewService.get_reviews_by_book(book_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_reviews_by_user(user_id: int):
    try:
        response = ReviewService.get_reviews_by_user(user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
