# backend/app/config/auth_config.py
from pydantic_settings import BaseSettings
from typing import Optional

class AuthConfig(BaseSettings):
    SECRET_KEY: str = "your-secret-key"  # Replace with a strong secret
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    DATABASE_URL: Optional[str] = None  # Database connection string (if applicable)
    DEBUG: bool = True
    API_KEY_EXTERNAL_SERVICE: Optional[str] = None  # External service API key
    AUTH_SERVICE_PORT: int = 5001
    PRODUCT_SERVICE_PORT: int = 5002
    CHATBOT_SERVICE_PORT: int = 5003

    class Config:
        env_file = ".env"
        case_sensitive = False

auth_config = AuthConfig()