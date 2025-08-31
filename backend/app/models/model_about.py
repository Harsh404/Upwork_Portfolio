from pydantic import BaseModel, Field
from typing import List, Optional
import datetime

class AboutModel(BaseModel):
    id: Optional[str] = None
    summary: str
    skills: List[str] = []
    experience: List[str] = []
    created_at: datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime = Field(default_factory=datetime.datetime.now)

