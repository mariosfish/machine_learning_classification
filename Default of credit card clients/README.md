# Models

## Model 1 

- data set as is (no encoding).

## Model 2

- Label encoding categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').

## Model 3

- get_dummies categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').

## Model 4

- get_dummies categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

## Model 5

- Label encoding categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

## Model 6

- get_dummies categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').
- perform oversampling with SMOTE.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

## Model 7

- Label encoding categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.

## Model 8

- Label encoding categorical data ('PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6').
- perform undersampling with NearMiss.
- exclude features `BILL_ATM2`,..., `BILL_ATM6`.