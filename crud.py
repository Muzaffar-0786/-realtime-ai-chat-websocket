"""
Project : Real-Time AI Chat (MVP)
File    : crud.py

Database CRUD operations.
"""

from typing import Optional

from sqlalchemy.orm import Session

from auth import hash_password, verify_password
from models import User, Chat, Message


# ==========================================================
# User
# ==========================================================

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def create_user(
    db: Session,
    username: str,
    email: str,
    password: str,
) -> User:

    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> Optional[User]:

    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


# ==========================================================
# Chat
# ==========================================================

def create_chat(
    db: Session,
    user_id: int,
    title: str = "New Chat",
) -> Chat:

    chat = Chat(
        user_id=user_id,
        title=title,
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat(
    db: Session,
    chat_id: int,
) -> Optional[Chat]:

    return db.query(Chat).filter(Chat.id == chat_id).first()


def get_user_chats(
    db: Session,
    user_id: int,
):

    return (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.created_at.desc())
        .all()
    )


# ==========================================================
# Message
# ==========================================================

def save_message(
    db: Session,
    chat_id: int,
    role: str,
    content: str,
) -> Message:

    message = Message(
        chat_id=chat_id,
        role=role,
        content=content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


def get_chat_messages(
    db: Session,
    chat_id: int,
):

    return (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
        .all()
    )
