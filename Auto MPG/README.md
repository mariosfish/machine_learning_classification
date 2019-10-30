# Models for  Auto MPG Data set

## Quinlan's results

| |Mean squared error (MSE) | Mean absolute error (MAE)       |
|--------------------------|---------------------------|------|
| Linear Regression        | 19.4                      | 2.61 |
| Decision tree            | 14.7                      | 2.11 |
| Neural Network           | 12.5                      | 2.02 |

## Model 1 (as in Kaggle.com)

- missing values for `horsepower` replaced with the mean of `horsepower`.
- all columns are numbers.

| |MSE                  | MAE    | CV Accuracy | Accuracy |       
|----------------------|--------|-------------|----------|-------|
| Linear Regression    | 11.293 | 2.570       | 0.806    | 0.811 |
| Decision Tree        | 13.965 | 2.660       | 0.811    | 0.766 |
| Neural Network (MLP) | 6.894  | 1.749       | 0.850    | 0.884 |

## Model 2

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with Label encoder.

| |MSE                  | MAE    | CV Accuracy | Accuracy |       
|----------------------|--------|-------------|----------|-------|
| Linear Regression    | 10.754 | 2.500       | 0.571    | 0.820 |
| Decision Tree        | 13.965 | 2.660       | 0.549    | 0.766 |
| Neural Network (MLP) | 7.490  | 1.849       | 0.391    | 0.874 |

## Model 3 (best)

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.

| |MSE                  | MAE    | CV Accuracy | Accuracy |       
|----------------------|--------|-------------|----------|-------|
| Linear Regression    | 8.385  | 2.103       | 0.834    | 0.859 |
| Decision Tree        | 21.924 | 3.472       | 0.740    | 0.633 |
| Neural Network (MLP) | 6.554  | 1.834       | 0.822    | 0.890 |

## Model 4

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.
- exclude column `weight` due to high correlation with `discplacement`.

| |MSE                  | MAE    | CV Accuracy | Accuracy        |
|----------------------|--------|-------------|----------|-------|
| Linear Regression    | 9.957  | 2.265       | 0.807    | 0.833 |
| Decision Tree        | 19.354 | 3.259       | 0.681    | 0.676 |
| Neural Network (MLP) | 7.431  | 1.945       | 0.814    | 0.875 |


