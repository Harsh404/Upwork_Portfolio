from pydantic import BaseModel
from typing import Optional, List

class ReviewSchema(BaseModel):
    rating: int
    comment: Optional[str]

class ProductCreateSchema(BaseModel):
    name: str
    description: Optional[str]
    price: float
    category: Optional[str] = None

class ProductResponseSchema(ProductCreateSchema):
    id: str
    reviews: List[ReviewSchema] = []
