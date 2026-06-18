# House Price Prediction

## Project Overview

This project predicts house sale prices using machine learning techniques.

The dataset was obtained from Kaggle's House Prices - Advanced Regression Techniques competition.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Jupyter Notebook

---

## Data Preprocessing

- Removed columns with excessive missing values
- Handled missing numerical values using median imputation
- Handled missing categorical values using mode imputation
- Applied One-Hot Encoding to categorical features

---

## Models Used

### Linear Regression

Results:
- MAE: 20,436
- RMSE: 52,315
- R² Score: 0.643

### Random Forest Regressor

Results:
- MAE: 17,675
- RMSE: 28,833
- R² Score: 0.892

---

## Conclusion

Random Forest significantly outperformed Linear Regression and achieved an R² score of approximately 89%.

---

## Dataset

Download the dataset from Kaggle:

House Prices - Advanced Regression Techniques

Place:

train.csv

inside:

data/train.csv