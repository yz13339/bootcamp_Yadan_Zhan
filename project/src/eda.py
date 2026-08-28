"""Project EDA summaries."""
import pandas as pd

def eda_summary(df: pd.DataFrame) -> dict:
    """Return shapes, dtypes, missingness, numeric statistics, skew and kurtosis."""
    return {"shape":df.shape,"dtypes":df.dtypes.astype(str).to_frame("dtype"),"missing":df.isna().sum().to_frame("missing"),"numeric":df.describe(include="number").T,"skew_kurt":df.select_dtypes("number").agg(["skew","kurt"]).T}
