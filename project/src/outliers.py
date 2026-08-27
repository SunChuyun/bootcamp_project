"""Reusable outlier analysis for daily ETF returns."""

from __future__ import annotations

import pandas as pd


def flag_iqr_by_group(
    df: pd.DataFrame,
    column: str,
    group: str = "ticker",
    k: float = 1.5,
) -> pd.Series:
    """Flag observations outside group-specific IQR bounds."""
    if k <= 0:
        raise ValueError("k must be positive")

    def flag(series: pd.Series) -> pd.Series:
        """Apply the IQR rule to one group."""
        q1, q3 = series.quantile([0.25, 0.75])
        iqr = q3 - q1
        return ((series < q1 - k * iqr) | (series > q3 + k * iqr)).fillna(False)

    return df.groupby(group, group_keys=False)[column].apply(flag).sort_index()


def winsorize_by_group(
    df: pd.DataFrame,
    column: str,
    group: str = "ticker",
    lower: float = 0.01,
    upper: float = 0.99,
) -> pd.Series:
    """Cap a numeric column at group-specific lower and upper quantiles."""
    if not 0 <= lower < upper <= 1:
        raise ValueError("require 0 <= lower < upper <= 1")

    def cap(series: pd.Series) -> pd.Series:
        """Clip one group at its selected quantiles."""
        return series.clip(series.quantile(lower), series.quantile(upper))

    return df.groupby(group, group_keys=False)[column].apply(cap).sort_index()
