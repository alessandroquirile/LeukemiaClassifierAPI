from fastapi import FastAPI

from src.routers import classification

app = FastAPI()
app.include_router(classification.router, prefix="/classify", tags=["Classification"])
