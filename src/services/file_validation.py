from PIL import Image
from fastapi import UploadFile, HTTPException


def validate_image(file: UploadFile):
    """
    Validates if the uploaded file is a valid image by checking MIME type and file integrity.
    Raises HTTPException if validation fails.
    """
    check_mime(file)
    verify_image_content(file)


def check_mime(file: UploadFile):
    """
    Checks if the uploaded file's MIME type indicates it's an image.
    Raises HTTPException if the check fails.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, detail="Invalid file. It must be an image."
        )


def verify_image_content(file: UploadFile):
    """
    Verifies that the content of the uploaded file is a valid image using PIL's verify().
    Resets the file pointer after the check to allow further processing.
    Raises HTTPException if the image check fails.
    """
    try:
        Image.open(file.file).verify()
    except Exception:
        raise HTTPException(
            status_code=400, detail="Invalid or corrupted image file."
        )
    finally:
        file.file.seek(0)  # Reset the file pointer in all cases
