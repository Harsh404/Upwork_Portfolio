from pydantic import BaseModel, HttpUrl
from typing import Optional


# DB Model (Mongo)
class HeroInDB(BaseModel):
    id: Optional[str] = None
    title: str
    subtitle: str
    description: str
    profile_image: Optional[HttpUrl] = None
    resume_link: Optional[HttpUrl] = None

class HeroUpdate(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    profile_image: Optional[HttpUrl] = None
    resume_link: Optional[HttpUrl] = None
