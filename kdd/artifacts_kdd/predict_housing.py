
"""Housing Price Prediction Module

This module provides a production-ready function to predict house prices
based on key housing features.

Usage:
    from predict_housing import predict_prices
    import pandas as pd
    
    data = pd.DataFrame({
        'SquareFeet': [2000],
        'Bedrooms': [3],
        'Bathrooms': [2],
        'Neighborhood': ['Suburb'],
        'YearBuilt': [2015]
    })
    
    prices = predict_prices(data)
"""

import pickle
import pandas as pd
import numpy as np
from pathlib import Path

# Path configuration
ARTIFACT_DIR = Path(__file__).parent / 'artifacts_kdd'

def engineer_features(X_df, current_year=2025):
    """Feature engineering for prediction"""
    X_eng = X_df.copy()
    
    X_eng['House_Age'] = current_year - X_df['YearBuilt']
    X_eng['Is_New'] = (X_eng['House_Age'] <= 5).astype(int)
    X_eng['Is_Vintage'] = (X_eng['House_Age'] >= 50).astype(int)
    X_eng['Total_Rooms'] = X_df['Bedrooms'] + X_df['Bathrooms']
    X_eng['Room_Ratio'] = X_df['Bathrooms'] / (X_df['Bedrooms'] + 0.1)
    X_eng['SqFt_Per_Room'] = X_df['SquareFeet'] / (X_eng['Total_Rooms'] + 0.1)
    X_eng['SqFt_x_Neighborhood'] = X_df['SquareFeet'] * X_df['Neighborhood_Encoded']
    
    return X_eng

def predict_prices(df_new, 
                   model_path=None,
                   pipeline_path=None):
    """
    Predict house prices from housing features.
    
    Parameters:
    -----------
    df_new : pd.DataFrame
        DataFrame with columns: SquareFeet, Bedrooms, Bathrooms, Neighborhood, YearBuilt
    model_path : str, optional
        Path to model file (default: artifacts_kdd/best_model.pkl)
    pipeline_path : str, optional
        Path to pipeline file (default: artifacts_kdd/preprocessing_pipeline.pkl)
        
    Returns:
    --------
    predictions : np.array
        Predicted prices
    """
    if model_path is None:
        model_path = ARTIFACT_DIR / 'best_model.pkl'
    if pipeline_path is None:
        pipeline_path = ARTIFACT_DIR / 'preprocessing_pipeline.pkl'
    
    # Load artifacts
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(pipeline_path, 'rb') as f:
        pipeline = pickle.load(f)
    
    scaler = pipeline['scaler']
    label_encoder = pipeline['label_encoder']
    feature_columns = pipeline['feature_columns']
    
    # Validate
    required_cols = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'Neighborhood', 'YearBuilt']
    missing = set(required_cols) - set(df_new.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Process
    df_proc = df_new[required_cols].copy()
    df_proc['Neighborhood_Encoded'] = label_encoder.transform(df_proc['Neighborhood'])
    X_new = df_proc[feature_columns]
    X_scaled = pd.DataFrame(scaler.transform(X_new), columns=feature_columns, index=X_new.index)
    X_eng = engineer_features(X_scaled)
    
    return model.predict(X_eng)
