"""Leakage-aware feature engineering for daily price data."""
import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create past-only return, volatility, momentum, and weekday features."""
    required = {"date", "close"}
    if not required.issubset(df.columns):
        raise KeyError(f"Required columns: {sorted(required)}")
    out = df.copy().sort_values("date").reset_index(drop=True)
    out["date"] = pd.to_datetime(out["date"], errors="raise")
    out["return"] = out["close"].pct_change()
    out["return_lag1"] = out["return"].shift(1)
    out["rolling_mean_5"] = out["return"].shift(1).rolling(5).mean()
    out["rolling_std_10"] = out["return"].shift(1).rolling(10).std()
    out["momentum_5"] = out["close"].shift(1).pct_change(5)
    out["day_name"] = out["date"].dt.day_name()
    out = pd.get_dummies(out, columns=["day_name"], prefix="dow", dtype=int)
    out["target_next_return"] = out["return"].shift(-1)
    return out
