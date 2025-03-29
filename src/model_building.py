import numpy as np
import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestRegressor

train_df = pd.read_csv("data/preprocessed/train_preprocessed.csv")
test_df = pd.read_csv("data/preprocessed/test_preprocessed.csv")

X_train=train_df.iloc[:,0:-1].values
Y_train=train_df.iloc[:,-1].values


model=RandomForestRegressor()

model.fit(X_train,Y_train)
pickle.dump(model,open("model.pkl","wb"))
