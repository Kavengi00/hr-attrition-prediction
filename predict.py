#!/usr/bin/env python3
"""
predict.py: Updated for split preprocessing (OHE via loaded pipeline + separate scaler for continuous cols).
- Loads OHE pipeline → applies to new data.
- Aligns features (post-VIF).
 Applies scaler to continuous cols only..
"""

import joblib
import pandas as pd
import numpy as np

def load_artifacts():
    try:
        model = joblib.load("final_logistic_model.pkl")
        ohe_pipeline = joblib.load("preprocessor_ohe.pkl")  # OHE only
        scaler = joblib.load("scaler_continuous.pkl")       # Scaling for continuous
        selected_features = joblib.load("selected_features.pkl")
        continuous_cols = joblib.load("continuous_cols.pkl")  # Post-VIF continuous
        
        print("Artifacts loaded successfully.")
        return model, ohe_pipeline, scaler, selected_features, continuous_cols
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

def preprocess_new_data(new_df, ohe_pipeline, scaler, selected_features, continuous_cols):
    """
    Split preprocessing: OHE → align → scale continuous cols.
    """
    # Optional drop irrelevant (if inputs have them)
    # irrelevant_cols = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']
    # for col in irrelevant_cols: new_df = new_df.drop(columns=[col], errors='ignore')
    
    # Apply OHE pipeline
    new_ohe = ohe_pipeline.transform(new_df)
    new_ohe_df = pd.DataFrame(new_ohe, columns=ohe_pipeline.named_steps['preprocess'].get_feature_names_out())
    
    # Align to selected features
    new_aligned = new_ohe_df.reindex(columns=selected_features, fill_value=0)
    missing_cols = [col for col in selected_features if col not in new_aligned.columns]
    if missing_cols:
        print(f"Warning: Adding {missing_cols} with zeros.")
        for col in missing_cols:
            new_aligned[col] = 0
    
    # Scale only continuous cols (post-align)
    continuous_in_selected = [col for col in continuous_cols if col in new_aligned.columns]
    new_aligned[continuous_in_selected] = scaler.transform(new_aligned[continuous_in_selected])
    
    print(f"Preprocessed shape: {new_aligned.shape}")
    return new_aligned

def make_predictions(model, X_new):
    proba = model.predict_proba(X_new)[:, 1]
    predictions = (proba > 0.5).astype(int)
    return proba, predictions

def main():
    model, ohe_pipeline, scaler, selected_features, continuous_cols = load_artifacts()
    
    try:
        new_df = pd.read_csv("new_data.csv")
        print(f"Loaded new data: {new_df.shape}")
    except FileNotFoundError:
        print("Error: 'new_data.csv' not found.")
        return
    
    X_new = preprocess_new_data(new_df, ohe_pipeline, scaler, selected_features, continuous_cols)
    proba, predictions = make_predictions(model, X_new)
    
    results = pd.DataFrame({
        'Attrition_Probability': proba,
        'Predicted_Attrition': predictions  # 1=Yes, 0=No
    })
    
    print("\nSample Predictions:")
    print(results.head())
    results.to_csv("predictions.csv", index=False)
    print("\nSaved to 'predictions.csv'.")
    
    attrition_rate = (predictions.sum() / len(predictions)) * 100
    print(f"Predicted Attrition Rate: {attrition_rate:.2f}%")

if __name__ == "__main__":
    main()