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

- get_dummies categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.816       | 0.779     | 0.670  | 0.352 | 0.462 | 0.771 |
| Decision Tree        | 0.814       | 0.818     | 0.700  | 0.301 | 0.421 | 0.719 |
| Neural Network (MLP) | 0.812       | 0.779     | 0.641  | 0.365 | 0.466 | 0.764 |

## Model 4

- get_dummies categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.816       | 0.779     | 0.671  | 0.352 | 0.461 | 0.771 |
| Decision Tree        | 0.814       | 0.818     | 0.700  | 0.301 | 0.421 | 0.719 |
| Neural Network (MLP) | 0.816       | 0.779     | 0.665  | 0.359 | 0.467 | 0.769 |

## Model 5

- Label encoding categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.680       | 0.779     | 0.365  | 0.577 | 0.448 | 0.692 |
| Decision Tree        | 0.715       | 0.821     | 0.407  | 0.590 | 0.482 | 0.714 |
| Neural Network (MLP) | 0.730       | 0.655     | 0.429  | 0.612 | 0.505 | 0.748 |

## Model 6

- get_dummies categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.813       | 0.779     | 0.644  | 0.371 | 0.471 | 0.757 |
| Decision Tree        | 0.786       | 0.818     | 0.522  | 0.529 | 0.526 | 0.724 |
| Neural Network (MLP) | 0.802       | 0.779     | 0.588  | 0.397 | 0.474 | 0.754 |

## Model 7

- Label encoding categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC          |
|----------------------|-------------|-----------|--------|-------|-------|-------|
| Logistic Regression  | 0.405       | 0.779     | 0.225  | 0.675 | 0.337 | 0.448 |
| Decision Tree        | 0.532       | 0.821     | 0.246  | 0.524 | 0.335 | 0.489 |
| Neural Network (MLP) | 0.398       | 0.655     | 0.228  | 0.704 | 0.344 | 0.436 |

## Model 8

- get_dummies categorical data (`'PAY_1'`, `'PAY_2'`, `'PAY_3'`, `'PAY_4'`, `'PAY_5'`, `'PAY_6'`).
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

| |Accuracy             | CV Accuracy | Precision | Recall | F1    | AUC         |
|----------------------|-------------|-----------|--------|-------|-------|------|
| Logistic Regression  | 0.430       | 0.779     | 0.232  | 0.669 | 0.345 | 0.48 |
| Decision Tree        | 0.516       | 0.818     | 0.233  | 0.506 | 0.319 | 0.48 |
| Neural Network (MLP) | 0.407       | 0.779     | 0.228  | 0.687 | 0.342 | 0.45 |
