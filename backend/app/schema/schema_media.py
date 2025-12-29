from pydantic import BaseModel
from typing import Optional

class MediaCreate(BaseModel):
    filename: str
    content_type: str
    size: int
    url: str
    alt_text: Optional[str] = None

class MediaResponse(MediaCreate):
    id: str