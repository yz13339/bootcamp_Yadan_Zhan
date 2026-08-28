"""Flask API for next-day multi-asset market-stress probability."""
from pathlib import Path
import joblib
import pandas as pd
from flask import Flask,jsonify,request

ROOT=Path(__file__).resolve().parent
BUNDLE=joblib.load(ROOT/"model/market_stress_model.pkl")
MODEL,FEATURES=BUNDLE["model"],BUNDLE["features"]
app=Flask(__name__)

@app.get("/health")
def health(): return jsonify(status="ok",model="market_stress_classifier",feature_count=len(FEATURES))

@app.post("/predict")
def predict():
    try:
        payload=request.get_json(silent=True) or {}; supplied=payload.get("features")
        if not isinstance(supplied,dict): raise ValueError("features must be a JSON object")
        missing=[x for x in FEATURES if x not in supplied]
        if missing: raise ValueError(f"missing features: {missing}")
        row=pd.DataFrame([[float(supplied[x]) for x in FEATURES]],columns=FEATURES)
        probability=float(MODEL.predict_proba(row)[0,1]); return jsonify(high_stress_probability=probability,high_stress_flag=int(probability>=.5))
    except (ValueError,TypeError) as exc: return jsonify(error=str(exc)),400

if __name__=="__main__": app.run(host="127.0.0.1",port=5051,debug=False)
