"""
Project : Real-Time AI Chat (MVP)
File    : ai_service.py

Google Gemini AI Service
"""

from typing import List, Dict

import google.generativeai as genai

from config import settings


# ---------------------------------------------------------
# Configure Gemini
# ---------------------------------------------------------

genai.configure(api_key=settings.GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)


# ---------------------------------------------------------
# Convert Database Messages
# ---------------------------------------------------------

def build_history(messages: List) -> List[Dict]:
    """
    Convert database messages into Gemini history format.
    """

    history = []

    for message in messages:

        role = "user"

        if message.role == "assistant":
            role = "model"

        history.append(
            {
                "role": role,
                "parts": [message.content],
            }
        )

    return history


# ---------------------------------------------------------
# Generate AI Response
# ---------------------------------------------------------

def generate_ai_response(
    prompt: str,
    previous_messages: List,
) -> str:
    """
    Generate AI response using Gemini.
    """

    try:

        history = build_history(previous_messages)

        chat = model.start_chat(
            history=history
        )

        response = chat.send_message(prompt)

        if response.text:
            return response.text.strip()

        return "Sorry, I couldn't generate a response."

    except Exception as exc:

        print(f"Gemini Error: {exc}")

        return (
            "AI service is temporarily unavailable. "
            "Please try again later."
        )
