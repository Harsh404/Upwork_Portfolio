from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import create_access_token, create_refresh_token, decode_token
from app.schema.schema_user import UserCreate, UserPublic, Token, TokenData
from app.crud import crud_user
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# --- Admin bootstrap route (create first admin if none exists) ---
@router.post("/bootstrap-admin", response_model=UserPublic)
async def bootstrap_admin(user: UserCreate):
    existing = await crud_user.get_by_email(user.email) or await crud_user.get_by_username(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user_id = await crud_user.create_user(user, role="admin")
    doc = await crud_user.get_by_id(user_id)
    return {
        "id": str(doc["_id"]),
        "username": doc["username"],
        "email": doc["email"],
        "role": doc["role"],
        "is_active": doc.get("is_active", True),
    }

@router.post("/register", response_model=UserPublic)
async def register(user: UserCreate):
    existing = await crud_user.get_by_email(user.email) or await crud_user.get_by_username(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user_id = await crud_user.create_user(user, role="viewer")
    doc = await crud_user.get_by_id(user_id)
    return {
        "id": str(doc["_id"]),
        "username": doc["username"],
        "email": doc["email"],
        "role": doc["role"],
        "is_active": doc.get("is_active", True),
    }

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await crud_user.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    payload = {"user_id": str(user["_id"]), "username": user["username"], "role": user.get("role", "viewer")}
    access_token = create_access_token(payload)
    refresh_token = create_refresh_token(payload)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
async def refresh_token(refresh_token: str):
    try:
        data = decode_token(refresh_token)
        if data.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    # Verify user still exists
    user = await crud_user.get_by_id(data["user_id"])
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    payload = {"user_id": str(user["_id"]), "username": user["username"], "role": user.get("role", "viewer")}
    new_access_token = create_access_token(payload)
    new_refresh_token = create_refresh_token(payload)
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}

# --- Dependencies to use in other routes ---
async def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        data = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    return TokenData(**data)

async def get_current_admin(user: TokenData = Depends(get_current_user)) -> TokenData:
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user
