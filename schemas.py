"""
Project : Real-Time AI Chat (MVP)
File    : schemas.py

Pydantic schemas for request and response validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ==========================================================
# User Schemas
# ==========================================================

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime


# ==========================================================
# Token Schemas
# ==========================================================

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None


# ==========================================================
# Chat Schemas
# ==========================================================

class ChatCreate(BaseModel):
    title: str = Field(default="New Chat", max_length=200)


class ChatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    user_id: int
    created_at: datetime


# ==========================================================
# Message Schemas
# ==========================================================

class MessageCreate(BaseModel):
    content: str = Field(..., min_length=1)


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chat_id: int
    role: str
    content: str
    created_at: datetime


# ==========================================================
# WebSocket Schemas
# ==========================================================

class ChatRequest(BaseModel):
    chat_id: int
    message: str


class ChatAIResponse(BaseModel):
    role: str = "assistant"
    message: str
