from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class ContestBase(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime

class ContestCreate(ContestBase):
    problem_ids: List[int]

class Contest(ContestBase):
    id: int
    creator_id: int
    problems: List[int]
    participants: List[int] = []
    leaderboard: Dict[int, int] = {}
    created_at: datetime

    class Config:
        orm_mode = True