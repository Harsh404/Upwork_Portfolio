from app.db import mongodb
from app.schema.schema_contact import ContactCreate
from bson import ObjectId

CONTACTS_COLLECTION = "contacts"

def get_collection():
    if mongodb.db is None:
        raise RuntimeError("Database not initialized. Did you connect?")
    return mongodb.db[CONTACTS_COLLECTION]

async def create_contact(contact: ContactCreate):
    new_contact = contact.dict()
    result = await get_collection().insert_one(new_contact)
    return str(result.inserted_id)

async def get_all_contacts():
    contacts = await get_collection().find().sort("created_at", -1).to_list(100)
    return contacts

async def get_contact_by_id(contact_id: str):
    contact = await get_collection().find_one({"_id": ObjectId(contact_id)})
    return contact

async def delete_contact(contact_id: str):
    result = await get_collection().delete_one({"_id": ObjectId(contact_id)})
    return result.deleted_count
