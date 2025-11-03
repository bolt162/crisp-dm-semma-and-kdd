
# Housing Price Prediction - KDD Project Artifacts

## Overview
This directory contains all artifacts from the Knowledge Discovery in Databases (KDD) project for housing price prediction.

**Project:** House Price Prediction using Machine Learning  
**Date:** October 2025  
**Best Model:** Lasso  
**Test RMSE:** $49,370.38  
**Test R²:** 0.5754

---

## Quick Start

### Making Predictions

```python
from predict_housing import predict_prices
import pandas as pd

# Prepare your data
data = pd.DataFrame({
    'SquareFeet': [2000, 2500],
    'Bedrooms': [3, 4],
    'Bathrooms': [2, 3],
    'Neighborhood': ['Suburb', 'Urban'],
    'YearBuilt': [2015, 2020]
})

# Get predictions
prices = predict_prices(data)
print(prices)
```

---

## Directory Structure

### 📁 Core Artifacts
- `best_model.pkl` - Trained Lasso model
- `preprocessing_pipeline.pkl` - Complete preprocessing pipeline
- `predict_housing.py` - Production prediction function

### 📊 Analysis Results
- `model_comparison.csv` - Performance metrics for all models
- `feature_importance.csv` - Feature importance rankings
- `permutation_importance.csv` - Permutation-based importance
- `error_by_decile.csv` - Error analysis by price range

### 📈 Visualizations
- `target_distribution.png` - Price distribution analysis
- `correlation_heatmap.png` - Feature correlation matrix
- `model_comparison_metrics.png` - Model performance comparison
- `feature_importance.png` - Top features visualization
- `residual_analysis.png` - Residual diagnostic plots
- `predicted_vs_actual.png` - Prediction accuracy visualization
- `error_by_decile.png` - Error patterns by price range

### 🔧 Configuration & Metadata
- `selection_metadata.json` - Feature selection details
- `preprocessing_summary.json` - Preprocessing configuration
- `transformation_summary.json` - Feature engineering details
- `best_model_metadata.json` - Model metadata
- `findings_and_insights.md` - Comprehensive insights report

### 🛠️ Additional Resources
- `scaler.pkl` - Fitted RobustScaler
- `label_encoder.pkl` - Neighborhood encoder
- `pca_model.pkl` - PCA transformer
- `lasso_selector.pkl` - Lasso feature selector

---

## Model Details

### Input Features
1. **SquareFeet** (numeric) - Total square footage
2. **Bedrooms** (numeric) - Number of bedrooms
3. **Bathrooms** (numeric) - Number of bathrooms
4. **Neighborhood** (categorical) - Urban/Suburb/Rural
5. **YearBuilt** (numeric) - Year of construction

### Output
- **Predicted Price** (USD) - Estimated sale price

### Performance
- Mean Absolute Error: $39,437.76
- Root Mean Squared Error: $49,370.38
- R² Score: 0.5754

---

## Technical Specifications

### Preprocessing
- **Scaling:** RobustScaler (robust to outliers)
- **Encoding:** LabelEncoder for neighborhood
- **Missing Values:** None in current dataset

### Feature Engineering
- House age calculation
- Room ratios and totals
- Space efficiency metrics
- Neighborhood interactions

### Model Training
- **Train/Val/Test Split:** 60/20/20
- **Random Seed:** 42
- **Cross-Validation:** 5-fold for hyperparameter tuning

---

## Requirements

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
xgboost>=1.5.0
```

---

## Support & Contact

For questions or issues:
- Review `findings_and_insights.md` for detailed analysis
- Check model metadata in JSON files
- Refer to original Colab notebook for full code

---

**Last Updated:** October 2025  
**Version:** 1.0  
**License:** MIT
