from PIL import Image
from fastapi import UploadFile


class ImageValidationError(Exception):
    pass


def validate_image(file: UploadFile):
    check_mime(file)
    verify_image_content(file)


def check_mime(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise ImageValidationError("Invalid file. It must be an image.")


def verify_image_content(file: UploadFile):
    try:
        Image.open(file.file).verify()
    except Exception:
        raise ImageValidationError("Invalid or corrupted image file.")
    finally:
        file.file.seek(0)  # Reset file pointer regardless of success or failure
