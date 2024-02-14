from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.database_connection import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    author = Column(String, index=True)
    category = Column(String, index=True)
    resume = Column(String, index=True)
    image = Column(String, index=True)
    
    review = relationship("Review", back_populates="book")