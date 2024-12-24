# backend/app/controllers/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException, Request, logger, status
from app.models.auth_model import UserAuth, UserCreate, Token
from app.services.auth_service import AuthService
from app.core.limiter import limiter
from app import oauth2_scheme

router = APIRouter()
auth_service = AuthService()

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def register(request: Request, user_data: UserCreate):
    try:
        await auth_service.register_user(user_data)
        return await auth_service.authenticate_user(UserAuth(email=user_data.email, password=user_data.password))
    except HTTPException as e:
        raise e  # Re-raise HTTPExceptions
    except Exception as e:
        logger.exception(f"Error during registration: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Registration failed")

@router.post("/token", response_model=Token)
@limiter.limit("5/minute")
async def login(request: Request, user_data: UserAuth):
    try:
        return await auth_service.authenticate_user(user_data)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception(f"Error during login: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Login failed")

@router.get("/verify")
async def verify_token(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid", "token": token}

# Optional: Add a user info endpoint
@router.get("/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = await auth_service.get_user_from_token(token)
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception(f"Error getting current user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not retrieve user")