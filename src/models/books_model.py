from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from src.database.database_connection import Base

class User(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    autor = Column(String, index=True)
    category = Column(String, index=True)
    resume = Column(String, index=True)
    image = Column(String, index=True)