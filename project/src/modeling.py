"""Training helpers for the next-day market-stress classifier."""
from pathlib import Path
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from .features import FEATURES

def make_pipeline(class_weight=None):
    """Create a scaled, reproducible logistic-regression pipeline."""
    return Pipeline([("scale",StandardScaler()),("model",LogisticRegression(max_iter=2000,class_weight=class_weight,random_state=5040))])

def train_time_split(df, train_fraction=.8, class_weight=None):
    """Fit on the earliest observations and return model plus train/test frames."""
    if not 0 < train_fraction < 1: raise ValueError("train_fraction must be between 0 and 1")
    cut=int(len(df)*train_fraction); train,test=df.iloc[:cut],df.iloc[cut:]
    model=make_pipeline(class_weight); model.fit(train[FEATURES],train.target_next_high_stress.astype(int))
    return model,train,test

def save_bundle(model,path):
    """Persist model and feature contract together."""
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); joblib.dump({"model":model,"features":FEATURES},path); return path
