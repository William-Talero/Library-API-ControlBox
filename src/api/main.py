"""RANTE API"""

# FastAPI
from fastapi import FastAPI

# Routers 
from src.api.routers import library

app = FastAPI()

app.include_router(library.router, tags=["library"], prefix="/library")
