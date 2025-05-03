from fastapi.testclient import TestClient
from ml_interview_project.main import app

client = TestClient(app)

def test_predict_positive():
    payload = {"text": "excellent quality and service"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_negative():
    payload = {"text": "terrible product, very disappointing"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()