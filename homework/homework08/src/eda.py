"""Reusable exploratory-data-analysis summaries."""

from __future__ import annotations

import pandas as pd


def eda_summary(df: pd.DataFrame) -> dict[str, object]:
    """Return structure, missingness, numeric profiles, categories, and attention flags."""
    numeric = df.select_dtypes(include="number")
    categorical = df.select_dtypes(include=["object", "category", "bool"])

    profile = numeric.describe().T
    if not profile.empty:
        profile["skew"] = numeric.skew()
        profile["kurtosis"] = numeric.kurtosis()

    category_profile = {
        column: categorical[column].value_counts(dropna=False).to_dict()
        for column in categorical.columns
    }
    attention = {
        "high_missing": df.columns[df.isna().mean() > 0.20].tolist(),
        "near_zero_variance": numeric.columns[numeric.nunique(dropna=True) <= 1].tolist(),
        "dominant_category": [
            column
            for column in categorical.columns
            if not categorical[column].dropna().empty
            and categorical[column].value_counts(normalize=True, dropna=True).iloc[0] > 0.90
        ],
    }
    return {
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
        "missing": df.isna().sum().to_dict(),
        "numeric_profile": profile,
        "categorical_profile": category_profile,
        "attention": attention,
    }
