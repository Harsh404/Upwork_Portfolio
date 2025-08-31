from datetime import datetime
from typing import Optional, List
from bson import ObjectId
from app.models.model_hero import HeroInDB, HeroUpdate
from app.db import mongodb  # assume MongoDB collection

HERO_COLLECTION = "hero"
def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[HERO_COLLECTION]


async def get_hero_by_id(hero_id: str):
    hero = await get_collection().find_one({"_id": ObjectId(hero_id)})
    if hero:
        hero["id"] = str(hero["_id"])
    return hero

async def create_hero_data(hero_data: HeroInDB) -> dict:
    hero = hero_data.model_dump()
    result = await get_collection().insert_one(hero)
    hero["id"] = str(result.inserted_id)
    return hero

async def update_hero_data(hero_id: str, update_data: HeroUpdate ):
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    result = await get_collection().update_one(
        {"_id": ObjectId(hero_id)}, {"$set": update_dict}
    )
    return result.modified_count > 0

async def delete_hero_data(hero_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(hero_id)})
    return result.deleted_count > 0

