from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np


# ---------------------------
# Initialize app
# ---------------------------
app = FastAPI(title="HR Attrition Prediction API")

# ---------------------------
# Load model and preprocessing artifacts
# ---------------------------
try:
    model = joblib.load("final_logistic_model.pkl")
    preprocessor = joblib.load("preprocessor_ohe.pkl")
    scaler = joblib.load("scaler_continuous.pkl")
    selected_features = joblib.load("selected_features.pkl")
    continuous_cols = joblib.load("continuous_cols.pkl")
except Exception as e:
    print(f"Error loading model or transformers: {e}")

# ---------------------------
# Input schema
# ---------------------------
class EmployeeData(BaseModel):
    Gender: str
    OverTime: str
    BusinessTravel: str
    Department: str
    EducationField: str
    MaritalStatus: str
    JobRole_Grouped: str
    Age: int
    DailyRate: int
    DistanceFromHome: int
    Education: int
    EnvironmentSatisfaction: int
    HourlyRate: int
    JobInvolvement: int
    JobSatisfaction: int
    MonthlyRate: int
    NumCompaniesWorked: int
    PercentSalaryHike: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsSinceLastPromotion: int
    MonthlyIncome: int
    JobLevel: int
    YearsWithCurrManager: int
    YearsInCurrentRole: int
    TotalWorkingYears: int
    PerformanceRating: int

    model_config = {
        "json_schema_extra": {
            "example": {
                 "Age": 41,
                "BusinessTravel": "Travel_Rarely",
                "Department": "Sales",
                "DistanceFromHome": 1,
                "Education": 2,
                "EducationField": "Life Sciences",
                "Gender": "Female",
                "JobSatisfaction": 4,
                "MaritalStatus": "Single",
                "MonthlyIncome": 5993,
                "OverTime": "Yes",
                "JobRole_Grouped": "Sales Executive",
                "DailyRate": 1102,
                "HourlyRate": 94,
                "MonthlyRate": 19479,
                "NumCompaniesWorked": 8,
                "PercentSalaryHike": 11,
                "YearsAtCompany": 6,
                "YearsSinceLastPromotion": 0,
                "EnvironmentSatisfaction": 3,
                "JobInvolvement": 3,
                "RelationshipSatisfaction": 1,
                "WorkLifeBalance": 1,
                "JobLevel": 2,
                "YearsWithCurrManager": 5,
                "YearsInCurrentRole": 4,
                "TotalWorkingYears": 8,
                "PerformanceRating": 3,
                "StockOptionLevel": 0,
                "TrainingTimesLastYear": 0
            }
        }
    }


# ---------------------------
# Root endpoint
# ---------------------------
@app.get("/")
async def root():
    return {"message": "HR Attrition Prediction API is running"}

# ---------------------------
# Prediction endpoint
# ---------------------------
@app.post("/predict")
async def predict(employee: EmployeeData):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([employee.model_dump()])  # Use model_dump with Pydantic v2
        
        # Compute log column for MonthlyIncome
        df["MonthlyIncome_log"] = np.log(df["MonthlyIncome"])
        
        # Apply preprocessor
        X_ohe = preprocessor.transform(df)
        feature_names = preprocessor.get_feature_names_out()
        X_ohe_df = pd.DataFrame(X_ohe, columns=feature_names)
        
        # Align with selected features
        X_aligned = X_ohe_df.reindex(columns=selected_features, fill_value=0)
        
        # Scale continuous columns
        continuous_in_selected = [col for col in continuous_cols if col in X_aligned.columns]
        if continuous_in_selected:
            X_aligned[continuous_in_selected] = scaler.transform(X_aligned[continuous_in_selected])
        
        # Predict probability
        probability = model.predict_proba(X_aligned)[0, 1]
        prediction = "yes" if probability > 0.5 else "no"
        
        # Return structured response
        return {
            "attrition_probability": float(probability),
            "will_leave": prediction,
            "risk_level": "High" if probability > 0.7 else "Medium" if probability > 0.3 else "Low"
        }

        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# ---------------------------
# Optional main for standalone run
# ---------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)