import pickle
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

# ensure Artifacts directory exists
os.makedirs("Artifacts", exist_ok=True)

# dummy input matching form fields
X_dummy = pd.DataFrame({
    "airline": ["Indigo"],
    "source_city": ["Delhi"],
    "departure_time": ["Morning"],
    "stops": ["zero"],
    "arrival_time": ["Night"],
    "destination_city": ["Mumbai"],
    "classs": ["Economy"],
    "duration": [2.5],
    "days_left": [10]
})

# correct for sklearn >= 1.2
preprocessor = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
X_transformed = preprocessor.fit_transform(X_dummy)

# dummy model trained on SAME feature count
model = LinearRegression()
y_dummy = np.array([5000])
model.fit(X_transformed, y_dummy)

# save artifacts
with open("Artifacts/Preprocessor.pkl", "wb") as f:
    pickle.dump(preprocessor, f)

with open("Artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

print(f"✅ Dummy artifacts created with {X_transformed.shape[1]} features")
