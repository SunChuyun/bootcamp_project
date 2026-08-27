"""Two-route Flask API for the Stage 13 homework regression model."""

from __future__ import annotations

from pathlib import Path

from flask import Flask, jsonify, request
import joblib


MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.pkl"
MODEL = joblib.load(MODEL_PATH)
EXPECTED_FEATURES = 2

app = Flask(__name__)


# --- Prediction helpers --- #

def make_prediction(features: object) -> float:
    """Validate two numeric features and return one prediction."""
    if not isinstance(features, list) or len(features) != EXPECTED_FEATURES:
        raise ValueError("features must be a list containing exactly two values")
    try:
        numeric_features = [float(value) for value in features]
    except (TypeError, ValueError) as exc:
        raise ValueError("both features must be numeric") from exc
    return float(MODEL.predict([numeric_features])[0])


# --- API routes --- #

@app.post("/predict")
def predict_post() -> tuple[object, int]:
    """Predict from a JSON body containing a two-value features list."""
    payload = request.get_json(silent=True)
    try:
        features = payload.get("features") if isinstance(payload, dict) else None
        return jsonify({"prediction": make_prediction(features)}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@app.get("/predict/<f1>/<f2>")
def predict_get(f1: str, f2: str) -> tuple[object, int]:
    """Predict from two numeric path parameters."""
    try:
        return jsonify({"prediction": make_prediction([f1, f2])}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False, use_reloader=False)
