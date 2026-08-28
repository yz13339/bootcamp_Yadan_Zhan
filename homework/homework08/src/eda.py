"""Reusable exploratory-data-analysis helpers."""
import pandas as pd

def eda_summary(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Return numeric, missingness, categorical, and attention summaries."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    numeric = df.describe(include="number").T
    missing = pd.DataFrame({"count": df.isna().sum(), "pct": df.isna().mean()})
    categorical = {c: df[c].value_counts(dropna=False).to_frame("count") for c in df.select_dtypes(exclude="number")}
    attention = pd.DataFrame(index=df.columns)
    attention["high_missing"] = missing["pct"] > 0.20
    attention["near_zero_variance"] = [df[c].nunique(dropna=True) <= 1 for c in df]
    attention["dominant_category"] = [df[c].value_counts(normalize=True, dropna=False).max() > .95 for c in df]
    return {"numeric": numeric, "missing": missing, "categorical": categorical, "attention": attention}
