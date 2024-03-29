from fastapi import HTTPException
from src.services.user_service import UserService

def get_message():
    return {"Hello": "World"}

def create_user(username: str, fullname: str, email: str, password: str):
    try:
        response = UserService.create_user(username, fullname, email, password)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_user(user_id: int, username: str, fullname: str, email: str, password: str):
    try:
        response = UserService.update_user(user_id, username, fullname, email, password)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_user(user_id: int):
    try:
        response = UserService.delete_user(user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_all_users():
    try:
        response = UserService.get_all_users()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_user_by_id(user_id: int):
    try: 
        response = UserService.get_user_by_id(user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def validate_user(username: str, password: str):
    try:
        response = UserService.validate_user(username, password)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))