from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .predict import predict
from .utils import read_image, encode_image
import io

app = FastAPI(title="PPE Helmet Detection API v1")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict_endpoint(file: UploadFile = File(...), conf: float = Form(0.5), model: str = Form("v1")):
    """
    Accept an uploaded image and return annotated image with detected PPE
    """
    
    # Read image
    image = await read_image(file)
    
    # Run prediction
    annotated_image, boxes, classes = predict(image, conf, model)
    
    # Encode image as JPEG for response
    img_bytes = encode_image(annotated_image)
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/jpeg")
