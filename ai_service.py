"""
Project : Real-Time AI Chat (MVP)
File    : ai_service.py
Part    : 1/2

Google Gemini AI Service
"""

from typing import List

import google.generativeai as genai

from config import settings


# ==========================================================
# Configure Gemini
# ==========================================================

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

MODEL_NAME = "gemini-1.5-flash"

model = genai.GenerativeModel(
    model_name=MODEL_NAME
)


# ==========================================================
# Build Conversation History
# ==========================================================

def build_history(
    messages: List,
) -> list:

    history = []

    for message in messages:

        role = "user"

        if message.role == "assistant":
            role = "model"

        history.append(
            {
                "role": role,
                "parts": [
                    message.content
                ],
            }
        )

    return history


# ==========================================================
# Start Chat Session
# ==========================================================

def create_chat_session(
    previous_messages: List,
    
):

    history = build_history(
        previous_messages
    )

    
    return model.start_chat(
        history=history
    )
# ==========================================================
# Generate AI Response
# ==========================================================

def generate_ai_response(
    prompt: str,
    previous_messages: List,
) -> str:
    """
    Generate a response from Google Gemini AI.
    """

    try:

        chat = create_chat_session(
            previous_messages=previous_messages
        )

        response = chat.send_message(
            prompt
        )

        if response is None:
            return (
                "Sorry, I couldn't generate a response."
            )

        if not hasattr(response, "text"):
            return (
                "Sorry, I couldn't understand the AI response."
            )

        ai_text = response.text.strip()

        if not ai_text:
            return (
                "Sorry, I couldn't generate a response."
            )

        return ai_text

    except Exception as exc:

        print(
            f"[Gemini Error] {exc}"
        )

        return safe_fallback_response()


# ==========================================================
# Safe Fallback Response
# ==========================================================

def safe_fallback_response() -> str:
    """
    Return a safe fallback response whenever
    Gemini API is unavailable.
    """

    return (
        "I'm sorry, but the AI service is currently "
        "unavailable. Please try again in a few moments."
    )


# ==========================================================
# AI Health Check
# ==========================================================

def check_ai_connection() -> bool:
    """
    Check whether Gemini API is reachable.
    """

    try:

        model.generate_content(
            "Hello"
        )

        return True

    except Exception:

        return False
