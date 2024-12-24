# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2PasswordBearer
# from slowapi import Limiter
# from slowapi.util import get_remote_address
# import logging
# from app.config.settings import settings

# # Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)
# logger.info("Application starting...")

# # Initialize FastAPI app
# app = FastAPI(
#     title=settings.PROJECT_NAME,
#     version=settings.VERSION,
# )

# # Initialize limiter
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter

# # Initialize OAuth2
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Import and setup middleware
# from app.middleware.cors import setup_cors
# from app.middleware.error_handlers import setup_error_handlers

# # Setup middleware
# setup_cors(app)
# setup_error_handlers(app)

# # Export the limiter instance
# __all__ = ['app', 'limiter', 'oauth2_scheme']

# print("Limiter initialized:", hasattr(app.state, 'limiter'))