import numpy as np
import pandas as pd
import os
import pickle
import json
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    explained_variance_score
)

test_df=pd.read_csv("data/preprocessed/test_preprocessed.csv")

X_test = test_df.drop(columns=["charges"]).values  
y_test = test_df["charges"].values     

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


y_pred=model.predict(X_test)


metrics = {
    "MAE": mean_absolute_error(y_test, y_pred),
    "MSE": mean_squared_error(y_test, y_pred),
    "RMSE": mean_squared_error(y_test, y_pred),
    "R2": r2_score(y_test, y_pred),
    "Explained Variance": explained_variance_score(y_test, y_pred)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)