import joblib
import pandas as pd


model = joblib.load("model.pkl")


for distance in [1,5,10,50]:

    data = pd.DataFrame([{

        "passenger_count":1,
        "hour":19,
        "day":7,
        "month":5,
        "distance":distance

    }])


    print(
        distance,
        model.predict(data)
    )