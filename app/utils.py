import cv2
import numpy as np
from fastapi import UploadFile

async def read_image(file: UploadFile) -> np.ndarray:
    """
    Read uploaded file as cv2 image (numpy array)
    """
    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def encode_image(image: np.ndarray) -> bytes:
    """
    Encode cv2 image to JPEG bytes for FastAPI response
    """
    _, img_encoded = cv2.imencode(".jpg", image)
    return img_encoded.tobytes()
