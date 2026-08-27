"""Time-aware linear-regression baseline for next-day ETF returns."""

from __future__ import annotations

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd

from src.features import add_ticker_indicators


BASE_FEATURES = [
    "return_1d",
    "momentum_21d",
    "momentum_63d",
    "momentum_126d",
    "volatility_21d",
    "drawdown_63d",
]


def prepare_model_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """Create a chronological 80/20 split and aligned model columns."""
    encoded = add_ticker_indicators(df)
    ticker_features = sorted(column for column in encoded.columns if column.startswith("ticker_"))
    feature_columns = BASE_FEATURES + ticker_features
    model_data = encoded.dropna(subset=feature_columns + ["next_day_return"]).copy()

    dates = model_data["date"].sort_values().unique()
    split_date = dates[int(len(dates) * 0.8)]
    train = model_data.loc[model_data["date"] < split_date].copy()
    test = model_data.loc[model_data["date"] >= split_date].copy()
    return train, test, feature_columns


def fit_return_model(
    train: pd.DataFrame,
    test: pd.DataFrame,
    feature_columns: list[str],
) -> tuple[Pipeline, pd.DataFrame]:
    """Fit a standardized linear regression and return dated test predictions."""
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("linear_regression", LinearRegression()),
    ])
    model.fit(train[feature_columns], train["next_day_return"])
    predictions = test[["date", "ticker", "next_day_return"]].copy()
    predictions["predicted_return"] = model.predict(test[feature_columns])
    return model, predictions
