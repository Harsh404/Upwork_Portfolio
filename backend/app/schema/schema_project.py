from typing import Optional, List
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    title: str
    description: str
    tech_stack: List[str]
    live_url: Optional[str] = None
    repo_url: Optional[str] = None

class ProjectResponse(ProjectCreate):
    id: str
    average_rating: float = 0.0
    ratings_count: int = 0

class ProjectRating(BaseModel):
    rating: int  # 1–5
