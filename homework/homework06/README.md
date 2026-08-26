# Homework 06: Data Preprocessing

## Cleaning Strategy

1. Drop columns with more than 50% missing values.
2. Fill missing numeric values with the median because it is less sensitive to extreme values than the mean.
3. Standardize `age`, `income`, and `score` with z-scores so their scales are comparable.
4. Keep identifiers such as `zipcode` and labels such as `city` unchanged.

Reusable functions are stored in `src/cleaning.py`. The notebook compares the original and cleaned data and saves the result to `data/processed/`.
