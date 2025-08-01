from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

router = APIRouter()

# Load the trained expiry predictor model
model = joblib.load("expiry_predictor.pkl")

# Define the expected input format (matches training features)
class ExpiryInput(BaseModel):
    hemoglobin: float       # corresponds to 'hemoglobin_g_dl'
    volume: float           # corresponds to 'collection_volume_ml'
    donor_age: int

@router.post("/predict_expiry")
def predict_expiry(data: ExpiryInput):
    try:
        # Create feature array in the same order as training
        features = np.array([
            data.hemoglobin,
            data.volume,
            data.donor_age
        ]).reshape(1, -1)

        # Predict shelf life
        prediction = model.predict(features)

        return {"predicted_shelf_life_days": round(float(prediction[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
