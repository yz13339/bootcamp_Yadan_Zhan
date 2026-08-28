"""Leakage-aware multi-asset market-stress features."""
from pathlib import Path
import numpy as np
import pandas as pd

FEATURES=["spy_ret_lag1","vix_change_lag1","spy_vol_20","spy_drawdown","vix_z_60","tlt_ret_lag1","gld_ret_lag1"]

def build_market_features(prices: pd.DataFrame) -> pd.DataFrame:
    """Build past-only features and next-day high-stress target from price levels."""
    df=prices.copy(); df["Date"]=pd.to_datetime(df["Date"],errors="raise"); df=df.sort_values("Date").drop_duplicates("Date").reset_index(drop=True)
    for c in ["SPY","VIX","TLT","GLD"]: df[f"{c.lower()}_ret"]=df[c].pct_change()
    df["spy_ret_lag1"]=df.spy_ret.shift(1); df["vix_change_lag1"]=df.vix_ret.shift(1)
    df["tlt_ret_lag1"]=df.tlt_ret.shift(1); df["gld_ret_lag1"]=df.gld_ret.shift(1)
    df["spy_vol_20"]=df.spy_ret.shift(1).rolling(20).std()
    df["spy_drawdown"]=df.SPY.shift(1)/df.SPY.shift(1).rolling(60).max()-1
    vix_lag=df.VIX.shift(1); df["vix_z_60"]=(vix_lag-vix_lag.rolling(60).mean())/vix_lag.rolling(60).std()
    future_stress=((df.VIX.shift(-1)>=25)|(df.spy_ret.shift(-1)<=-.025)).astype(int)
    future_stress.iloc[-1]=np.nan; df["target_next_high_stress"]=future_stress
    return df

def save_features(input_path, output_path):
    """Build features from a CSV and save them; returns the output path."""
    out=Path(output_path); out.parent.mkdir(parents=True,exist_ok=True)
    build_market_features(pd.read_csv(input_path)).dropna(subset=FEATURES+["target_next_high_stress"]).to_csv(out,index=False)
    return out
