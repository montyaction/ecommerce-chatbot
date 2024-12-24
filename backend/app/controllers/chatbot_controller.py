# backend/app/controllers/chatbot_controller.py
from fastapi import APIRouter, Depends, HTTPException, Request, logger
from typing import List
from app.models.product_model import Product
from app.services.chatbot_service import ChatbotService
from app import oauth2_scheme
from app.core.limiter import limiter

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat")
@limiter.limit("20/minute")
async def chat_endpoint(
    request: Request,
    message: str,
    token: str = Depends(oauth2_scheme)
):
    try:
        response = await chatbot_service.process_message(token, message)
        return {"response": response}
    except Exception as e:
        logger.exception(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail="Error processing message")

@router.get("/products")
@limiter.limit("100/minute")
async def get_products(
    request: Request,
    token: str = Depends(oauth2_scheme)
) -> List[Product]:
    try:
        # return await chatbot_service.get_product_recommendations(token)
        return []
    except Exception as e:
        logger.exception(f"Error getting products: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving products")