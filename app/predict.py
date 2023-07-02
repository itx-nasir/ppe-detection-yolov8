from ultralytics import YOLO
from .utils import read_image
import numpy as np

# Model version
MODEL_VERSION = "v1"
MODEL_PATH = f"./models/{MODEL_VERSION}/helmet_detector.pt"

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

def predict(image: np.ndarray, conf: float = 0.5):
    """
    Run YOLOv8 prediction on an image
    Returns annotated image, bounding boxes, and class IDs
    """
    results = model.predict(source=image, conf=conf, save=False)
    annotated_image = results[0].plot()  # annotated numpy image
    boxes = results[0].boxes.xyxy        # bounding box coordinates
    classes = results[0].boxes.cls       # class IDs
    return annotated_image, boxes, classes
