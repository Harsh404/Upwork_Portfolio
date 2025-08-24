from typing import List, Optional
from bson import ObjectId
from app.db import mongodb
from datetime import datetime

PRODUCTS_COLLECTION = "product"


def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[PRODUCTS_COLLECTION]


def product_helper(product) -> dict:
    """Convert MongoDB doc -> Python dict"""
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "reviews": product.get("reviews", []),
        "average_rating": product.get("average_rating", 0.0),
    }


async def create_product(product_data: dict) -> dict:
    product_data["reviews"] = []
    product_data["average_rating"] = 0.0
    result = await get_collection().insert_one(product_data)
    product = await get_collection().find_one({"_id": result.inserted_id})
    return product_helper(product)


async def get_all_products() -> List[dict]:
    products = []
    async for product in get_collection().find():
        products.append(product_helper(product))
    return products


async def get_product_by_id(product_id: str) -> Optional[dict]:
    product = await get_collection().find_one({"_id": ObjectId(product_id)})
    if product:
        return product_helper(product)
    return None


async def update_product(product_id: str, update_data: dict) -> Optional[dict]:
    await get_collection().update_one(
        {"_id": ObjectId(product_id)}, {"$set": update_data}
    )
    product = await get_collection().find_one({"_id": ObjectId(product_id)})
    if product:
        return product_helper(product)
    return None