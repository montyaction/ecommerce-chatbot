# backend/app/middleware/error_handlers.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from typing import Union
from app.core.limiter import limiter    # Updated import

def setup_error_handlers(app: FastAPI):
    """Configure global error handlers"""
    app.state.limiter = limiter    # Set up rate limiter

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ) -> JSONResponse:
        """Handle all unhandled exceptions"""
        error_msg = f"An error occurred: {str(exc)}"
        return JSONResponse(
            status_code=500,
            content={
                "error": error_msg,
                "path": request.url.path
            }
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException
    ) -> JSONResponse:
        """Handle HTTP exceptions"""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.detail,
                "path": request.url.path
            }
        )

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit_handler(
        request: Request,
        exc: RateLimitExceeded
    ) -> Union[JSONResponse, None]:
        """Handle rate limit exceeded errors"""
        return _rate_limit_exceeded_handler(request, exc)