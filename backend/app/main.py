from fastapi import FastAPI
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api.v1 import routes_projects

app = FastAPI(title=settings.PROJECT_NAME)

# Startup / Shutdown Events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Routers
app.include_router(routes_projects.router, prefix=settings.API_V1_STR)
