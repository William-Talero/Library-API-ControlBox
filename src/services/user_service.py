from sqlalchemy.orm import Session
from src.models.user_model import User
from src.database.database_connection import get_db
import hashlib

class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str):
        db = next(get_db())
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(username=username, fullname="Maria", email=email, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update_user(user_id: int, username: str, email: str, password: str):
        db = next(get_db())
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        user.username = username
        user.email = email
        user.password = password
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
