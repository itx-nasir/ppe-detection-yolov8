# PPE Detection using YOLOv8

## Overview
This project is a **Personal Protective Equipment (PPE) detection system** built using **YOLOv8** and deployed via **FastAPI**.  
It detects construction site safety equipment such as **helmets**, **heads**, and **persons** in real-time images.

The project is **versioned**, allowing multiple iterations of the model to be deployed and compared (v1, v2, v3, ...).

---

## Features

- **Object Detection**: Detects helmets, heads, and persons.
- **Real-time API**: Deploys a FastAPI service that accepts images and returns annotated images.
- **Model Versioning**: Supports multiple versions of the model for A/B testing and improvement.
- **Data Preprocessing & Training**: Fine-tuned on a PPE dataset for construction safety.

---

## Folder Structure

```
ppe-detection-yolov8/
├── Dockerfile
├── README.md
├── requirements.txt
├── app/
│   ├── main.py          # FastAPI application
│   ├── predict.py       # YOLO prediction logic
│   └── utils.py         # Utility functions for image processing
└── models/
    ├── v1/
    │   └── helmet_detector.pt  # Trained YOLO model
    ├── v2/
    └── v3/
```

---

## Installation and Running

### Option 1: Running Locally with Virtual Environment

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/itx-nasir/ppe-detection-yolov8.git
   cd ppe-detection-yolov8
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**:
   - Open your browser and go to `http://127.0.0.1:8000`
   - API documentation available at `http://127.0.0.1:8000/docs`

### Option 2: Running with Docker

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/itx-nasir/ppe-detection-yolov8.git
   cd ppe-detection-yolov8
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t ppe-detection .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 ppe-detection
   ```

4. **Access the API**:
   - Open your browser and go to `http://127.0.0.1:8000`
   - API documentation available at `http://127.0.0.1:8000/docs`

---

## API Usage

- **GET /**: Home endpoint
- **POST /predict/**: Upload an image and get the annotated image with detections
  - Parameters:
    - `file`: Image file (JPEG/PNG)
    - `conf`: Confidence threshold (default 0.5)

Example using curl:
```bash
curl -X POST "http://127.0.0.1:8000/predict/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@image.jpg"
```

---

## Model Versioning

To use a different model version, update `MODEL_VERSION` in `app/predict.py` to "v2" or "v3" and ensure the corresponding model file exists in `models/vX/`.

---

## Contributing

Feel free to contribute by training new models or improving the detection accuracy.

