from fastapi import APIRouter, Depends, HTTPException
from app.schema.schema_product import ProductCreateSchema, ProductResponseSchema, ReviewSchema
from app.crud import crud_product
from app.services.rating_service import add_review_to_product
from app.api.v1.routes_user import get_current_admin, get_current_user
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/create", response_model=ProductResponseSchema)
async def create_product(product: ProductCreateSchema, user=Depends(get_current_admin)):
    return await crud_product.create_product(product.dict())


@router.get("/get_all", response_model=List[ProductResponseSchema])
async def get_products():
    return await crud_product.get_all_products()


@router.get("/get/{product_id}", response_model=ProductResponseSchema)
async def get_product(product_id: str):
    product = await crud_product.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/{product_id}/reviews", response_model=ProductResponseSchema)
async def add_review(product_id: str, review: ReviewSchema, user=Depends(get_current_user)):
    try:
        updated_product = await add_review_to_product(product_id, review, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
