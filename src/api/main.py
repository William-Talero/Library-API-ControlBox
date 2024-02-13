"""RANTE API"""

# FastAPI
from fastapi import FastAPI

# Routers 
from src.api.routers import database, user

app = FastAPI()

app.include_router(database.router, tags=["database"], prefix="/database")
app.include_router(user.router, tags=["users"], prefix="/user")
