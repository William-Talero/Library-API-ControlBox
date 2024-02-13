from src.models.user_model import Base
from src.database.database_connection import engine

class DatabaseService:
    @staticmethod
    def create_database():
        Base.metadata.create_all(bind=engine)
        return {"result": "Database Created Successfully"}

