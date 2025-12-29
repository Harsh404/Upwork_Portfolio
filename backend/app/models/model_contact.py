from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class ContactModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    email: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow)