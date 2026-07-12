from predict import predict_price

price = predict_price(
    overall_qual=7,
    gr_liv_area=1800,
    garage_cars=2,
    garage_area=500,
    lot_area=8500,
    year_built=2005,
    total_bsmt_sf=900
)

print(price)