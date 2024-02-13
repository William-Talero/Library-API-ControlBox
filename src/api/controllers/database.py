from fastapi import HTTPException, Depends
from src.services.database_service import DatabaseService

def create_database():
    try:
        response = DatabaseService.create_database()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))