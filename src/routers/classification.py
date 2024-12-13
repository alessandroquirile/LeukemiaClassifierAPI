from PIL import Image
from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.services.classification import ClassificationService

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
service = ClassificationService()


@router.post("")
@limiter.limit("10/minute")
async def classify_image(request: Request, file: UploadFile = File(...)):
    image = Image.open(file.file)
    prediction = service.classify(image)
    prediction = bool(prediction)  # Convert numpy.bool_ to native Python bool
    return JSONResponse({"prediction": prediction})
