from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_blog import BlogCreate, BlogResponse
from app.crud import crud_blog
from app.api.v1.routes_user import get_current_user, get_current_admin
from app.schema.schema_user import TokenData

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def create_blog(blog: BlogCreate, user: TokenData = Depends(get_current_admin)):
    blog_id = await crud_blog.create_blog(blog, user.username)
    return blog_id

@router.get("/", response_model=list[BlogResponse], dependencies=[Depends(get_current_user)])
async def list_blogs():
    blogs = await crud_blog.get_all_blogs()
    return [{**b, "id": str(b["_id"])} for b in blogs]

@router.get("/admin", response_model=list[BlogResponse], dependencies=[Depends(get_current_admin)])
async def list_blogs_admin():
    blogs = await crud_blog.get_all_blogs_admin()
    return [{**b, "id": str(b["_id"])} for b in blogs]

@router.get("/{blog_id}", response_model=BlogResponse, dependencies=[Depends(get_current_user)])
async def get_blog(blog_id: str):
    blog = await crud_blog.get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog["id"] = str(blog["_id"])
    return blog

@router.put("/{blog_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def update_blog(blog_id: str, blog: BlogCreate):
    updated = await crud_blog.update_blog(blog_id, blog.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"status": "success", "updated_count": updated}

@router.delete("/{blog_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_blog(blog_id: str):
    deleted = await crud_blog.delete_blog(blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"status": "success", "deleted_count": deleted}
