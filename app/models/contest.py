from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from ..database import Base

class Contest(Base):
    __tablename__ = "contests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    creator_id = Column(Integer, nullable=False)
    problems = Column(JSON, default=list)  # List of problem IDs
    participants = Column(JSON, default=list)  # List of participant IDs
    leaderboard = Column(JSON, default=dict)  # Dictionary of user_id: score
    created_at = Column(DateTime(timezone=True), server_default=func.now())