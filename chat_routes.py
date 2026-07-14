"""
Project : Real-Time AI Chat (MVP)
File    : chat_routes.py

Protected Chat APIs
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user
from crud import (
    create_chat,
    get_chat,
    get_user_chats,
    get_chat_messages,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
)
def create_new_chat(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    chat = create_chat(
        db=db,
        user_id=current_user.id,
    )

    return {
        "success": True,
        "chat_id": chat.id,
        "title": chat.title,
    }


@router.get("/")
def get_my_chats(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    chats = get_user_chats(
        db=db,
        user_id=current_user.id,
    )

    return chats


@router.get("/{chat_id}")
def get_chat_history(
    chat_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    chat = get_chat(
        db=db,
        chat_id=chat_id,
    )

    if chat is None:
        raise HTTPException(
            status_code=404,
            detail="Chat not found.",
        )

    if chat.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Permission denied.",
        )

    messages = get_chat_messages(
        db=db,
        chat_id=chat.id,
    )

    return {
        "chat_id": chat.id,
        "title": chat.title,
        "messages": messages,
    }
