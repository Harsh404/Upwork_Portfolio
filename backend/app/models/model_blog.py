from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

class BlogBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    content: str
    media: Optional[List[HttpUrl]] = []  # store image/video URLs
    author: Optional[str] = "Admin"

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    media: Optional[List[HttpUrl]]

class BlogDB(BlogBase):
    id: Optional[str]
    created_at: datetime
    updated_at: datetime
