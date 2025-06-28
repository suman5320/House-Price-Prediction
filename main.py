from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd

app = FastAPI()

# Load the pipeline model
with open("model/xgb_model_pipeline.pkl", "rb") as f:
    model_pipeline = pickle.load(f)

# Define input format using Pydantic
class HouseFeatures(BaseModel):
    OverallQual: int
    GrLivArea: float
    GarageCars: int
    TotalBsmtSF: float
    FullBath: int
    YearBuilt: int

@app.post("/predict")
def predict_price(data: HouseFeatures):
    # Create input DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Make prediction
    prediction = model_pipeline.predict(input_df)[0]
    
    return {
        "predicted_price": round(prediction, 2)
    }
