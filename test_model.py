import joblib
import pandas as pd
import numpy as np

# Load model and transformers
model = joblib.load("final_logistic_model.pkl")
preprocessor = joblib.load("preprocessor_ohe.pkl")
scaler = joblib.load("scaler_continuous.pkl")
selected_features = joblib.load("selected_features.pkl")
continuous_cols = joblib.load("continuous_cols.pkl")

# Sample employee data (replace values as needed)
sample_employee = {
    "JobLevel": 2,
    "YearsWithCurrManager": 5,
    "YearsInCurrentRole": 4,
    "TotalWorkingYears": 8,
    "PerformanceRating": 3,
    "Gender": "Female",
    "OverTime": "Yes",
    "BusinessTravel": "Travel_Rarely",
    "Department": "Sales",
    "EducationField": "Life Sciences",
    "MaritalStatus": "Single",
    "JobRole_Grouped": "Sales Executive",
    "Age": 41,
    "DailyRate": 1102,
    "DistanceFromHome": 1,
    "Education": 2,
    "EnvironmentSatisfaction": 3,
    "HourlyRate": 94,
    "JobInvolvement": 3,
    "JobSatisfaction": 4,
    "MonthlyRate": 19479,
    "NumCompaniesWorked": 8,
    "PercentSalaryHike": 11,
    "RelationshipSatisfaction": 1,
    "StockOptionLevel": 0,
    "TrainingTimesLastYear": 0,
    "WorkLifeBalance": 1,
    "YearsAtCompany": 6,
    "YearsSinceLastPromotion": 0,
    "MonthlyIncome": 5993
}


# Compute log column
sample_employee["MonthlyIncome_log"] = np.log(sample_employee["MonthlyIncome"])
# Remove original MonthlyIncome (optional)
#sample_employee.pop("MonthlyIncome")

# Convert to DataFrame
new_df = pd.DataFrame([sample_employee])

# Apply preprocessing
X_ohe = preprocessor.transform(new_df)
X_ohe_df = pd.DataFrame(X_ohe, columns=preprocessor.get_feature_names_out())

# Align to selected features (fill missing columns with 0)
X_aligned = X_ohe_df.reindex(columns=selected_features, fill_value=0)
#X_aligned = X_ohe_df.reindex(columns=selected_features, fill_value=0)


# Scale continuous columns
X_aligned[continuous_cols] = scaler.transform(X_aligned[continuous_cols])
#X_aligned[continuous_cols] = scaler.transform(X_aligned[continuous_cols])

# Predict
proba = model.predict_proba(X_aligned)[0, 1]
#proba = model.predict_proba(X_ohe_df)[0, 1]
label = "Yes" if proba >= 0.5 else "No"

print(f"Prediction Probability: {proba:.4f}")
print(f"Prediction Label: {label}")
