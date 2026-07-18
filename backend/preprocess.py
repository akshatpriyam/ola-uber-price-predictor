import pandas as pd
import numpy as np


# Load dataset
data = pd.read_csv("dataset.csv")

# Remove missing values
data = data.dropna()


# Remove wrong coordinates
data = data[
    (data.pickup_longitude.between(-180,180)) &
    (data.dropoff_longitude.between(-180,180)) &
    (data.pickup_latitude.between(-90,90)) &
    (data.dropoff_latitude.between(-90,90))
]


# Convert datetime
data["pickup_datetime"] = pd.to_datetime(data["pickup_datetime"])


# Extract time features
data["hour"] = data["pickup_datetime"].dt.hour
data["day"] = data["pickup_datetime"].dt.day
data["month"] = data["pickup_datetime"].dt.month
data = data.drop("Unnamed: 0", axis=1)


# Haversine distance calculation

def haversine(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius km

    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)

    lon1 = np.radians(lon1)
    lon2 = np.radians(lon2)


    dlat = lat2 - lat1
    dlon = lon2 - lon1


    a = (
        np.sin(dlat/2)**2 +
        np.cos(lat1) *
        np.cos(lat2) *
        np.sin(dlon/2)**2
    )


    c = 2*np.arcsin(np.sqrt(a))

    return R*c



data["distance"] = haversine(
    data["pickup_latitude"],
    data["pickup_longitude"],
    data["dropoff_latitude"],
    data["dropoff_longitude"]
)



# Remove unnecessary columns

data = data.drop(
    [
        "key",
        "pickup_datetime",
        "pickup_latitude",
        "pickup_longitude",
        "dropoff_latitude",
        "dropoff_longitude"
    ],
    axis=1
)


# Remove unrealistic fares

data = data[
    (data.fare_amount > 0) &
    (data.distance > 0)
]

# Remove unwanted index column if present

if "Unnamed: 0" in data.columns:
    data = data.drop("Unnamed: 0", axis=1)

    
# Save processed data

data.to_csv(
    "processed_dataset.csv",
    index=False
)


print(data.head())

print("\nFinal shape:")
print(data.shape)

