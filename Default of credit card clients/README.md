# Models

## Paper results


### 1) The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications 36 (2009) 2473–2480

|                     | Error rate | Accuracy |
|---------------------|:----------:|:--------:|
| Logistic Regression |    0.18    |   0.82   |
| Decision tree       |    0.17    |   0.83   |
| Neural Network      |    0.17    |   0.83   |

### 2) Liu,  R.L.  (2018) Machine  Learning  Approaches  to  Predict Default  of  Credit  Card  Clients. Modern Economy, 9, 1828-1838. 

|                | Accuracy |   F1   |
|----------------|:--------:|:------:|
|  Decision tree |  0.7973  | 0.4912 |
| Neural Network |  0.8227  | 0.4593 |

## Model 1

- data set as is (no encoding).

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.808       | 0.779     | 0.724  | 0.232 | 0.351 | 0.727 |
| Decision Tree        | 0.818       | 0.821     | 0.671  | 0.375 | 0.481 | 0.733 |
| Neural Network (MLP) | 0.818       | 0.779     | 0.662  | 0.383 | 0.485 | 0.769 |

## Model 2

- Label encoding categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.805       | 0.779     | 0.693  | 0.236 | 0.353 | 0.729 |
| Decision Tree        | 0.818       | 0.821     | 0.671  | 0.375 | 0.481 | 0.733 |
| Neural Network (MLP) | 0.817       | 0.779     | 0.671  | 0.365 | 0.473 | 0.767 |

## Model 3

- get_dummies categorical data (`'EDUCATION'`,`'MARRIAGE'`,`'SEX'`,`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.817       | 0.779     | 0.677  | 0.353 | 0.464 | 0.772 |
| Decision Tree        | 0.814       | 0.818     | 0.700  | 0.301 | 0.421 | 0.719 |
| Neural Network (MLP) | 0.813       | 0.779     | 0.652  | 0.357 | 0.462 | 0.765 |

## Model 4

- get_dummies categorical data (`'EDUCATION'`,`'MARRIAGE'`,`'SEX'`,`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.817       | 0.779     | 0.677  | 0.353 | 0.464 | 0.771 |
| Decision Tree        | 0.814       | 0.818     | 0.700  | 0.301 | 0.421 | 0.719 |
| Neural Network (MLP) | 0.817       | 0.777     | 0.650  | 0.371 | 0.472 | 0.769 |

## Model 5

- Label encoding categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.681       | 0.779     | 0.366  | 0.576 | 0.448 | 0.690 |
| Decision Tree        | 0.718       | 0.821     | 0.409  | 0.581 | 0.480 | 0.715 |
| Neural Network (MLP) | 0.742       | 0.664     | 0.443 | 0.584 | 0.504 | 0.748 |

## Model 6

- get_dummies categorical data (`'EDUCATION'`,`'MARRIAGE'`,`'SEX'`,`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.817       | 0.779     | 0.678  | 0.355 | 0.466 | 0.771 |
| Decision Tree        | 0.786       | 0.818     | 0.522  | 0.529 | 0.526 | 0.729 |
| Neural Network (MLP) | 0.812       | 0.777    | 0.644  | 0.360 | 0.462 | 0.768 |

## Model 7

- Label encoding categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.405       | 0.779     | 0.226  | 0.680 | 0.339 | 0.448 |
| Decision Tree        | 0.532       | 0.821     | 0.246  | 0.524 | 0.335 | 0.489 |
| Neural Network (MLP) | 0.403       | 0.664     | 0.231  | 0.710 | 0.348 | 0.438 |

## Model 8

- get_dummies categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC         |
|----------------------|-------------|-----------|--------|-------|-------|------|
| Logistic Regression  | 0.430       | 0.779     | 0.232  | 0.668 | 0.345 | 0.482 |
| Decision Tree        | 0.516       | 0.818     | 0.233  | 0.506 | 0.319 | 0.480 |
| Neural Network (MLP) | 0.413       | 0.777    | 0.229  | 0.684 | 0.343 | 0.453 |
