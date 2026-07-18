import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import joblib



# Load processed data

data = pd.read_csv("processed_dataset.csv")
data = data[
    (data["distance"] > 0) &
    (data["distance"] < 100) &
    (data["fare_amount"] > 0)
]


# Features

X = data[
    [
        "passenger_count",
        "distance"
    ]
]


# Target

y = data["fare_amount"]



# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Model

model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    random_state=42
)



# Train

model.fit(
    X_train,
    y_train
)



# Prediction

predictions = model.predict(X_test)



# Evaluation

print(
    "MAE:",
    mean_absolute_error(y_test,predictions)
)



rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

print(
    "RMSE:",
    rmse
)


print(
    "R2 Score:",
    r2_score(
        y_test,
        predictions
    )
)



# Save model

joblib.dump(
    model,
    "model.pkl"
)


print("Model saved successfully!")