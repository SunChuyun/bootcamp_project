"""Reusable data-cleaning functions for Homework 06."""

from __future__ import annotations

import pandas as pd


def fill_missing_median(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """Return a copy with missing numeric values filled by column medians."""
    result = df.copy()
    selected = columns or result.select_dtypes(include="number").columns.tolist()
    for column in selected:
        result[column] = result[column].fillna(result[column].median())
    return result


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns whose missing-value share is greater than threshold."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    missing_share = df.isna().mean()
    return df.drop(columns=missing_share[missing_share > threshold].index).copy()


def normalize_data(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return a copy with selected columns standardized to z-scores."""
    result = df.copy()
    for column in columns:
        mean = result[column].mean()
        std = result[column].std(ddof=0)
        result[column] = 0.0 if std == 0 else (result[column] - mean) / std
    return result
