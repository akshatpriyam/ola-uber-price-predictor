from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pandas as pd
import joblib


app = FastAPI()


# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load trained model
model = joblib.load("model.pkl")


print("Model expects:", model.feature_names_in_)



# Input format
class RideData(BaseModel):

    distance: float

    passenger_count: int




@app.get("/")
def home():

    return {
        "message": "Uber Fare Estimator API Running"
    }




@app.post("/predict")
def predict_fare(data: RideData):


    # Create dataframe with EXACT training order

    input_data = pd.DataFrame([{

        "passenger_count": data.passenger_count,

        "distance": data.distance

    }])


    print("Input received:")

    print(input_data)



    # Prediction

    prediction = model.predict(input_data)


    print("Model prediction:")

    print(prediction)



    # Convert USD to INR

    fare = float(prediction[0])


    fare = max(0, fare * 83)



    return {

        "estimated_fare": round(fare, 2),

        "currency": "INR"

    }