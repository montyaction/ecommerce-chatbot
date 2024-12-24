# backend/main.py
from app import app
from uvicorn import run
from fastapi import HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from app.controllers import auth_controller, chatbot_controller

# Include routers with prefixes and tags
app.include_router(
    auth_controller.router, prefix="/auth", tags=["auth"]
)
app.include_router(
    chatbot_controller.router, prefix="/api/v1", tags=["chatbot"]
)

# @app.route("/")
# def home():
#     return "<h1>Welcome to the Home page!</h1>"

# @app.route("/about")
# def about():
#     return "<h1>About Us</h1><p>This is the about page of our Flask application.</p>"

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(HTTPException, _rate_limit_exceeded_handler)

# Run the Uvicorn server
if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)