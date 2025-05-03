from fastapi import FastAPI, Body
from ml_interview_project.inference import load_model, predict_text

app = FastAPI()

@app.post("/predict")
def predict(payload: dict = Body(...)):
    text = payload.get("text")
    model = load_model()
    return {
        "prediction": predict_text(text, model)
    }