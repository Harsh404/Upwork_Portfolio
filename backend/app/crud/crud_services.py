from app.db import mongodb
from app.schema.schema_services import ServiceCreate
from bson import ObjectId

SERVICES_COLLECTION = "services"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[SERVICES_COLLECTION]

async def create_service(service: ServiceCreate):
    new_service = service.dict()
    result = await get_collection().insert_one(new_service)
    return str(result.inserted_id)

async def get_all_services():
    services = await get_collection().find().to_list(100)
    return services

async def get_service_by_id(service_id: str):
    service = await get_collection().find_one({"_id": ObjectId(service_id)})
    return service

async def update_service(service_id: str, data: dict):
    result = await get_collection().update_one(
        {"_id": ObjectId(service_id)}, {"$set": data}
    )
    return result.modified_count

async def delete_service(service_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(service_id)})
    return result.deleted_count
