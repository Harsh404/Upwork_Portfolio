from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api.v1 import routes_projects
from app.api.v1 import routes_user
from app.api.v1 import routes_blog
from app.api.v1 import routes_contact
from app.api.v1 import routes_products
from app.api.v1 import routes_services
from app.api.v1 import routes_media
from app.crud import crud_user

app = FastAPI(title=settings.project_name)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

app.include_router(routes_user.router, prefix=settings.api_v1_str)
app.include_router(routes_projects.router, prefix=settings.api_v1_str)
app.include_router(routes_blog.router, prefix=settings.api_v1_str)
app.include_router(routes_contact.router, prefix=settings.api_v1_str)
app.include_router(routes_products.router, prefix=settings.api_v1_str)
app.include_router(routes_services.router, prefix=settings.api_v1_str)
app.include_router(routes_media.router, prefix=settings.api_v1_str)