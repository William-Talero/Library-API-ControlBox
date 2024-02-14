from sqlalchemy.orm import Session
from src.models.user_model import User
from src.database.database_connection import get_db
import hashlib

class UserService:
    @staticmethod
    def create_user(username: str, fullname: str, email: str, password: str):
        db = next(get_db())
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(username=username, fullname=fullname, email=email, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update_user(user_id: int, username: str, fullname: str, email: str, password: str):
        db = next(get_db())
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user.username = username
        user.fullname = fullname
        user.email = email
        user.hashed_password = hashed_password
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(user_id: int):
        db = next(get_db())
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True
    
    @staticmethod
    def get_all_users():
        db = next(get_db())
        users = db.query(User).all()
        return users
    
    @staticmethod
    def get_user_by_id(user_id: int):
        db = next(get_db())
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user_data = {key: value for key, value in user.__dict__.items() if key != 'hashed_password'}
            return user_data
        else:
            return "User not found."
    
    @staticmethod
    def validate_user(username: str, password: str) -> bool:
        db = next(get_db())
        user = db.query(User).filter(User.username == username).first()
        
        if not user:
            return {"user": False, "validate": False}
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return {"user": True, "validate": user.hashed_password == hashed_password, "userData": user if user.hashed_password == hashed_password else False}
