from app.db import mongodb
from app.schema.schema_project import ProjectCreate
from bson import ObjectId

PROJECTS_COLLECTION = "project"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[PROJECTS_COLLECTION]

async def create_project(project: ProjectCreate):
    new_project = project.dict()
    result = await get_collection().insert_one(new_project)
    return str(result.inserted_id)

async def get_all_projects():
    projects = await get_collection().find().to_list(100)
    return projects

async def get_project_by_id(project_id: str):
    project = await get_collection().find_one({"_id": ObjectId(project_id)})
    return project

async def update_project(project_id: str, data: dict):
    result = await get_collection().update_one(
        {"_id": ObjectId(project_id)}, {"$set": data}
    )
    return result.modified_count

async def delete_project(project_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(project_id)})
    return result.deleted_count


async def add_rating(project_id: str, rating: int):
    project = await get_project_by_id(project_id)
    if not project:
        return None

    # Initialize if missing
    if "ratings" not in project:
        project["ratings"] = []

    project["ratings"].append(rating)

    await get_collection().update_one(
        {"_id": ObjectId(project_id)},
        {"$set": {"ratings": project["ratings"]}}
    )

    return project
