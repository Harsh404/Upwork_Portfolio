from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class MediaModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    filename: str
    content_type: str
    size: int
    url: str
    alt_text: Optional[str]