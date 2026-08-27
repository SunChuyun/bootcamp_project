"""Reusable exploratory-data-analysis summaries."""

from __future__ import annotations

import pandas as pd


def eda_summary(df: pd.DataFrame) -> dict[str, object]:
    """Return structure, missingness, numeric profiles, and date coverage."""
    numeric = df.select_dtypes(include="number")
    profile = numeric.describe().T
    if not profile.empty:
        profile["skew"] = numeric.skew()
        profile["kurtosis"] = numeric.kurtosis()

    return {
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
        "missing": df.isna().sum().to_dict(),
        "numeric_profile": profile,
        "date_min": df["date"].min(),
        "date_max": df["date"].max(),
        "rows_by_ticker": df.groupby("ticker").size().to_dict(),
    }
