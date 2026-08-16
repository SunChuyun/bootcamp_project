"""Reusable data-summary functions for Homework 3."""

import pandas as pd


# --- Summary statistics --- #

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for the numeric columns in a DataFrame."""
    return df.select_dtypes(include="number").describe()
