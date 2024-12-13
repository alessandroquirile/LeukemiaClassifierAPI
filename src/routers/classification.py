from PIL import Image
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from src.services.classification import ClassificationService

router = APIRouter()
service = ClassificationService()


@router.post("")
async def classify_image(file: UploadFile = File(...)):
    image = Image.open(file.file)
    prediction = service.classify(image)
    return JSONResponse({"prediction": prediction})
