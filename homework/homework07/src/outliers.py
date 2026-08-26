"""Reusable outlier detection and treatment functions."""

from __future__ import annotations

import pandas as pd


def _validate_series(series: pd.Series) -> pd.Series:
    """Validate and return a numeric, non-empty series."""
    if series.empty:
        raise ValueError("series must not be empty")
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError("series must be numeric")
    return series


def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Flag values outside Q1 - k*IQR and Q3 + k*IQR; NaNs are not flagged."""
    series = _validate_series(series)
    if k <= 0:
        raise ValueError("k must be positive")
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    return ((series < q1 - k * iqr) | (series > q3 + k * iqr)).fillna(False)


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Flag absolute population z-scores above threshold; NaNs are not flagged."""
    series = _validate_series(series)
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    sigma = series.std(ddof=0)
    if sigma == 0 or pd.isna(sigma):
        return pd.Series(False, index=series.index)
    return (((series - series.mean()) / sigma).abs() > threshold).fillna(False)


def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    """Cap a numeric series at the selected lower and upper quantiles."""
    series = _validate_series(series)
    if not 0 <= lower < upper <= 1:
        raise ValueError("require 0 <= lower < upper <= 1")
    return series.clip(lower=series.quantile(lower), upper=series.quantile(upper))
