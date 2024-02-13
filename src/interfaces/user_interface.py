from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    disabled: bool = None
