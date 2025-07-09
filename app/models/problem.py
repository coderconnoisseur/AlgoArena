from sqlalchemy import Column, Integer, String, Float, Text
from app.database import Base

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)  # Question ID
    title = Column(String, nullable=False)              # Question Title
    slug = Column(String, unique=True, index=True)      # Question Slug
    text = Column(Text)                                 # Question Text
    tags = Column(String)                               # Topic Tagged text
    difficulty = Column(String)                         # Difficulty Level
    success_rate = Column(Float)                        # Success Rate
    total_submissions = Column(Integer)                 # total submission
    total_accepted = Column(Integer)                    # total accepted
    likes = Column(Integer)                             # Likes
    dislikes = Column(Integer)                          # Dislikes
    hints = Column(Text)                                # Hints
    similar_question_ids = Column(String)               # Similar Questions ID
    similar_question_texts = Column(Text)               # Similar Questions Text
