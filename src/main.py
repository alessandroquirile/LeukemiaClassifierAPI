from fastapi import FastAPI

from src.routers import classify

app = FastAPI()
app.include_router(classify.router, prefix="/classify", tags=["Classification"])
