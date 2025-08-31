from bson import ObjectId
import datetime
from app.db import mongodb
from app.schema.schema_about import AboutCreate, AboutUpdate

ABOUT_COLLECTION = "about"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[ABOUT_COLLECTION]

# ✅ Create About Section
async def create_about_data(about_data: AboutCreate) -> dict:
    about = about_data.model_dump()
    about["created_at"] = datetime.datetime.now(datetime.UTC)
    about["updated_at"] = datetime.datetime.now(datetime.UTC)
    result = await get_collection().insert_one(about)
    about["id"] = str(result.inserted_id)
    return about

# ✅ Get All (though we usually expect only one about section)
async def get_all_about():
    abouts = []
    cursor = get_collection().find({})
    async for about in cursor:
        about["id"] = str(about["_id"])
        abouts.append(about)
    return abouts

# ✅ Get Single About by ID
async def get_about_by_id(about_id: str):
    about = await get_collection().find_one({"_id": ObjectId(about_id)})
    if about:
        about["id"] = str(about["_id"])
    return about

# ✅ Update About Section
async def update_about_data(about_id: str, update_data: AboutUpdate):
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    update_dict["updated_at"] = datetime.datetime.now(datetime.UTC)
    result = await get_collection().update_one(
        {"_id": ObjectId(about_id)}, {"$set": update_dict}
    )
    return result.modified_count > 0

# ✅ Delete About Section
async def delete_about_data(about_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(about_id)})
    return result.deleted_count > 0
