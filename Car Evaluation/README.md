# Models

## Paper results

| |Accuracy             | CV Accuracy | 
|:----------|:----------------------|:-------------:|
| Logistic Regression  |    -    | - |  -|  -|
| Decision Tree        | 0.908       | 0.932 | 
| Neural Network (MLP) | 0.908     | 0.935 |

## Model 1 (as in Kaggle.com)

- Label encoder categorical data.

| |Accuracy             | CV Accuracy | MSE   | MAE          |
|----------------------|-------------|-------|-------|-------|
| Logistic Regression  | 0.819       | 0.779 | 0.306 | 0.218 |
| Decision Tree        | 0.869       | 0.802 | 0.189 | 0.150 |
| Neural Network (MLP) | 0.925       | 0.897 | 0.116 | 0.089 |

## Model 2

- get_dummies categorical data.

|| Accuracy             | CV Accuracy | MSE   | MAE         |
|----------------------|-------------|-------|-------|-------|
| Logistic Regression  | 0.929       | 0.833 | 0.089 | 0.077 |
| Decision Tree        | 0.869       | 0.804 | 0.229 | 0.164 |
| Neural Network (MLP) | 0.952       | 0.898 | 0.066 | 0.054 |

## Model 3 

- get_dummies categorical data.
- perform oversampling with SMOTE.

| |Accuracy             | CV Accuracy | MSE   | MAE          |
|----------------------|-------------|-------|-------|-------|
| Logistic Regression  | 0.792       | 0.833 | 0.347 | 0.254 |
| Decision Tree        | 0.763       | 0.804 | 0.393 | 0.289 |
| Neural Network (MLP) | 0.906       | 0.898 | 0.146 | 0.112 |

## Model 4

- get_dummies categorical data.
- perform undersampling with NearMiss.

| |Accuracy             | CV Accuracy | MSE   | MAE         |
|----------------------|-------------|-------|-------|-------|
| Logistic Regression  | 0.751       | 0.833 | 0.382 | 0.293 |
| Decision Tree        | 0.557       | 0.804 | 1.264 | 0.717 |
| Neural Network (MLP) | 0.638       | 0.898 | 0.551 | 0.424 |
