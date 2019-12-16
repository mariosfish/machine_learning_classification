# Models

## Paper results

| |Accuracy             | CV Accuracy | 
|:----------|:----------------------|:-------------:|
| Logistic Regression  |    -    | - |  -|  -|
| Decision Tree        | 0.908       | 0.932 | 
| Neural Network (MLP) | 0.908     | 0.935 |

## Model 1 (as in Kaggle.com)

- Label encoder categorical data.

| Models               | Accuracy | CV Accuracy | Precision | Recall | F1    |
|----------------------|----------|-------------|-----------|--------|-------|
| Logistic Regression  | 0.819    | 0.779       | 0.707     | 0.643  | 0.667 |
| Decision Tree        | 0.969    | 0.884       | 0.892     | 0.903  | 0.894 |
| Neural Network (MLP) | 0.925    | 0.898       | 0.845     | 0.807  | 0.815 |

## Model 2

- get_dummies categorical data.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  | 0.929    | 0.833       | 0.833     | 0.854  | 0.843 |
| Decision Tree        | 0.960    | 0.844       | 0.872     | 0.895  | 0.882 |
| Neural Network (MLP) | 0.952    | 0.888       | 0.866     | 0.914  | 0.888 |

## Model 3 

- get_dummies categorical data.
- perform oversampling with SMOTE.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  | 0.792    | 0.833       | 0.381     | 0.455  | 0.397 |
| Decision Tree        | 0.961    | 0.844       | 0.925     | 0.926  | 0.922 |
| Neural Network (MLP) | 0.886    | 0.888       | 0.727     | 0.787  | 0.750 |

## Model 4

- get_dummies categorical data.
- perform undersampling with NearMiss.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  | 0.751    | 0.833       | 0.639     | 0.793  | 0.665 |
| Decision Tree        | 0.601    | 0.844       | 0.715     | 0.721  | 0.595 |
| Neural Network (MLP) | 0.638    | 0.888       | 0.596     | 0.768  | 0.613 |