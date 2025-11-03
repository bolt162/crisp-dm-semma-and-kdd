# Model Card: Telco Customer Churn Prediction

## Model Details

**Model Type:** Logistic Regression

**Version:** 1.0.0

**Date:** 2025-10-28

**Methodology:** CRISP-DM

**Developers:** Data Science Team

**License:** Internal Use Only

## Intended Use

**Primary Use Case:** Predict probability of customer churn to enable proactive retention interventions

**Target Users:** Marketing team, customer success team, data analysts

**Deployment Context:** Monthly batch scoring of active customer base

**Out-of-Scope Uses:**
- Real-time prediction (model designed for batch scoring)
- Individual customer-level decisions without human review
- Automated contract termination

## Training Data

**Dataset:** Telco Customer Churn (WA_Fn-UseC_-Telco-Customer-Churn.csv)

**Size:** 7,043 total customers

**Split:**
- Training: 60% (4,225 samples)
- Validation: 20% (1,409 samples)
- Test: 20% (1,409 samples)

**Class Distribution:**
- No Churn: 5,174 (73.5%)
- Churn: 1,869 (26.5%)

**Features:** 19 original features → 30 after encoding

**Preprocessing:**
- Missing value imputation (median for numeric, constant for categorical)
- One-hot encoding for categorical variables
- Standard scaling for numeric variables
- SMOTE oversampling for class balance (training only)

## Model Performance

### Test Set Results

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| ROC AUC | 0.800 | 0.840 | ✅ |
| Recall @ Top 10% | 0.400 | 0.278 | ⚠️ |
| Precision | 0.600 | 0.515 | ⚠️ |
| F1 Score | 0.600 | 0.622 | ✅ |

**Optimal Threshold:** 0.455 (F1-optimized)

**Confusion Matrix (Test Set):**
```
                Predicted
              No Churn  Churn
Actual No      758      277
       Churn   80       294
```

### Cross-Validation Performance

**Mean CV ROC AUC:** 0.8669 ± 0.0106

## Ethical Considerations

**Fairness:** Model trained on aggregate data without demographic features. Recommend monitoring for disparate impact across customer segments in production.

**Transparency:** SHAP values provide feature-level explanations for predictions.

**Privacy:** No personally identifiable information (PII) used in model. Customer IDs removed during preprocessing.

**Potential Harms:**
- False positives may lead to unnecessary retention spending
- False negatives miss at-risk customers
- Model should not be sole factor in customer treatment decisions

## Limitations

- Trained on historical data - performance may degrade with changing customer behavior
- Class imbalance addressed via SMOTE - real-world distribution may differ
- Model does not capture temporal dynamics or seasonality
- Feature engineering limited to available data - additional signals may improve performance
- Threshold optimization based on test set - may need adjustment in production
- Model interpretability varies by algorithm choice
- Potential for concept drift - requires regular retraining

## Recommendations

1. **Monitoring:** Track model performance monthly via ROC AUC and recall @ top 10%
2. **Retraining:** Retrain quarterly or when performance drops >5%
3. **Validation:** A/B test retention interventions to measure business impact
4. **Threshold Tuning:** Adjust decision threshold based on retention budget and campaign capacity
5. **Data Quality:** Implement ongoing data quality checks
6. **Concept Drift:** Monitor for changes in feature distributions

## Contact

**Model Owner:** Data Science Team

**Last Updated:** 2025-10-28

**Documentation:** See `/content/artifacts/` for all model artifacts

---

*This model card follows guidelines from Mitchell et al. (2019) and is intended to promote transparency and responsible AI practices.*
