from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

# Helper to handle Mongo ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# MongoDB model (internal representation)
class ProjectModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    title: str
    description: str
    tech_stack: list[str]
    live_url: Optional[str]
    repo_url: Optional[str]
