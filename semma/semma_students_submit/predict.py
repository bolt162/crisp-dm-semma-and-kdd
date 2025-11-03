# Prediction Function for Student Performance Model
# Generated: 2025-10-28 23:30:40

import pickle
import pandas as pd
import numpy as np

# Load artifacts
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('best_model.pkl', 'rb') as f:
    model_clf = pickle.load(f)

with open('best_model_regression.pkl', 'rb') as f:
    model_reg = pickle.load(f)

# Feature engineering function
def engineer_features(df):
    df = df.copy()
    df['attendance_ratio'] = 1 - (df['absences'] / df['absences'].max())
    df['study_effort_index'] = df['studytime'] * (1 + df['schoolsup'].map({'yes': 1, 'no': 0}))
    df['parent_edu_avg'] = (df['Medu'] + df['Fedu']) / 2
    df['social_risk'] = (df['Dalc'] + df['Walc'] + df['goout']) / 3
    df['family_support'] = df['famrel'] * (1 + df['famsup'].map({'yes': 1, 'no': 0}))
    df['has_failures'] = (df['failures'] > 0).astype(int)
    return df

# Feature columns
feature_cols = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'attendance_ratio', 'study_effort_index', 'parent_edu_avg', 'social_risk', 'family_support', 'has_failures']

# Prediction function
def predict(df):
    df_processed = engineer_features(df.copy())
    X = df_processed[feature_cols]
    X_processed = preprocessor.transform(X)
    
    pass_pred = model_clf.predict(X_processed)
    pass_proba = model_clf.predict_proba(X_processed)[:, 1]
    grade_pred = model_reg.predict(X_processed)
    
    results = pd.DataFrame({
        'pass_prediction': pass_pred,
        'pass_probability': pass_proba,
        'grade_prediction': np.clip(grade_pred, 0, 20)
    })
    
    return results

# Example usage:
# df = pd.read_csv('new_student_data.csv')
# predictions = predict(df)
