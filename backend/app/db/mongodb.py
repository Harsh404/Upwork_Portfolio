from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client: AsyncIOMotorClient | None = None
db = None

async def connect_to_mongo():
    global client, db
    if client is None:
        client = AsyncIOMotorClient(settings.mongo_uri)
        db = client[settings.database_name]
        # test connection
        await db.command("ping")
        print("✅ Connected to MongoDB Atlas")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("❌ MongoDB connection closed")
