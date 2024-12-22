from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from slowapi import Limiter
from slowapi.util import get_remote_address

# Initialze FastAPI app
app = FastAPI(title="E-commerce Sales Chatbot API")

# Initialze core components
limiter = Limiter(key_func=get_remote_address)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Import and setup middleware
from app.middleware.cors import setup_cors
from app.middleware.error_handlers import setup_error_handlers

# Setup middleware
setup_cors(app)
setup_error_handlers(app)
