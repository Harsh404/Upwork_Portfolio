from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Review(BaseModel):
    user_id: str
    rating: int = Field(..., ge=1, le=5)  # rating 1-5
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    reviews: List[Review] = []
