# app/routes/blog_routes.py

from fastapi import APIRouter, Depends, HTTPException
from app.models.model_blog import BlogCreate, BlogUpdate
from app.crud.crud_blog import (
    create_blog_data,
    get_all_blogs,
    get_blog_by_id,
    update_blog_data,
    delete_blog_data
)
from app.api.v1.routes_user import get_current_admin   # ✅ Authentication

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/create", response_model=dict)
async def create_blog(blog: BlogCreate, user: dict = Depends(get_current_admin)):
    """Only authenticated users can create blogs"""
    blog = await create_blog_data(blog)
    blog["id"] = str(blog.pop("_id"))   
    return blog

@router.get("/", response_model=list)
async def get_blogs():
    """Anyone can view blogs"""
    return await get_all_blogs()

@router.get("/{blog_id}", response_model=dict)
async def get_blog(blog_id: str):
    """Anyone can view a specific blog"""
    blog = await get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.put("/{blog_id}", response_model=dict)
async def update_blog(blog_id: str, data: BlogUpdate, user: dict = Depends(get_current_admin)):
    """Only authenticated users can update blogs"""
    return await update_blog_data(blog_id, data)

@router.delete("/{blog_id}", response_model=dict)
async def delete_blog(blog_id: str, user: dict = Depends(get_current_admin)):
    """Only authenticated users can delete blogs"""
    return await delete_blog_data(blog_id)
