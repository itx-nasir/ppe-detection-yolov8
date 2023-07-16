from ultralytics import YOLO
from .utils import read_image
import numpy as np

# Model cache to avoid reloading
model_cache = {}

def get_model(model_version: str):
    """Load and cache YOLO model"""
    
    if model_version not in model_cache:
        model_path = f"./models/{model_version}/ppe_detector.pt"
        model_cache[model_version] = YOLO(model_path)
    else:
        pass
    
    return model_cache[model_version]

def predict(image: np.ndarray, conf: float = 0.5, model_version: str = "v1"):
    """
    Run YOLOv8 prediction on an image
    Returns annotated image, bounding boxes, and class IDs
    """
    
    model = get_model(model_version)
    
    results = model.predict(source=image, conf=conf, save=False)
    
    annotated_image = results[0].plot()  # annotated numpy image
    boxes = results[0].boxes.xyxy        # bounding box coordinates
    classes = results[0].boxes.cls       # class IDs
    
    return annotated_image, boxes, classes
