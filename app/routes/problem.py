from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schema.problem import Problem, ProblemCreate
from ..models.problem import Problem as ProblemModel

router = APIRouter(prefix="/problems", tags=["problems"])


@router.post("/", response_model=Problem)
async def create_problem(problem: ProblemCreate):
    # Implementation here
    pass

@router.get("/", response_model=List[Problem])
async def get_problems():
    # Implementation here
    pass

@router.get("/{problem_id}", response_model=Problem)
async def get_problem(problem_id: int):
    # Implementation here
    pass