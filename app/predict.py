from ultralytics import YOLO
from .utils import read_image
import numpy as np

# Model cache to avoid reloading
model_cache = {}

def get_model(model_version: str):
    """Load and cache YOLO model"""
    print(f"DEBUG: get_model called with model_version: '{model_version}'")  # Debug log
    
    if model_version not in model_cache:
        model_path = f"./models/{model_version}/ppe_detector.pt"
        print(f"DEBUG: Loading new model from: {model_path}")  # Debug log
        model_cache[model_version] = YOLO(model_path)
        print(f"DEBUG: Model loaded and cached for version: {model_version}")  # Debug log
    else:
        print(f"DEBUG: Using cached model for version: {model_version}")  # Debug log
    
    return model_cache[model_version]

def predict(image: np.ndarray, conf: float = 0.5, model_version: str = "v1"):
    """
    Run YOLOv8 prediction on an image
    Returns annotated image, bounding boxes, and class IDs
    """
    print(f"DEBUG: predict called with model_version: '{model_version}', conf: {conf}")  # Debug log
    
    model = get_model(model_version)
    print(f"DEBUG: Using model object: {type(model)}")  # Debug log
    
    results = model.predict(source=image, conf=conf, save=False)
    print(f"DEBUG: Prediction completed. Found {len(results[0].boxes)} detections")  # Debug log
    
    annotated_image = results[0].plot()  # annotated numpy image
    boxes = results[0].boxes.xyxy        # bounding box coordinates
    classes = results[0].boxes.cls       # class IDs
    
    print(f"DEBUG: Classes detected: {classes.tolist() if len(classes) > 0 else 'None'}")  # Debug log
    
    return annotated_image, boxes, classes
