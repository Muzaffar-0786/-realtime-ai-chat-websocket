"""
Project : Real-Time AI Chat (MVP)
File    : main.py
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import settings
from database import Base, engine, get_db

from schemas import (
    UserCreate,
    UserLogin,
    Token,
)

from crud import (
    create_user,
    authenticate_user,
    get_user_by_email,
    get_user_by_username,
)

from auth import create_access_token

from dependencies import get_current_user

from websocket import router as websocket_router
from chat_routes import router as chat_router

from exceptions import register_exception_handlers


# ==========================================================
# Create Database Tables
# ==========================================================

Base.metadata.create_all(bind=engine)


# ==========================================================
# FastAPI App
# ==========================================================

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)


# ==========================================================
# Register Exception Handlers
# ==========================================================

register_exception_handlers(app)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# Routers
# ==========================================================

app.include_router(chat_router)
app.include_router(websocket_router)


# ==========================================================
# Root Endpoint
# ==========================================================

@app.get("/", tags=["Root"])
def root():

    return {
        "success": True,
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "message": "Real-Time AI Chat API is running successfully.",
    }


# ==========================================================
# Health Check
# ==========================================================

@app.get("/health", tags=["Health"])
def health():

    return {
        "success": True,
        "status": "healthy",
    }


# ==========================================================
# Signup API
# ==========================================================

@app.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"],
)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists.",
        )

    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists.",
        )

    new_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password,
    )

    return {
        "success": True,
        "message": "Account created successfully.",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        },
    }
    # ==========================================================
# Login API
# ==========================================================

@app.post(
    "/login",
    response_model=Token,
    tags=["Authentication"],
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):

    authenticated_user = authenticate_user(
        db=db,
        email=user.email,
        password=user.password,
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    access_token = create_access_token(
        user_id=authenticated_user.id,
    )

    return Token(
        access_token=access_token,
        token_type="bearer",
    )


# ==========================================================
# Current User
# ==========================================================

@app.get(
    "/me",
    tags=["Authentication"],
)
def get_current_logged_user(
    current_user=Depends(get_current_user),
):

    return {
        "success": True,
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "created_at": current_user.created_at,
        },
    }


# ==========================================================
# API Information
# ==========================================================

@app.get("/info", tags=["System"])
def api_info():

    return {
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "authentication": "JWT",
        "database": "SQLite",
        "ai": "Google Gemini",
        "websocket": "/ws/chat/{chat_id}",
        "documentation": "/docs",
    }
