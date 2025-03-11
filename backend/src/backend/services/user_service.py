from backend.lib.db import prisma
from fastapi import HTTPException

async def create_user(email: str, hashed_password: str):
    try:
        user = await prisma.user.create(
            data={
                'email': email,
                'password': hashed_password
            }
        )
        return user
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"User creation failed: {str(e)}")

async def get_user(user_id: str):
    user = await prisma.user.find_unique(
        where={"id": user_id},
        include={
            "posts": True,
        }
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_dict = user.model_dump()  
    user_dict.pop("password", None)

    return user_dict

async def get_user_by_email(email: str):
    user = await prisma.user.find_unique(
        where={"email": email},
        include={
            "posts": False,
        }
    )

    return user

async def update_user(user_id: str, data: dict):
    try:
        user = await prisma.user.update(
            where={'id': user_id},
            data=data
        )
        return user
    except Exception:
        raise HTTPException(status_code=400, detail="User update failed")

async def delete_user(user_id: str):
    try:
        user = await prisma.user.delete(where={'id': user_id})
        return user
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")

async def get_user_posts(user_id: str):
    user = await prisma.user.find_unique(
        where={'id': user_id},
        include={'posts': True}
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.posts

async def get_user_with_posts(user_id: str):
    user = await prisma.user.find_unique(
        where={'id': user_id},
        include={'posts': True, 'userPosts': True}
    )
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
