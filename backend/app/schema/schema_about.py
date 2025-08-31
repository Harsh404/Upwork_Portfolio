from pydantic import BaseModel
from typing import List, Optional

class AboutCreate(BaseModel):
    summary: str
    skills: List[str]
    experience: List[str]

class AboutUpdate(BaseModel):
    summary: Optional[str] = None
    skills: Optional[List[str]] = None
    experience: Optional[List[str]] = None

class AboutResponse(BaseModel):
    id: str
    summary: str
    skills: List[str]
    experience: List[str]
