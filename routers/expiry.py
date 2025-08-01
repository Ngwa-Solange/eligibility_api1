from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

router = APIRouter()

# Load model
model = joblib.load("expiry_predictor.pkl")

class ExpiryInput(BaseModel):
    blood_type: str
    donation_volume: float
    temperature: float
    location: str
    donor_age: int

@router.post("/predict_expiry")
def predict_expiry(data: ExpiryInput):
    try:
        # Sample input transformation
        features = np.array([
            data.donor_age,
            data.donation_volume,
            data.temperature
        ]).reshape(1, -1)

        prediction = model.predict(features)
        return {"predicted_shelf_life_days": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
