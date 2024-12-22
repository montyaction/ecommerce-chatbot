import uvicorn
from app import app
from app.controllers import auth_controller, chatbot_controller

app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
app.include_router(chatbot_controller.router, prefix="/api", tags=["chatbot"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)