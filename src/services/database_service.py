from src.models.user_model import Base as UserBase
from src.models.books_model import Base as BooksBase
from src.models.reviews_model import Base as ReviewBase
from src.database.database_connection import engine

class DatabaseService:
    @staticmethod
    def create_database():
        UserBase.metadata.create_all(bind=engine)
        BooksBase.metadata.create_all(bind=engine)
        ReviewBase.metadata.create_all(bind=engine)
        return {"result": "Database Created Successfully"}

