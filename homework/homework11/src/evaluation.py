"""Bootstrap and classification evaluation helpers."""
import numpy as np

def classification_metrics(y_true, y_pred):
    """Return accuracy, precision, recall, and F1 without zero-division errors."""
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    tp=((y_true==1)&(y_pred==1)).sum(); fp=((y_true==0)&(y_pred==1)).sum(); fn=((y_true==1)&(y_pred==0)).sum()
    accuracy=(y_true==y_pred).mean(); precision=tp/(tp+fp) if tp+fp else 0.; recall=tp/(tp+fn) if tp+fn else 0.
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.
    return {"accuracy":accuracy,"precision":precision,"recall":recall,"f1":f1}

def bootstrap_metric(y_true, y_pred, metric_fn, n_boot=1000, seed=5040):
    """Bootstrap paired observations and return estimates plus a percentile 95% CI."""
    if n_boot < 500: raise ValueError("n_boot must be at least 500")
    y_true, y_pred=np.asarray(y_true),np.asarray(y_pred); rng=np.random.default_rng(seed); values=[]
    for _ in range(n_boot):
        idx=rng.integers(0,len(y_true),len(y_true)); values.append(metric_fn(y_true[idx],y_pred[idx]))
    values=np.asarray(values)
    return values, tuple(np.quantile(values,[.025,.975]))
