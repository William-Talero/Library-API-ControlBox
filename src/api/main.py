"""RANTE API"""

# FastAPI
from fastapi import FastAPI

# Routers 
from src.api.routers import database, user, book, review

app = FastAPI()

app.include_router(database.router, tags=["database"], prefix="/database")
app.include_router(user.router, tags=["users"], prefix="/user")
app.include_router(book.router, tags=["books"], prefix="/book")
app.include_router(review.router, tags=["reviews"], prefix="/review")