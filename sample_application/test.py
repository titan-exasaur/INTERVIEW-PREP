import numpy as np
import pandas as pd

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,3,4,5,6]).reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
lr_model.fit(x,y)

import joblib
joblib.dump(lr_model, "model.pkl")