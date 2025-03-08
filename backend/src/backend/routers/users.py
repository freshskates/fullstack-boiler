from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from backend.dependencies import get_current_user

from backend.lib.config import config
from backend.services import auth_service, user_service

router = APIRouter()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/me", tags=["users"])
async def read_user_me(user_id: int = Depends(get_current_user)):

    user = await user_service.get_user(user_id)
    return user

class UserCreate(BaseModel):
    email: str
    password: str

@router.post("/create", tags=["users"])
async def create_user(body: UserCreate):
    hashed_password = auth_service.get_password_hash(body.password)

    user = await user_service.create_user(body.email, hashed_password)

    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")

    user_token = auth_service.generate_token_from_user(user)

    return {"user": user, "token": user_token}

@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}


