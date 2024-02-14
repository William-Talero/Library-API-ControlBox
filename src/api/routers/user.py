"""USER ROUTER"""

# FastAPI
from fastapi import APIRouter

# Controllers
from src.api.controllers.user import get_message, create_user, update_user, delete_user, get_all_users, validate_user, get_user_by_id

router = APIRouter()


@router.get("/")
def library_route():
    return get_message()

@router.post("/create-user")
def create_user_route(username: str, fullname: str, email: str, password: str):
    return create_user(username, fullname, email, password)

@router.put("/update-user")
def update_user_route(user_id: int, username: str, fullname: str, email: str, password: str):
    return update_user(user_id, username, fullname, email, password)

@router.delete("/delete-user")
def delete_user_route(user_id: int):
    return delete_user(user_id)

@router.get("/get-all-users")
def get_all_users_route(): 
    return get_all_users()

@router.get("/get-user-by-id")
def get_user_by_id_route(user_id: int):
    return get_user_by_id(user_id)

@router.get("/validate-user")
def validate_user_route(username: str, password: str):
    return validate_user(username, password)