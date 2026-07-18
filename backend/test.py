import joblib
import pandas as pd


model = joblib.load("model.pkl")


ride = pd.DataFrame([
    {
        "distance":10,
        "time":30,
        "traffic":"medium",
        "vehicle":"sedan"
    }
])


prediction = model.predict(ride)


print(prediction)