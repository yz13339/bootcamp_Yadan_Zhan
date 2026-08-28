"""Flask prediction API for the Homework 13 regression model."""
from pathlib import Path
import joblib
from flask import Flask, jsonify, request

APP_DIR = Path(__file__).resolve().parent
MODEL = joblib.load(APP_DIR / "model" / "model.pkl")
app = Flask(__name__)

def predict(features):
    """Validate two numeric features and return a scalar prediction."""
    if not isinstance(features, (list, tuple)) or len(features) != 2:
        raise ValueError("features must be a list containing exactly two numbers")
    try: values = [float(value) for value in features]
    except (TypeError, ValueError) as exc: raise ValueError("both features must be numeric") from exc
    return float(MODEL.predict([values])[0])

@app.post("/predict")
def predict_post():
    try:
        payload=request.get_json(silent=True) or {}
        if "features" not in payload: raise ValueError("JSON body must contain the features key")
        return jsonify(prediction=predict(payload["features"]))
    except ValueError as exc: return jsonify(error=str(exc)), 400

@app.get("/predict/<f1>/<f2>")
def predict_get(f1, f2):
    try: return jsonify(prediction=predict([f1,f2]))
    except ValueError as exc: return jsonify(error=str(exc)), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
