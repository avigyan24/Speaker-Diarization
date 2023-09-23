from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
 # Assuming you have a function for this
from app.model.model import __version__ as model_version
from app.model.model import predict_pipeline

app = FastAPI()








@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    # Assuming you have a function to process the WAV file and generate RTTM text
    rttm_text = predict_pipeline(file.file)
     
    return rttm_text