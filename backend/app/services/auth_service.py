# app/services/auth_service.py
from typing import Optional
from datetime import timedelta
from fastapi import HTTPException, logger, status
from app.models.user_model import User
from app.models.auth_model import UserAuth, UserCreate, Token
from app.utils.security import hash_password, verify_password, create_access_token
from app.config.auth_config import auth_config

class AuthService:
    def __init__(self):
        self.users = {}  # Replace with database in production

    async def register_user(self, user_data: UserCreate) -> User:
        if user_data.email in self.users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        hashed_password = hash_password(user_data.password)
        user = User(
            username=user_data.username,
            email=user_data.email,
            full_name=user_data.full_name
        )
        
        self.users[user.email] = {
            "username": user.username,
            "password": hashed_password,
            "full_name": user.full_name
        }
        
        return user

    async def authenticate_user(self, user_data: UserAuth) -> Optional[Token]:
        user = self.users.get(user_data.email)
        if not user or not verify_password(user_data.password, user["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user["username"]},
            expires_delta=access_token_expires
        )
        
        return Token(
            access_token=access_token,
            token_type="bearer"
        )
    
    async def get_user_from_token(self, token: str):
        # Implement token verification and user retrieval here
        # Example using JWT decoding (you'll need to install pyjwt)
        import jwt
        try:
            payload = jwt.decode(token, auth_config.SECRET_KEY, algorithms=[auth_config.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token")
            #Get user from database here
            user = self.users.get(username) #replace with database query
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            logger.exception(f"Error getting user from token: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")