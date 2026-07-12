import joblib
import pandas as pd

# Load model only once
model = joblib.load("models/house_price_model_v2.pkl")


def predict_price(
    overall_qual,
    gr_liv_area,
    garage_cars,
    garage_area,
    lot_area,
    year_built,
    total_bsmt_sf,
):

    input_data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars],
        "GarageArea": [garage_area],
        "LotArea": [lot_area],
        "YearBuilt": [year_built],
        "TotalBsmtSF": [total_bsmt_sf]
    })

    prediction = model.predict(input_data)

    return prediction[0]