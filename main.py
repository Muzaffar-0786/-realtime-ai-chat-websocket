"""
Project : Real-Time AI Chat (MVP)
File    : main.py
"""

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import settings
from database import Base, engine, get_db
from schemas import UserCreate, UserLogin, Token
from crud import (
    create_user,
    authenticate_user,
    get_user_by_email,
    get_user_by_username,
)
from auth import create_access_token
from websocket import router as websocket_router


# -----------------------------------------------------
# Create Database Tables
# -----------------------------------------------------

Base.metadata.create_all(bind=engine)


# -----------------------------------------------------
# FastAPI App
# -----------------------------------------------------

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)


# -----------------------------------------------------
# CORS
# -----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------
# WebSocket Router
# -----------------------------------------------------

app.include_router(websocket_router)


# -----------------------------------------------------
# Root
# -----------------------------------------------------

@app.get("/")
def root():

    return {
        "message": "Real-Time AI Chat API is Running."
    }


# -----------------------------------------------------
# Signup
# -----------------------------------------------------

@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )

    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )

    new_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password,
    )

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
    }


# -----------------------------------------------------
# Login
# -----------------------------------------------------

@app.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):

    db_user = authenticate_user(
        db=db,
        email=user.email,
        password=user.password,
    )

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    access_token = create_access_token(
        user_id=db_user.id,
    )

    return Token(
        access_token=access_token,
        token_type="bearer",
    )
