"""Feature engineering for ETF prices and returns."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.utils import require_columns


def add_market_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add return, momentum, volatility, drawdown, and future-return columns."""
    require_columns(df, ["date", "ticker", "close", "volume"])
    result = df.sort_values(["ticker", "date"]).copy()
    grouped_close = result.groupby("ticker")["close"]
    result["return_1d"] = grouped_close.pct_change(fill_method=None)
    result["momentum_21d"] = grouped_close.pct_change(21, fill_method=None)
    result["momentum_63d"] = grouped_close.pct_change(63, fill_method=None)
    result["momentum_126d"] = grouped_close.pct_change(126, fill_method=None)
    result["volatility_21d"] = result.groupby("ticker")["return_1d"].transform(
        lambda values: values.rolling(21, min_periods=21).std() * np.sqrt(252)
    )
    rolling_high = grouped_close.transform(lambda values: values.rolling(63, min_periods=63).max())
    result["drawdown_63d"] = result["close"] / rolling_high - 1
    result["next_day_return"] = result.groupby("ticker")["return_1d"].shift(-1)
    return result


def add_ticker_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add one-hot indicators for the nominal ticker field."""
    indicators = pd.get_dummies(df["ticker"], prefix="ticker", dtype=int)
    return pd.concat([df.copy(), indicators], axis=1)
