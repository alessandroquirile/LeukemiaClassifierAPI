import logging
from fastapi import Request


from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from src.services.file_validation import ImageValidationError

logger = logging.getLogger("uvicorn.error")


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ImageValidationError as e:
            return JSONResponse(
                status_code=400,
                content={"detail": str(e)},
            )
        except Exception:
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"},
            )


def add_error_handling_middleware(app):
    app.add_middleware(ErrorHandlingMiddleware)
