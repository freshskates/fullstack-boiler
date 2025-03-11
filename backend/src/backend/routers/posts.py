from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma

router = APIRouter()

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

# todo: add post creation
