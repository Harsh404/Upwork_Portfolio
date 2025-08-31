from fastapi import APIRouter, Depends, HTTPException, status
from app.models.model_hero import HeroInDB, HeroUpdate
from app.crud.crud_hero import get_hero_by_id, create_hero_data, update_hero_data, delete_hero_data
from app.api.v1.routes_user import get_current_admin  # assuming you already have auth

router = APIRouter(prefix="/hero", tags=["Hero Section"])

@router.get("/{hero_id}", response_model=HeroInDB)
async def get_hero(hero_id: str):
    hero = await get_hero_by_id(hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero section not set")
    return hero

@router.post("/", response_model=HeroInDB)
async def create_hero(hero_data: HeroInDB, user=Depends(get_current_admin)):
    # only authenticated user (you) can update
    hero=await create_hero_data(hero_data)
    hero["id"]=str(hero.pop("_id"))
    return hero

@router.put("/{hero_id}", response_model=HeroInDB)
async def update_hero(hero_id: str, hero_data: HeroUpdate, user=Depends(get_current_admin)):
    updated = await update_hero_data(hero_id, hero_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Hero section not found")
    return await get_hero_by_id(hero_id)

@router.delete("/{hero_id}", response_model=dict)
async def delete_hero(hero_id: str, user=Depends(get_current_admin)):
    deleted = await delete_hero_data(hero_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Hero section not found")
    return {"message": "Hero section deleted"}
