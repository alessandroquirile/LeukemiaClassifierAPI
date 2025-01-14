from PIL import Image
from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.services.classification import ClassificationService
from src.services.file_validation import validate_image

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
service = ClassificationService("config.yaml")


@router.post("")
@limiter.limit("10/minute")
async def classify_image(request: Request, file: UploadFile = File(...)):
    validate_image(file)
    image = Image.open(file.file)
    prediction = service.classify(image)
    return JSONResponse({"prediction": prediction})
