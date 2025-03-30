from fastapi import FastAPI
import pickle
import pandas as pd
import os
from src.data_model import Medical


app = FastAPI(
    title = "Medical Cost Predictor",
    description = "Predicting your Medical Cost "
)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return "Welcome to Medical Cost Predictor FastAPI"

@app.post("/predict")
def model_predict(medical:Medical):
    sample=pd.DataFrame({
        "age":[medical.age],
        "bmi":[medical.bmi],
        "children":[medical.children],
        "sex_female": [medical.sex_female],
        "sex_male": [medical.sex_male],
        "smoker_no": [medical.smoker_no],
        "smoker_yes": [medical.smoker_yes],
        "region_northeast": [medical.region_northeast],
        "region_northwest": [medical.region_northwest],
        "region_southeast": [medical.region_southeast],
        "region_southwest": [medical.region_southwest],
    })
    
    pred_value=model.predict(sample)

    return {"predicted_cost": float(pred_value[0])}


