from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_media import MediaCreate, MediaResponse
from app.crud import crud_media
from app.api.v1.routes_user import get_current_admin

router = APIRouter(prefix="/media", tags=["Media"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def upload_media(media: MediaCreate):
    media_id = await crud_media.create_media(media)
    return media_id

@router.get("/", response_model=list[MediaResponse])
async def list_media():
    media = await crud_media.get_all_media()
    return [{**m, "id": str(m["_id"])} for m in media]

@router.get("/{media_id}", response_model=MediaResponse)
async def get_media(media_id: str):
    media = await crud_media.get_media_by_id(media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")
    media["id"] = str(media["_id"])
    return media

@router.delete("/{media_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_media(media_id: str):
    deleted = await crud_media.delete_media(media_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Media not found")
    return {"status": "success", "deleted_count": deleted}
