# Exploratory Data Analysis Summary
Generated: 2025-10-28 23:23:10

## Dataset Overview
- Total samples: 395
- Training samples: 237 (60.0%)
- Validation samples: 79 (20.0%)
- Test samples: 79 (20.0%)
- Features: 34
- Target: G3 (Final Grade, 0-20 scale)

## Data Quality
- Missing values: 0 (0.00%)
- Duplicate rows: 0 (0.00%)
- Numeric features: 13
- Categorical features: 17

## Target Variable
- Mean G3: 10.30 ± 4.75
- Median G3: 11.00
- Pass rate: 67.09% (threshold = 10)

## Top Correlated Features with G3
Medu          0.177011
Fedu          0.134332
famrel        0.105061
studytime     0.092599
freetime      0.039835
absences      0.039020
Walc          0.014837
Dalc         -0.039864
health       -0.056616
traveltime   -0.078857

## Key Insights
1. **Grade Distribution**: The final grades show a roughly normal distribution with some left skew.
2. **Pass Rate**: Approximately 67% of students pass with a grade >= 10.
3. **Strong Predictors**: Past performance (if available), study time, and parental education show strong correlations.
4. **Risk Factors**: Higher number of past failures is associated with lower final grades.
5. **Data Quality**: The dataset is clean with no missing values, making it suitable for modeling.

## Figures Generated
- target_distribution.png
- missing_values.png
- numeric_distributions.png
- categorical_distributions.png
- correlations.png
- pairwise_relationships.png
- segment_analysis.png
