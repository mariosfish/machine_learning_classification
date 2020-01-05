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

|        Models        |  MAE  |   MSE  |  RMSE | CV MAE | CV MSE | CV RMSE |
|:--------------------:|:-----:|:------:|:-----:|:------:|:------:|:-------:|
| Linear Regression    | 2.570 | 11.286 | 3.359 |  2.748 | 12.902 |  3.592  |
| Decision Tree        | 2.368 | 12.703 | 3.564 |  2.914 | 16.136 |  4.017  |
| Neural Network (MLP) | 1.752 |  6.876 | 2.622 |  2.802 | 14.255 |  3.776  |

## Model 2

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with Label encoder.

|        Models        |  MAE  |   MSE  |  RMSE | CV MAE | CV MSE | CV RMSE |
|:--------------------:|:-----:|:------:|:-----:|:------:|:------:|:-------:|
| Linear Regression    | 2.500 | 10.754 | 3.279 |  2.693 | 12.550 |  3.543  |
| Decision Tree        | 2.612 | 15.688 | 3.961 |  2.897 | 16.042 |  4.005  |
| Neural Network (MLP) | 1.849 |  7.490 | 2.737 |  3.639 | 21.659 |  4.654  |

## Model 3

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.

|        Models        |  MAE  |   MSE  |  RMSE | CV MAE |  CV MSE | CV RMSE |
|:--------------------:|:-----:|:------:|:-----:|:------:|:-------:|:-------:|
| Linear Regression    | 2.103 |  8.385 | 2.896 |  2.727 |  13.703 |  3.702  |
| Decision Tree        | 3.258 | 22.601 | 4.754 |  3.904 |  28.273 |  5.317  |
| Neural Network (MLP) | 1.834 |  6.554 | 2.560 |  8.205 | 106.624 |  10.326 |

## Model 4

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.
- exclude column `weight` due to high correlation with `discplacement`.

|        Models        |  MAE  |   MSE  |  RMSE | CV MAE | CV MSE | CV RMSE |
|:--------------------:|:-----:|:------:|:-----:|:------:|:------:|:-------:|
| Linear Regression    | 2.128 |  8.736 | 2.956 |  2.832 | 14.330 |  3.785  |
| Decision Tree        | 2.819 | 15.703 | 3.963 |  3.695 | 27.040 |  5.200  |
| Neural Network (MLP) | 1.790 |  6.768 | 2.602 |  5.772 | 59.731 |  7.729  |


## Model 5 (best)

- missing values for `horsepower` replaced with mode of `horsepower`.
- `origin` encoded with get_dummies.
- exclude columns `horsepower` and `displacement` due to high correlation with `weight`.


|        Models        |  MAE  |   MSE  |  RMSE | CV MAE | CV MSE | CV RMSE |
|:--------------------:|:-----:|:------:|:-----:|:------:|:------:|:-------:|
| Linear Regression    | 2.533 | 11.211 | 3.348 |  2.748 | 12.804 |  3.578  |
| Decision Tree        | 2.407 | 12.784 | 3.576 |  2.733 | 14.801 |  3.847  |
| Neural Network (MLP) | 1.924 |  6.794 | 2.607 |  2.451 | 11.271 |  3.357  |