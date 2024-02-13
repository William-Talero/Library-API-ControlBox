"""LIBRARY ROUTER"""

# FastAPI
from fastapi import APIRouter

# Controllers
from src.api.controllers.library import get_message, create_database, create_user, update_user, delete_user, get_all_users

router = APIRouter()


@router.get("/")
def library_route():
    return get_message()

@router.post("/create-database")
def create_database_route():
    return create_database()

@router.post("/create-user")
def create_user_route(username: str, email: str, password: str):
    return create_user(username, email, password)

@router.put("/update-user")
def update_user_route(user_id: int, username: str, email: str, password: str):
    return update_user(user_id, username, email, password)

@router.delete("/delete-user")
def delete_user_route(user_id: int):
    return delete_user(user_id)

@router.get("/get-all-users")
def get_all_users_route(): 
    return get_all_users()