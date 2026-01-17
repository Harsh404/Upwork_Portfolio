from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_project import ProjectCreate, ProjectResponse
from app.crud import crud_projects
from app.api.v1.routes_user import get_current_admin  # <- add

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def add_project(project: ProjectCreate, user:dict = Depends(get_current_admin)):
    project_id = await crud_projects.create_project(project, user.user_id)
    return project_id

@router.get("/all", response_model=list[ProjectResponse])
async def list_all_projects():
    projects = await crud_projects.get_all_projects_user()
    return [{**p, "id": str(p["_id"]), "_id": str(p["_id"])} for p in projects]

@router.get("/", response_model=list[ProjectResponse])
async def list_projects(user:dict = Depends(get_current_admin)):
    user_id = user.user_id
    projects = await crud_projects.get_all_projects(user_id)
    return [{**p, "id": str(p["_id"]), "_id": str(p["_id"])} for p in projects]

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str):
    project = await crud_projects.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project["id"] = str(project["_id"])
    return project

@router.put("/{project_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def update_project(project_id: str, project: ProjectCreate):
    updated = await crud_projects.update_project(project_id, project.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "success", "updated_count": updated}

@router.delete("/{project_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_project(project_id: str):
    deleted = await crud_projects.delete_project(project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "success", "deleted_count": deleted}
