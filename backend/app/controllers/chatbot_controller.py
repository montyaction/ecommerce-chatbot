from fastapi import APIRouter, Depends, Request
from typing import List
from backend.app.models.product_model import Product
from app.services.chatbot_service import ChatbotService
from app import limiter, oauth2_scheme

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat")
@limiter.limit("20/minute")
async def chat_endpoint(
    request: Request,
    message: str,
    token: str = Depends(oauth2_scheme)
):
    # Add your chatbot logic here
    response = await chatbot_service.process_message(token, message)
    return {"response": response}

@router.get("/products")
@limiter.limit("100/minute")
async def get_products(
    request: Request,
    token: str = Depends(oauth2_scheme)
) -> List[Product]:
    # Add your product retrieval logic here
    return []