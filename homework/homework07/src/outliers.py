"""Reusable functions for detecting and treating univariate outliers."""

import numpy as np
import pandas as pd


def _numeric_series(series: pd.Series) -> pd.Series:
    """Validate input and return it as a floating-point pandas Series."""
    if not isinstance(series, pd.Series):
        raise TypeError("series must be a pandas Series")
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError("series must contain numeric data")
    return series.astype(float)


def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return a boolean mask for values outside the Tukey IQR fences.

    Missing values are not flagged. ``k`` must be positive. If the series has
    no spread, every non-missing observation is treated as non-outlying.
    """
    values = _numeric_series(series)
    if not np.isfinite(k) or k <= 0:
        raise ValueError("k must be a finite positive number")
    q1, q3 = values.quantile([0.25, 0.75])
    iqr = q3 - q1
    if pd.isna(iqr) or iqr == 0:
        return pd.Series(False, index=values.index, dtype=bool)
    lower, upper = q1 - k * iqr, q3 + k * iqr
    return ((values < lower) | (values > upper)).fillna(False)


def detect_outliers_zscore(
    series: pd.Series, threshold: float = 3.0
) -> pd.Series:
    """Return a boolean mask where absolute population z-score exceeds a threshold.

    Missing values are not flagged. ``threshold`` must be positive. A constant
    or insufficient series produces an all-False mask.
    """
    values = _numeric_series(series)
    if not np.isfinite(threshold) or threshold <= 0:
        raise ValueError("threshold must be a finite positive number")
    standard_deviation = values.std(ddof=0)
    if pd.isna(standard_deviation) or standard_deviation == 0:
        return pd.Series(False, index=values.index, dtype=bool)
    zscores = (values - values.mean()) / standard_deviation
    return zscores.abs().gt(threshold).fillna(False)


def winsorize_series(
    series: pd.Series, lower: float = 0.05, upper: float = 0.95
) -> pd.Series:
    """Return a copy clipped to the requested lower and upper quantiles.

    Bounds must satisfy ``0 <= lower < upper <= 1``. Missing values remain
    missing, and the original index and name are retained.
    """
    values = _numeric_series(series)
    if not (0 <= lower < upper <= 1):
        raise ValueError("quantiles must satisfy 0 <= lower < upper <= 1")
    if values.dropna().empty:
        return values.copy()
    lower_value, upper_value = values.quantile([lower, upper])
    return values.clip(lower=lower_value, upper=upper_value)
