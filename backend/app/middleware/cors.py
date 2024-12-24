# backend/app/middleware/cors.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from config import settings

def setup_cors(app: FastAPI):
    """Configure CORS middleware"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )