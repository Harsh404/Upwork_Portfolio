from app.services.rating_service import calculate_average
from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_project import ProjectCreate, ProjectRating, ProjectResponse
from app.crud import crud_projects
from app.api.v1.routes_user import get_current_admin  # <- add

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=str, dependencies=[Depends(get_current_admin)])
async def add_project(project: ProjectCreate):
    project_id = await crud_projects.create_project(project)
    return project_id

@router.get("/", response_model=list[ProjectResponse])
async def list_projects():
    projects = await crud_projects.get_all_projects()
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


@router.post("/{project_id}/rate", response_model=ProjectResponse)
async def rate_project(project_id: str, rating: ProjectRating):
    project = await crud_projects.add_rating(project_id, rating.rating)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    avg_info = calculate_average(project.get("ratings", []))

    return {
        "id": str(project["_id"]),
        "title": project["title"],
        "description": project["description"],
        "tech_stack": project["tech_stack"],
        "live_url": project.get("live_url"),
        "repo_url": project.get("repo_url"),
        "average_rating": avg_info["average"],
        "ratings_count": avg_info["count"],
    }


@router.delete("/{project_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_project(project_id: str):
    deleted = await crud_projects.delete_project(project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"status": "success", "deleted_count": deleted}
