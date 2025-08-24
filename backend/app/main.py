from fastapi import FastAPI
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api.v1 import routes_projects, routes_blog, routes_products
from app.api.v1 import routes_user
from app.crud import crud_user

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()
    # create user indexes
    try:
        await crud_user.ensure_indexes()
    except Exception as e:
        print("Index creation warning:", e)

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(routes_user.router, prefix=settings.API_V1_STR)
app.include_router(routes_projects.router, prefix=settings.API_V1_STR)
app.include_router(routes_blog.router, prefix=settings.API_V1_STR)
app.include_router(routes_products.router, prefix=settings.API_V1_STR)
