"""
Project : Real-Time AI Chat (MVP)
File    : config.py

Application configuration using Pydantic Settings.
Loads values from .env file.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    # -------------------------
    # Project Information
    # -------------------------
    PROJECT_NAME: str = "Real-Time AI Chat API"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"

    # -------------------------
    # Security
    # -------------------------
    SECRET_KEY: str = Field(default="MySuperChatSecretKey786LongEnough", min_length=32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # -------------------------
    # Database
    # -------------------------
    DATABASE_URL: str = "sqlite:///./test.db"

    # -------------------------
    # Gemini AI
    # -------------------------
    GEMINI_API_KEY: str = ""

    # -------------------------
    # CORS
    # -------------------------
    ALLOWED_ORIGINS: list[str] = [
        "*"
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached settings instance.
    """
    return Settings()


settings = get_settings()
