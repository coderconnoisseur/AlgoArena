from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    xp: int = 0
    solved_problems: List[int] = []
    created_problems: List[int] = []
    is_active: bool = True
    created_at: datetime

    class Config:
        orm_mode = True