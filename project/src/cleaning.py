"""Reusable cleaning functions for ETF price data."""

from __future__ import annotations

import pandas as pd

from src.utils import require_columns


def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    """Parse, validate, deduplicate, and sort the raw ETF observations."""
    require_columns(df, ["date", "ticker", "close", "volume"])
    result = df.copy()
    result["date"] = pd.to_datetime(result["date"], errors="coerce")
    result["ticker"] = result["ticker"].astype("string").str.strip()
    result["close"] = pd.to_numeric(result["close"], errors="coerce")
    result["volume"] = pd.to_numeric(result["volume"], errors="coerce").fillna(0.0)

    result.loc[result["close"] <= 0, "close"] = pd.NA
    result = result.dropna(subset=["date", "ticker", "close"])
    result = result.drop_duplicates(subset=["date", "ticker"], keep="last")
    return result.sort_values(["ticker", "date"]).reset_index(drop=True)
