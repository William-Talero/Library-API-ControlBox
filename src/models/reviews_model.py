from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from src.database.database_connection import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    starts = Column(Integer, index=True)
    review = Column(String, index=True)
    date = Column(Date, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    book = relationship("Book", back_populates="review")
    user = relationship("User", back_populates="review")