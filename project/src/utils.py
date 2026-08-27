"""Small validation utilities shared across project stages."""

from __future__ import annotations

import pandas as pd


def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    """Raise a clear error when required dataframe columns are missing."""
    missing = sorted(set(columns) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def summarize_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and shares for columns with missing values."""
    summary = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_share": df.isna().mean(),
    })
    return summary.loc[summary["missing_count"] > 0].sort_values("missing_share", ascending=False)
