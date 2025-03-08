from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies import get_token_header
from prisma import Prisma

router = APIRouter()

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["posts"])
async def get_posts():
    return [{"username": "Rick"}, {"username": "Morty"}]
