from bson import ObjectId
import datetime
from app.db import mongodb
from app.models.model_blog import BlogCreate, BlogUpdate

BLOG_COLLECTION = "blogs"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[BLOG_COLLECTION]

async def create_blog_data(blog_data: BlogCreate) -> dict:
    blog = blog_data.model_dump()
    blog["created_at"] = datetime.datetime.now(datetime.UTC)
    blog["updated_at"] = datetime.datetime.now(datetime.UTC)
    result = await get_collection().insert_one(blog)
    blog["id"] = str(result.inserted_id)
    return blog

async def get_all_blogs():
    blogs = []
    cursor = get_collection().find({})
    async for blog in cursor:
        blog["_id"] = str(blog["_id"])
        blogs.append(blog)
    return blogs

async def get_blog_by_id(blog_id: str):
    blog = await get_collection().find_one({"_id": ObjectId(blog_id)})
    if blog:
        blog["_id"] = str(blog["_id"])
    return blog

async def update_blog_data(blog_id: str, update_data: BlogUpdate):
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    update_dict["updated_at"] = datetime.datetime.now(datetime.UTC)
    result = await get_collection().update_one(
        {"_id": ObjectId(blog_id)}, {"$set": update_dict}
    )
    return result.modified_count > 0

async def delete_blog_data(blog_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(blog_id)})
    return result.deleted_count > 0
