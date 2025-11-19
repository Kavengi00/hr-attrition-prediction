```markdown
# HR Attrition Prediction 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-latest-blue?logo=docker)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-orange)](https://render.com/)

---

## Project Overview

This project predicts **employee attrition** using HR data. The model analyzes employee features and estimates the probability of leaving the company, helping HR teams make informed decisions about retention strategies.

The prediction is served via a **FastAPI** REST API, containerized with **Docker**, and deployed to **Render** for easy access.

---

## Dataset

The dataset used is `HR-Employee-Attrition.csv`. It contains employee features and attrition labels such as:

- `Age`, `BusinessTravel`, `Department`, `DistanceFromHome`, `Education`, `EducationField`, `Gender`
- `JobSatisfaction`, `MaritalStatus`, `MonthlyIncome`, `OverTime`, `JobRole_Grouped`
- `DailyRate`, `HourlyRate`, `MonthlyRate`, `NumCompaniesWorked`, `PercentSalaryHike`, `YearsAtCompany`
- `EnvironmentSatisfaction`, `JobInvolvement`, `RelationshipSatisfaction`, `WorkLifeBalance`, `JobLevel`
- `YearsWithCurrManager`, `YearsInCurrentRole`, `TotalWorkingYears`, `PerformanceRating`, `StockOptionLevel`, `TrainingTimesLastYear`

> **If the dataset is not committed to this repository**, download it from Kaggle:  
> [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
> After downloading, place `HR-Employee-Attrition.csv` in the project root.

---

## Project Structure

```

hr-attrition-prediction/
├─ main.py                 # FastAPI app
├─ predict.py              # Script for loading model and making predictions
├─ train.py                # Script for training and saving model
├─ requirements.txt        # Python dependencies
├─ Dockerfile              # Docker container configuration
├─ HR-Employee-Attrition.csv # Dataset
├─ templates/              # HTML templates for form-based UI
├─ final_logistic_model.pkl # Saved model
└─ ...                     # Other artifacts like preprocessors and pickles

````

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/Kavengi00/hr-attrition-prediction.git
cd hr-attrition-prediction
````

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run locally with FastAPI**

```bash
uvicorn main:app --reload
```

* Access the API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Test predictions using the `/predict` endpoint or the `/predict_form` HTML form.

---

## Deployment

This project is deployed using **Render** with Docker.

* **Deployed URL:** [Your Render URL here]

### Steps:

1. Create a new Web Service in Render.
2. Connect your GitHub repository `hr-attrition-prediction`.
3. Select **Docker** as the environment.
4. Set `Dockerfile` as the build path.
5. Start the service.
6. Access the live API at the provided Render URL, e.g., `https://hr-attrition-prediction.onrender.com/docs`.

---

## How to Use the API

### Predict via API

Send a **POST** request with JSON data containing all employee features to:

```
POST /predict
```

Example JSON:

```json
{
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
```

* **Response:**

```json
{
  "attrition_probability": 0.67,
  "will_leave": "Yes",
  "risk_level": "Medium"
}
```

### Predict via HTML Form

* Access `/predict_form` to submit employee data using a web form.

---

## Features & Techniques

* Data Cleaning & EDA (Exploratory Data Analysis)
* Feature Importance Analysis
* Logistic Regression Model
* Model Export using Pickle
* Preprocessing with One-Hot Encoding & Scaling
* API Development using **FastAPI**
* Deployment with **Docker** and **Render**

---
Do you want me to do that next?
```
