"""DATABASE ROUTER"""

# FastAPI
from fastapi import APIRouter

# Controllers
from src.api.controllers.database import create_database

router = APIRouter()

@router.post("/create-database")
def create_database_route():
    return create_database()