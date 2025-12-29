from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []
    is_published: bool = True

class BlogResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    author: str
    created_at: datetime
    updated_at: datetime
    is_published: bool