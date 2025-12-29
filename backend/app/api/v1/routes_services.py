from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_services import ServiceCreate, ServiceResponse
from app.crud import crud_services
from app.api.v1.routes_user import get_current_admin

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def create_service(service: ServiceCreate):
    service_id = await crud_services.create_service(service)
    return service_id

@router.get("/", response_model=list[ServiceResponse])
async def list_services():
    services = await crud_services.get_all_services()
    return [{**s, "id": str(s["_id"])} for s in services]

@router.get("/{service_id}", response_model=ServiceResponse)
async def get_service(service_id: str):
    service = await crud_services.get_service_by_id(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    service["id"] = str(service["_id"])
    return service

@router.put("/{service_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def update_service(service_id: str, service: ServiceCreate):
    updated = await crud_services.update_service(service_id, service.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"status": "success", "updated_count": updated}

@router.delete("/{service_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_service(service_id: str):
    deleted = await crud_services.delete_service(service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"status": "success", "deleted_count": deleted}
