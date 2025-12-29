from app.db import mongodb
from app.schema.schema_product import ProductCreate
from bson import ObjectId

PRODUCTS_COLLECTION = "products"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[PRODUCTS_COLLECTION]

async def create_product(product: ProductCreate):
    new_product = product.dict()
    result = await get_collection().insert_one(new_product)
    return str(result.inserted_id)

async def get_all_products():
    products = await get_collection().find().to_list(100)
    return products

async def get_product_by_id(product_id: str):
    product = await get_collection().find_one({"_id": ObjectId(product_id)})
    return product

async def update_product(product_id: str, data: dict):
    result = await get_collection().update_one(
        {"_id": ObjectId(product_id)}, {"$set": data}
    )
    return result.modified_count

async def delete_product(product_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count
