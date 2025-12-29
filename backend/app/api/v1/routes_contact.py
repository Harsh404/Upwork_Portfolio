from fastapi import APIRouter, HTTPException, Depends
from app.schema.schema_contact import ContactCreate, ContactResponse
from app.crud import crud_contact
from app.api.v1.routes_user import get_current_admin

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/", response_model=str)
async def submit_contact(contact: ContactCreate):
    contact_id = await crud_contact.create_contact(contact)
    return contact_id

@router.get("/", response_model=list[ContactResponse], dependencies=[Depends(get_current_admin)])
async def list_contacts():
    contacts = await crud_contact.get_all_contacts()
    return [{**c, "id": str(c["_id"])} for c in contacts]

@router.get("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(get_current_admin)])
async def get_contact(contact_id: str):
    contact = await crud_contact.get_contact_by_id(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact["id"] = str(contact["_id"])
    return contact

@router.delete("/{contact_id}", response_model=dict, dependencies=[Depends(get_current_admin)])
async def delete_contact(contact_id: str):
    deleted = await crud_contact.delete_contact(contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"status": "success", "deleted_count": deleted}
