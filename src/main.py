from fastapi import FastAPI

from src.middleware.error_handling import get_error_handling_middleware
from src.routers import classification

app = FastAPI()
get_error_handling_middleware(app)
app.include_router(classification.router, prefix="/classify", tags=["Classification"])
