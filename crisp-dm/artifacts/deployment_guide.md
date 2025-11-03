# Deployment Guide: Telco Churn Prediction Model

## Quick Start

### Prerequisites
- Python 3.8+
- Required packages: pandas, numpy, scikit-learn, xgboost, joblib

### Installation
```bash
pip install pandas numpy scikit-learn xgboost joblib
```

## Artifacts

Required files from `/content/artifacts/`:
- `preprocessor.pkl` - Fitted preprocessing pipeline
- `best_model.pkl` - Trained Logistic Regression model
- `model_card.md` - Model documentation

## Usage

### 1. Load Model Artifacts

```python
import pickle
import pandas as pd

# Load artifacts
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)
```

### 2. Prepare Input Data

Input CSV must contain these columns:
gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges

**Note:** Do NOT include the 'Churn' column. CustomerID is optional.

### 3. Generate Predictions

```python
# Load customer data
customers = pd.read_csv('customers.csv')

# Make predictions
predictions = predict_churn_proba(
    customers,
    preprocessor,
    model,
    threshold=0.455  # F1-optimized threshold
)

# Save results
predictions.to_csv('churn_predictions.csv', index=False)
```

### 4. Batch Scoring (Production)

```python
# Batch score entire customer base
predictions = batch_score_customers(
    input_csv_path='monthly_customers.csv',
    output_csv_path='monthly_predictions.csv',
    artifacts_dir='/path/to/artifacts',
    threshold=0.455
)
```

## Output Format

Predictions include:
- `customerID`: Customer identifier (if provided)
- `churn_probability`: Probability of churn [0, 1]
- `churn_prediction`: Binary prediction (0=No Churn, 1=Churn)
- `risk_category`: Risk level (Low/Medium/High)

## Recommended Thresholds

| Strategy | Threshold | Use Case |
|----------|-----------|----------|
| Balanced (F1) | 0.455 | General purpose |
| High Precision | 0.652 | Minimize false alarms |
| Default | 0.500 | Standard approach |

## Production Checklist

- [ ] Model artifacts deployed to secure location
- [ ] Input data validation implemented
- [ ] Error handling and logging configured
- [ ] Performance monitoring dashboard created
- [ ] A/B testing framework set up
- [ ] Model refresh schedule established (quarterly)
- [ ] Stakeholder training completed

## Monitoring

Track these metrics monthly:
1. **Model Performance**
   - ROC AUC on recent data
   - Precision/Recall trends
   - Calibration metrics

2. **Data Quality**
   - Missing value rates
   - Feature distribution shifts
   - Outlier frequency

3. **Business Impact**
   - Retention campaign conversion rates
   - Cost per retained customer
   - False positive/negative rates

## Troubleshooting

### Issue: Missing columns
**Solution:** Ensure input data matches training schema exactly.

### Issue: Poor predictions
**Solution:** Check for:
- Data quality issues
- Concept drift (retrain model)
- Incorrect preprocessing

### Issue: Slow inference
**Solution:**
- Use batch processing for large datasets
- Consider model optimization techniques
- Implement caching for repeated predictions

## Support

For questions or issues:
- Review model_card.md for detailed documentation
- Check artifacts for additional resources
- Contact: Data Science Team

---

*Last Updated: 2025-10-28*
