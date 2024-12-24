# backend/app/config/setting.py
from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # Base configuration
    PROJECT_NAME: str = "E-commerce Chatbot"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # CORS configuration (if applicable)
    BACKEND_CORS_ORIGINS: List[str] = ["*"]     # Adjust allowed origin

    # Add the missing settings
    SECRET_KEY: str = "your-secret-key"  # Replace with a strong secret
    ALGORITHM: str = "HS256"  # Provide a default value if appropriate
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15 # Type hint as int
    DATABASE_URL: str
    DEBUG: bool = False # Type hint as bool
    API_KEY_EXTERNAL_SERVICE: Optional[str] = None # Optional field
    AUTH_SERVICE_PORT: int = 5001
    PRODUCT_SERVICE_PORT: int = 5002
    CHATBOT_SERVICE_PORT: int = 5003
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()