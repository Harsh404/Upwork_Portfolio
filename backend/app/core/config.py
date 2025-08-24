import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Portfolio Backend"
    API_V1_STR: str = "/api/v1"
    MONGODB_URI: str = os.getenv("MONGO_URI")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

settings = Settings()


