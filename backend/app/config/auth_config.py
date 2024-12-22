from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    SECRET_KEY: str = "your-secret-key"  # In production, use environment variable
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    
    class Config:
        env_file = ".env"

auth_config = AuthConfig()