# app/controllers/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from app.models.auth_model import UserAuth, UserCreate, Token
from app.services.auth_service import AuthService
from app import limiter

router = APIRouter()
auth_service = AuthService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def register(request: Request, user_data: UserCreate):
    # We don't need to store the user separately since authenticate_user will handle it
    await auth_service.register_user(user_data)
    return await auth_service.authenticate_user(
        UserAuth(email=user_data.email, password=user_data.password)
    )

@router.post("/token", response_model=Token)
@limiter.limit("5/minute")
async def login(request: Request, user_data: UserAuth):
    # Use the request parameter for rate limiting
    client_host = request.client.host if request.client else "unknown"
    # You could log the login attempt here
    print(f"Login attempt from {client_host}")  # Replace with proper logging
    
    return await auth_service.authenticate_user(user_data)

@router.get("/verify")
async def verify_token(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid", "token": token}

# Optional: Add a user info endpoint
@router.get("/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # You might want to decode the token and return user information
    try:
        # You'll need to implement get_user_from_token in auth_service
        user = await auth_service.get_user_from_token(token)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )