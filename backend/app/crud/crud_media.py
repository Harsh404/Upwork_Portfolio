from app.db import mongodb
from app.schema.schema_media import MediaCreate
from bson import ObjectId

MEDIA_COLLECTION = "media"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[MEDIA_COLLECTION]

async def create_media(media: MediaCreate):
    new_media = media.dict()
    result = await get_collection().insert_one(new_media)
    return str(result.inserted_id)

async def get_all_media():
    media = await get_collection().find().to_list(100)
    return media

async def get_media_by_id(media_id: str):
    media = await get_collection().find_one({"_id": ObjectId(media_id)})
    return media

async def delete_media(media_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(media_id)})
    return result.deleted_count
