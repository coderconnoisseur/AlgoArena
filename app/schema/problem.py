from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TestCase(BaseModel):
    input: str
    expected_output: str
    is_hidden: bool = False
    points: int = 1

class ProblemBase(BaseModel):
    name: str
    description: str
    constraints: str
    difficulty: str
    category: str
    points: int
    time_limit: int = 2000
    memory_limit: int = 256

class ProblemCreate(ProblemBase):
    testcases: List[TestCase]

class Problem(ProblemBase):
    id: int
    created_by: int
    created_at: datetime
    testcases: List[TestCase]

    class Config:
        orm_mode = True