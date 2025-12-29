from typing import Optional, List
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: Optional[float] = None
    features: List[str] = []
    category: Optional[str] = None

class ProductResponse(ProductCreate):
    id: str