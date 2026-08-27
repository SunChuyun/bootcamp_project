"""Flask API for the fitted ETF next-day return model."""

from __future__ import annotations

from pathlib import Path

from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd


MODEL_PATH = Path(__file__).resolve().parent / "model" / "return_model.pkl"
MODEL_BUNDLE = joblib.load(MODEL_PATH)
MODEL = MODEL_BUNDLE["model"]
FEATURE_NAMES = MODEL_BUNDLE["features"]

app = Flask(__name__)


# --- Input validation --- #

def parse_feature_payload(payload: object) -> pd.DataFrame:
    """Validate a keyed feature payload and return one model-ready row."""
    if not isinstance(payload, dict) or not isinstance(payload.get("features"), dict):
        raise ValueError("JSON must contain a 'features' object")

    features = payload["features"]
    missing = [name for name in FEATURE_NAMES if name not in features]
    extra = [name for name in features if name not in FEATURE_NAMES]
    if missing or extra:
        raise ValueError(f"Feature mismatch. Missing: {missing}; extra: {extra}")

    try:
        values = [float(features[name]) for name in FEATURE_NAMES]
    except (TypeError, ValueError) as exc:
        raise ValueError("All feature values must be numeric") from exc
    if not np.isfinite(values).all():
        raise ValueError("All feature values must be finite")
    return pd.DataFrame([values], columns=FEATURE_NAMES)


# --- API routes --- #

@app.get("/health")
def health() -> tuple[object, int]:
    """Report whether the model is loaded and ready."""
    return jsonify({"status": "ok", "feature_count": len(FEATURE_NAMES)}), 200


@app.post("/predict")
def predict() -> tuple[object, int]:
    """Return one next-day return prediction from a JSON feature mapping."""
    try:
        model_input = parse_feature_payload(request.get_json(silent=True))
        prediction = float(MODEL.predict(model_input)[0])
        return jsonify({"prediction": prediction}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)
