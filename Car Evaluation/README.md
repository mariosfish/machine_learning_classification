# Models

## Paper results

| |Accuracy             | CV Accuracy | 
|:----------|:----------------------|:-------------:|
| Logistic Regression  |    -    | - |  -|  -|
| Decision Tree        | 0.908       | 0.932 | 
| Neural Network (MLP) | 0.908     | 0.935 |

## Model 1 (as in Kaggle.com)

- Label encoder categorical data.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  |   0.819  |    0.779    |   0.707   |  0.643 | 0.667 |
| Decision Tree        |   0.967  |    0.879    |   0.914   |  0.920 | 0.916 |
| Neural Network (MLP) |   0.925  |    0.898    |   0.845   |  0.807 | 0.815 |

## Model 2

- get_dummies categorical data.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  |   0.929  |    0.833    |   0.833   |  0.854 | 0.843 |
| Decision Tree        |   0.958  |    0.839    |   0.876   |  0.905 | 0.888 |
| Neural Network (MLP) |   0.952  |    0.888    |   0.866   |  0.914 | 0.888 |

## Model 2 with K-means

- get_dummies categorical data.
- perform feature selection.
- perform k-means

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  |   0.934  |    0.849    |   0.835   |  0.850 | 0.842 |
| Decision Tree        |   0.961  |    0.869    |   0.893   |  0.930 | 0.909 |
| Neural Network (MLP) |   0.950  |    0.871    |   0.850   |  0.893 | 0.867 |

## Model 3 

- get_dummies categorical data.
- perform oversampling with SMOTE.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  |   0.792  |    0.833    |   0.381   |  0.455 | 0.397 |
| Decision Tree        |   0.954  |    0.839    |   0.889   |  0.908 | 0.898 |
| Neural Network (MLP) |   0.884  |    0.888    |   0.712   |  0.752 | 0.722 |

## Model 4

- get_dummies categorical data.
- perform undersampling with NearMiss.

|        Models        | Accuracy | CV Accuracy | Precision | Recall |   F1  |
|:--------------------:|:--------:|:-----------:|:---------:|:------:|:-----:|
| Logistic Regression  | 0.751    | 0.833       | 0.639     | 0.793  | 0.665 |
| Decision Tree        | 0.601    | 0.844       | 0.715     | 0.721  | 0.595 |
| Neural Network (MLP) | 0.638    | 0.888       | 0.596     | 0.768  | 0.613 |