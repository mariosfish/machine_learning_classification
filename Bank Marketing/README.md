# Models

## S. Moro, P. Cortez and P. Rita Results


|                     | AUC   |
|---------------------|-------|
| Logistic Regression | 0.900 |
| Decision tree       | 0.833 |
| Neural Network      | 0.929 |

## Model 1 (as in Kaggle.com)

- Label encoder categorical data.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | ROC AUC |       
|----------------------|-------------|-----------|--------|-------|---------|-------|
| Logistic Regression  | 0.912       | 0.851     | 0.655  | 0.413 | 0.506   | 0.928 |
| Decision Tree        | 0.916       | 0.765     | 0.643  | 0.509 | 0.568   | 0.928 |
| Neural Network (MLP) | 0.906       | 0.774     | 0.581  | 0.498 | 0.536   | 0.934 |

## Model 2

- Label encoder categorical data + column "pdays".

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |       
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.913       | 0.842     | 0.655  | 0.416 | 0.509 | 0.928 |
| Decision Tree        | 0.916       | 0.765     | 0.643  | 0.509 | 0.568 | 0.928 |
| Neural Network (MLP) | 0.907       | 0.812     | 0.573  | 0.561 | 0.567 | 0.935 |

## Model 3

- get_dummies for categorical data + column "pdays".

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |     
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.912       | 0.838     | 0.643  | 0.428 | 0.514 | 0.935 |
| Decision Tree        | 0.915       | 0.764     | 0.646  | 0.484 | 0.553 | 0.928 |
| Neural Network (MLP) | 0.907       | 0.775     | 0.586  | 0.498 | 0.538 | 0.937 |

## Model 4

- get_dummies for categorical data + column "pdays".
- exclude columns "euribor3m" and "nr.employed".

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |       
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.912       | 0.790     | 0.646  | 0.429 | 0.516 | 0.934 |
| Decision Tree        | 0.910       | 0.774     | 0.612  | 0.476 | 0.535 | 0.912 |
| Neural Network (MLP) | 0.909       | 0.781     | 0.595  | 0.521 | 0.556 | 0.937 |

## Model 5

- get_dummies for categorical data + column "pdays".
- exclude columns "euribor3m" and "nr.employed".
- SMOTE for oversampling.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |       
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.863       | 0.790     | 0.434  | 0.871 | 0.580 | 0.937 |
| Decision Tree        | 0.841       | 0.774     | 0.393  | 0.853 | 0.538 | 0.921 |
| Neural Network (MLP) | 0.889       | 0.781     | 0.492  | 0.733 | 0.589 | 0.925 |

## Model 6

- get_dummies for categorical data + column "pdays".
- SMOTE for oversampling.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |       
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.865       | 0.838     | 0.440  | 0.876 | 0.585 | 0.938 |
| Decision Tree        | 0.867       | 0.764     | 0.439  | 0.821 | 0.572 | 0.923 |
| Neural Network (MLP) | 0.883       | 0.775     | 0.477  | 0.767 | 0.588 | 0.927 |

## Model 7

- get_dummies for categorical data + column "pdays".
- NearMiss for undersampling.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC   |       
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.856       | 0.838     | 0.417  | 0.823 | 0.553 | 0.910 |
| Decision Tree        | 0.442       | 0.764     | 0.138  | 0.785 | 0.234 | 0.676 |
| Neural Network (MLP) | 0.781       | 0.775     | 0.309  | 0.819 | 0.449 | 0.876 |