from typing import Optional
from bson import ObjectId
from app.db import mongodb
from app.core.security import hash_password, verify_password
from app.schema.schema_user import UserCreate

USERS_COLLECTION = "users"

def _col():
    if mongodb.db is None:
        raise RuntimeError("DB not initialized")
    return mongodb.db[USERS_COLLECTION]

async def ensure_indexes():
    await _col().create_index("email", unique=True)
    await _col().create_index("username", unique=True)

async def get_by_email(email: str) -> Optional[dict]:
    return await _col().find_one({"email": email})

async def get_by_username(username: str) -> Optional[dict]:
    return await _col().find_one({"username": username})

async def get_by_id(user_id: str) -> Optional[dict]:
    return await _col().find_one({"_id": ObjectId(user_id)})

async def create_user(data: UserCreate, role: str = "admin") -> str:
    doc = {
        "username": data.username,
        "email": data.email,
        "hashed_password": hash_password(data.password),
        "role": role,
        "is_active": True,
    }
    res = await _col().insert_one(doc)
    return str(res.inserted_id)

async def authenticate(username_or_email: str, password: str) -> Optional[dict]:
    user = await get_by_email(username_or_email) or await get_by_username(username_or_email)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    if not user.get("is_active", True):
        return None
    return user
