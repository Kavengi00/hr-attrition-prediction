Yes, absolutely—adding dynamic badges is a great touch! They make the repo look more professional and give quick status checks (e.g., build success on Render). I'll integrate a "Badges" section at the top of the README using Shields.io (which auto-updates via API calls—no manual maintenance needed).

Here's the **updated README.md** with the badges added. I've placed them prominently after the title for visibility. The rest of the content remains the same, but I've refined a few spots for flow (e.g., fixed minor Markdown syntax in the structure tree and deployment steps).

```markdown
# HR Attrition Prediction 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-latest-blue?logo=docker)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-orange)](https://render.com/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Kavengi00/hr-attrition-prediction/ci.yml?logo=github-actions)](https://github.com/Kavengi00/hr-attrition-prediction/actions)  <!-- Add your repo owner/name -->
[![License](https://img.shields.io/github/license/Kavengi00/hr-attrition-prediction?color=brightgreen)](https://github.com/Kavengi00/hr-attrition-prediction/blob/main/LICENSE)

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
├── main.py                  # FastAPI app
├── predict.py               # Script for loading model and making predictions
├── train.py                 # Script for training and saving model
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container configuration
├── HR-Employee-Attrition.csv # Dataset
├── templates/               # HTML templates for form-based UI
├── final_logistic_model.pkl # Saved model
└── ...                      # Other artifacts like preprocessors and pickles
```

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kavengi00/hr-attrition-prediction.git
   cd hr-attrition-prediction
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally with FastAPI**

   ```bash
   uvicorn main:app --reload
   ```

   - Access the API documentation: http://127.0.0.1:8000/docs
   - Test predictions using the `/predict` endpoint or the `/predict_form` HTML form.

---

## Deployment

This project is deployed using Render with Docker.

- **Deployed URL:** [https://hr-attrition-prediction.onrender.com](https://hr-attrition-prediction.onrender.com) (update with your actual Render URL)

**Steps to Deploy on Render:**

1. Create a new Web Service in [Render Dashboard](https://dashboard.render.com).
2. Connect your GitHub repository `hr-attrition-prediction`.
3. Select **Docker** as the environment.
4. Set **Dockerfile** as the build path.
5. Add environment variables if needed (e.g., for secrets).
6. Deploy—Render auto-builds on git pushes.
7. Access the live API at the provided Render URL, e.g., https://hr-attrition-prediction.onrender.com/docs.

---

## How to Use the API

### Predict via API

Send a POST request with JSON data containing all employee features to:

```
POST /predict
```

**Example JSON:**

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

**Response:**

```json
{
  "attrition_probability": 0.67,
  "will_leave": "Yes",
  "risk_level": "Medium"
}
```

### Predict via HTML Form

- Access `/predict_form` to submit employee data using a web form (interactive UI for non-dev users).

---

## Features & Techniques

- **Data Cleaning & EDA** (Exploratory Data Analysis)
- **Feature Importance Analysis** (via SHAP values)
- **Logistic Regression Model** (or XGBoost; tunable)
- **Model Export using Pickle**
- **Preprocessing with One-Hot Encoding & Scaling**
- **API Development using FastAPI**
- **Deployment with Docker and Render**

---

*⭐ Star this repo if it helps! Contributions welcome via pull requests.*
```

### Quick Notes on the Badges
- **Customization:** Replace `Kavengi00/hr-attrition-prediction` with your actual GitHub repo path (e.g., for the build/license badges). Shields.io will auto-fetch data.
- **Dynamic Updates:** The Render badge links to your service status (it'll show "Deployed" or fail if down). GitHub Actions badge assumes you add a simple CI workflow (e.g., `ci.yml` for linting/tests—let me know if you need that file).
- **Why These?** They cover tech stack (Python/FastAPI/Docker), deployment (Render), and repo health (build/license). Keeps it concise.

Copy-paste this into your repo's `README.md`, commit/push, and watch the badges populate (may take a few minutes). If you need the full repo setup (e.g., `main.py` tweaks or CI YAML), just say the word! What's next—testing the deployment or adding a demo GIF?
