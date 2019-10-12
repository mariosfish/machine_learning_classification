# Models for  Auto MPG Data set

## Model 1 (as in Kaggle.com)

- missing values for `horsepower` replaced with the mean of `horsepower`.
- all columns are numbers.

## Model 2

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with Label encoder.

## Model 3 (best)

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.

## Model 4

- missing values for `horsepower` replaced with the mean of `horsepower`.
- `cylinders`, `model year` and `origin` as category.
- categorical data encoded with get_dummies.
- exclude column `weight` due to high correlation with `discplacement`.
