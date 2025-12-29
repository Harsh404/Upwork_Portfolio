import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    project_name: str = "Portfolio Backend"
    api_v1_str: str = "/api/v1"
    mongo_uri: str = os.getenv("MONGO_URI")
    database_name: str = os.getenv("DATABASE_NAME")

    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    refresh_token_expire_days: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

settings = Settings()


