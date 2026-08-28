"""Risk-aware model evaluation."""
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def metrics(y,p):
    """Return core classification metrics with safe zero division."""
    return {"accuracy":accuracy_score(y,p),"precision":precision_score(y,p,zero_division=0),"recall":recall_score(y,p,zero_division=0),"f1":f1_score(y,p,zero_division=0)}

def bootstrap_accuracy(y,p,n_boot=1000,seed=5040):
    """Paired bootstrap accuracy with percentile 95% confidence interval."""
    if n_boot<500: raise ValueError("n_boot must be >= 500")
    y,p=np.asarray(y),np.asarray(p); rng=np.random.default_rng(seed); vals=[]
    for _ in range(n_boot):
        idx=rng.integers(0,len(y),len(y)); vals.append((y[idx]==p[idx]).mean())
    vals=np.asarray(vals); return vals,tuple(np.quantile(vals,[.025,.975]))
