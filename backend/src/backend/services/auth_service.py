from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from fastapi import HTTPException
from backend.lib.config import config
from .user_service import get_user_by_email
import bcrypt 

def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()  
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def generate_token_from_user(user):
    access_token_expires = timedelta(minutes=config.TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "email": user.email }, expires_delta=access_token_expires
    )

    return access_token

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    
    return encoded_jwt

async def authenticate_user(prisma, email: str, password: str):
    user = await get_user_by_email(prisma, email)
    
    if not user or not verify_password(password, user.password):
        return False
    
    return user

async def login(prisma, email: str, password: str):
    user = await authenticate_user(prisma, email, password)

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=config.TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
