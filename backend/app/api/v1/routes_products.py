from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_product import ProductCreate, ProductResponse
from app.crud import crud_product
from app.api.v1.routes_user import get_current_admin

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def create_product(product: ProductCreate):
    product_id = await crud_product.create_product(product)
    return product_id

@router.get("/", response_model=list[ProductResponse])
async def list_products():
    products = await crud_product.get_all_products()
    return [{**p, "id": str(p["_id"])} for p in products]

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await crud_product.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = str(product["_id"])
    return product

@router.put("/{product_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def update_product(product_id: str, product: ProductCreate):
    updated = await crud_product.update_product(product_id, product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "success", "updated_count": updated}

@router.delete("/{product_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_product(product_id: str):
    deleted = await crud_product.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "success", "deleted_count": deleted}
