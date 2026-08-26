"""Reusable ETF-style feature engineering functions."""

from __future__ import annotations

import pandas as pd


def add_momentum(df: pd.DataFrame, periods: int = 5) -> pd.DataFrame:
    """Add per-ticker percentage price change over the selected lookback."""
    if periods <= 0:
        raise ValueError("periods must be positive")
    result = df.sort_values(["ticker", "date"]).copy()
    result[f"momentum_{periods}d"] = result.groupby("ticker")["close"].pct_change(periods)
    return result


def add_rolling_volatility(df: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    """Add per-ticker rolling standard deviation of daily returns."""
    if window <= 1:
        raise ValueError("window must be greater than one")
    result = df.sort_values(["ticker", "date"]).copy()
    result[f"volatility_{window}d"] = result.groupby("ticker")["daily_return"].transform(
        lambda values: values.rolling(window, min_periods=window).std()
    )
    return result


def add_ticker_one_hot(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode the nominal ticker column without imposing an order."""
    encoded = pd.get_dummies(df["ticker"], prefix="ticker", dtype=int)
    return pd.concat([df.copy(), encoded], axis=1)
