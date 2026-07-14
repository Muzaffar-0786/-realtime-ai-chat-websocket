"""
Project : Real-Time AI Chat (MVP)
File    : database.py

Database configuration and session management.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


# --------------------------------------------------
# Database Engine
# --------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
    if settings.DATABASE_URL.startswith("sqlite")
    else {},
    pool_pre_ping=True,
)


# --------------------------------------------------
# Session Factory
# --------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# --------------------------------------------------
# Base Model
# --------------------------------------------------

Base = declarative_base()


# --------------------------------------------------
# Dependency
# --------------------------------------------------

def get_db():
    """
    FastAPI dependency for database session.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------------------------
# Create Tables
# --------------------------------------------------

def create_tables():
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)
