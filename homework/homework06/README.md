# Homework 06: Data Preprocessing

This submission applies modular cleaning functions to SPY daily market data. Run `homework06_data-preprocessing_submission.ipynb` from top to bottom with the `bootcamp_env` kernel.

## Cleaning Strategy

The raw exercise file in `data/raw/` is copied from Homework 04's SPY CSV. Because the original file is complete, four cells were deliberately blanked to demonstrate the required preprocessing operations: `Close`, `Open`, `Volume`, and `Date`. The original Homework 04 file remains unchanged.

- Missing `Close` and `Open` prices are replaced with each column's median. Median imputation retains rows and is less sensitive to extreme values than a mean, but it reduces natural variation.
- Rows missing critical identifiers (`Date`) or activity (`Volume`) are dropped because those values should not be inferred. This removes two of 252 rows and may introduce bias if missingness is systematic.
- Price columns (`Adj Close`, `Close`, `High`, `Low`, and `Open`) are min-max normalized to `[0, 1]`, making their scales comparable. `Volume` is intentionally left in its original units for interpretability.
- The raw file is never overwritten. The cleaned result is saved to `data/processed/spy_preprocessing_cleaned.csv`.

Reusable functions live in `src/cleaning.py`. Each function returns a copy rather than mutating its input, validates requested columns, and documents edge-case behavior.
