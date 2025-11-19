---

# **HR Attrition Prediction 🚀**

A machine learning project that predicts whether an employee is likely to leave the company based on their profile and work-related features. The project covers **data preprocessing, EDA, model training, FastAPI deployment, Docker containerization and cloud deployment on Render**.

---

## **📌 Project Overview**

Employee attrition is a major challenge for organizations. Predicting which employees are at risk of leaving helps HR teams improve retention strategies and workforce planning.

This project uses HR data (demographics, job role, compensation, performance and satisfaction metrics) to predict attrition using a trained Logistic Regression model.

### **Key Features Used**

* Gender, Age, Marital Status
* Department, Job Role
* Business Travel, OverTime
* Monthly Income, Job Level
* Years at Company, Years in Current Role
* Job Satisfaction, Environment Satisfaction
* Performance Rating, Work-Life Balance
* Many other categorical & numeric features (full list in `EmployeeData` schema in `main.py`)

---

## **📂 Repository Structure**

```
hr-attrition-prediction/
├─ main.py                     # FastAPI application
├─ predict.py                  # Model loading and prediction utilities
├─ train.py                    # Model training script
├─ requirements.txt            # Python dependencies
├─ Dockerfile                  # Docker container configuration
├─ HR-Employee-Attrition.csv   # Dataset
├─ final_logistic_model.pkl    # Trained model
├─ scaler_continuous.pkl       # Scaler for numerical features
├─ preprocessor_ohe.pkl        # One-hot encoder
├─ selected_features.pkl       # Selected model features
└─ classification.ipynb        # EDA, preprocessing, and model building
```

---

## **📊 Dataset**

Dataset: **HR-Employee-Attrition.csv**

It contains:

* Employee demographics
* Compensation details
* Work satisfaction metrics
* Performance indicators
* **Attrition label**

If the dataset is not in the repo, download it from Kaggle:
➡️ *IBM HR Analytics Attrition Dataset*: [https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

Place the CSV file in the project root.

---

## **⚙️ Installation & Local Setup**

### 1. Clone Repository

```bash
git clone https://github.com/Kavengi00/hr-attrition-prediction.git
cd hr-attrition-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI App

```bash
uvicorn main:app --reload
```

### 5. Access Local API Documentation

📍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
(Interactive Swagger UI)

---

## **📡 How to Use the API**

### **POST /predict**

Send JSON with employee features.

#### **Example Input**

```json
{
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
  "MonthlyIncome": 5993,
  "JobLevel": 2,
  "YearsWithCurrManager": 5,
  "YearsInCurrentRole": 4,
  "TotalWorkingYears": 8,
  "PerformanceRating": 3
}
```

#### **Example Output**

```json
{
  "attrition_probability": 0.32,
  "will_leave": "No",
  "risk_level": "Medium"
}
```

---

## **🔍 Exploratory Data Analysis (EDA)**

Performed in `classification.ipynb`, including:

* Missing value checks
* Outlier detection
* Distribution analysis
* Feature engineering
* Correlations
* Feature importance

---

## **🧠 Model Training**

Model: **Logistic Regression**

Preprocessing steps:

* One-Hot Encoding (categorical features)
* Standard Scaling (numerical features)
* Feature selection

Artifacts saved:

* `final_logistic_model.pkl`
* `preprocessor_ohe.pkl`
* `scaler_continuous.pkl`
* `selected_features.pkl`

Prediction handled inside `predict.py`.

---

## **🐳 Docker Containerization**

### Build Docker Image

```bash
docker build -t hr-attrition-api .
```

### Run Container

```bash
docker run -p 8000:8000 hr-attrition-api
```

Then open:
📍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **☁️ Deployment on Render**

The service is deployed using **Docker on Render.com**.

### Deployment Settings:

* **Service Type:** Web Service
* **Environment:** Docker
* **Branch:** main
* **Build Command:** Dockerfile defaults
* **Start Command:**

  ```
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

### **Live API URL**

🔗 [https://hr-attrition-prediction-3if9.onrender.com/docs](https://hr-attrition-prediction-3if9.onrender.com/docs))

---

## **📦 Dependencies**

fastapi
uvicorn[standard]
pandas
numpy
scikit-learn
(Full list in `requirements.txt`)

---

## **📈 Project Highlights**

* Full ML pipeline from raw data to deployment
* Clean EDA and feature engineering
* Logistic Regression model (extendable to XGBoost, RandomForest, etc.)
* API-first architecture with FastAPI
* Dockerized for portability
* Cloud deployment on Render

---

## **📸 Screenshots / Demo**

* Find `/docs` Swagger UI prediction screenshot on Screenshot_20-11-2025_21544_hr-attrition-prediction-3if9.onrender.com

---

## **📬 Final Notes**

* Users can test directly via the Render URL
* Contributions and improvements are welcome

---
