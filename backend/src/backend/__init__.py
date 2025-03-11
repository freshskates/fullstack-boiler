from typing import Union
from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from backend.lib.db import prisma
from backend.routers import posts, users
from backend.lib.types import Item
from fastapi.middleware.cors import CORSMiddleware

# https://fastapi.tiangolo.com/advanced/events/#async-context-manager
# best practice when handling db connections
@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    print("[INFO] Prisma connected")
    yield
    await prisma.disconnect()
    print("[INFO] Prisma disconnected")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.api_route("/{path_name:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(request: Request, path_name: str):
    print(f"Path: {path_name}")
    return {
        "path": path_name,
        "method": request.method,
        "status": "not found"
    }

