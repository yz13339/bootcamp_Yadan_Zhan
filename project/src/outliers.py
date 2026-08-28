"""Outlier detection for market-return series."""
import pandas as pd

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Flag values outside Tukey IQR fences; missing values are not flagged."""
    if k <= 0: raise ValueError("k must be positive")
    if not pd.api.types.is_numeric_dtype(series): raise TypeError("series must be numeric")
    q1,q3=series.quantile([.25,.75]); spread=q3-q1
    if pd.isna(spread) or spread==0: return pd.Series(False,index=series.index,dtype=bool)
    return ((series<q1-k*spread)|(series>q3+k*spread)).fillna(False)

def winsorize_series(series: pd.Series, lower=.01, upper=.99) -> pd.Series:
    """Clip a numeric series to selected quantiles without changing row count."""
    if not 0 <= lower < upper <= 1: raise ValueError("require 0 <= lower < upper <= 1")
    lo,hi=series.quantile([lower,upper]); return series.clip(lo,hi)
