from app.db import mongodb
from app.schema.schema_blog import BlogCreate
from app.models.model_blog import BlogModel
from bson import ObjectId
from datetime import datetime

BLOGS_COLLECTION = "blogs"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[BLOGS_COLLECTION]

async def create_blog(blog: BlogCreate, author_id: str):
    new_blog = blog.dict()
    new_blog["author"] = author_id
    new_blog["created_at"] = datetime.utcnow()
    new_blog["updated_at"] = datetime.utcnow()
    result = await get_collection().insert_one(new_blog)
    return str(result.inserted_id)

async def get_all_blogs(published_only: bool = True):
    query = {"is_published": True} if published_only else {}
    blogs = await get_collection().find(query).sort("created_at", -1).to_list(100)
    return blogs

async def get_blog_by_id(blog_id: str):
    blog = await get_collection().find_one({"_id": ObjectId(blog_id)})
    return blog

async def update_blog(blog_id: str, data: dict):
    data["updated_at"] = datetime.utcnow()
    result = await get_collection().update_one(
        {"_id": ObjectId(blog_id)}, {"$set": data}
    )
    return result.modified_count

async def delete_blog(blog_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(blog_id)})
    return result.deleted_count
