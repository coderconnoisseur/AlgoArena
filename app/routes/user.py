from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schema.user import User, UserCreate
from ..models.user import User as UserModel

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    # Implementation here
    pass

@router.get("/", response_model=List[User])
async def get_users():
    # Implementation here
    pass

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    # Implementation here
    pass

@router.get("/{user_id}/solved_problems")
async def get_solved_problems(user_id: int):
    # Implementation here
    pass

@router.get("/{user_id}/created_problems")
async def get_created_problems(user_id: int):
    # Implementation here
    pass

@router.get("/{user_id}/contests")
async def get_user_contests(user_id: int):
    # Implementation here
    pass