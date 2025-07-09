from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class User(UserBase):
    username: str
    email: EmailStr
    id: int
    xp: int = 0
    solved_problems: List[int] = []
    created_problems: List[int] = []
    is_active: bool = True
    created_at: datetime

    class Config:
        orm_mode = True