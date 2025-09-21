import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class Settings:
    # Database
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "resume_user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "resume_db")
    DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

    # Application
    APP_SECRET_KEY: str = os.getenv("APP_SECRET_KEY", "change-this-in-production")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "False").lower() == "true"
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))

    # Security
    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "").split(",")
    DOMAIN_NAME: str = os.getenv("DOMAIN_NAME", "localhost")

    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 60

settings = Settings()