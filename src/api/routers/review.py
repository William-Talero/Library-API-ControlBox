"""BOOK ROUTER"""

# FastAPI
from fastapi import APIRouter
from datetime import datetime

# Controllers
from src.api.controllers.review import create_review, update_review, delete_review, get_all_reviews, get_review_by_id, get_reviews_by_book, get_reviews_by_user

router = APIRouter()

@router.post("/create-review")
def create_review_route(starts: int, review_text: str, date: str, book_id: int, user_id: int):
    date_obj = datetime.strptime(date, "%d/%m/%Y").date()
    return create_review(starts, review_text, date_obj, book_id, user_id)

@router.put("/update-review")
def update_review_route(review_id: int, starts: int, review_text: str, date: str):
    date_obj = datetime.strptime(date, "%d/%m/%Y").date()
    return update_review(review_id, starts, review_text, date_obj)

@router.delete("/delete-review")
def delete_review_route(review_id: int):
    return delete_review(review_id)

@router.get("/get-all-reviews")
def get_all_reviews_route():
    return get_all_reviews()

@router.get("/get-review-by-id")
def get_review_by_id_route(review_id: int):
    return get_review_by_id(review_id)

@router.get("/get-reviews-by-book")
def get_reviews_by_book_route(book_id: int):
    return get_reviews_by_book(book_id)

@router.get("/get-reviews-by-user")
def get_reviews_by_user_route(user_id: int):
    return get_reviews_by_user(user_id)