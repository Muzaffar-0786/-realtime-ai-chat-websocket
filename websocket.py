"""
Project : Real-Time AI Chat (MVP)
File    : websocket.py

Real-time WebSocket Chat
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session

from database import SessionLocal
from crud import (
    get_chat,
    get_chat_messages,
    save_message,
)
from ai_service import generate_ai_response


router = APIRouter()


class ConnectionManager:

    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket,
    ):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(
        self,
        websocket: WebSocket,
    ):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_json(
        self,
        websocket: WebSocket,
        data: dict,
    ):
        await websocket.send_json(data)


manager = ConnectionManager()


@router.websocket("/ws/chat/{chat_id}")
async def websocket_chat(
    websocket: WebSocket,
    chat_id: int,
):

    await manager.connect(websocket)

    db: Session = SessionLocal()

    try:

        chat = get_chat(db, chat_id)

        if chat is None:
            await manager.send_json(
                websocket,
                {
                    "success": False,
                    "message": "Chat not found."
                }
            )
            return

        while True:

            data = await websocket.receive_json()

            user_message = data.get("message", "").strip()

            if not user_message:
                continue

            # Save User Message
            save_message(
                db=db,
                chat_id=chat_id,
                role="user",
                content=user_message,
            )

            # Fetch Updated History
            history = get_chat_messages(
                db=db,
                chat_id=chat_id,
            )

            # AI Response
            ai_reply = generate_ai_response(
                prompt=user_message,
                previous_messages=history,
            )

            # Save AI Message
            save_message(
                db=db,
                chat_id=chat_id,
                role="assistant",
                content=ai_reply,
            )

            # Send Response
            await manager.send_json(
                websocket,
                {
                    "success": True,
                    "role": "assistant",
                    "message": ai_reply,
                }
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)

    except Exception as exc:

        await manager.send_json(
            websocket,
            {
                "success": False,
                "message": str(exc),
            }
        )

    finally:

        db.close()
