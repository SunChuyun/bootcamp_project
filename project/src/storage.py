"""CSV and Parquet storage utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_df(df: pd.DataFrame, path: str | Path) -> Path:
    """Write a dataframe according to a CSV or Parquet file suffix."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".csv":
        df.to_csv(output, index=False)
    elif output.suffix.lower() == ".parquet":
        df.to_parquet(output, index=False)
    else:
        raise ValueError("Supported output formats are .csv and .parquet")
    return output


def read_df(path: str | Path, parse_dates: list[str] | None = None) -> pd.DataFrame:
    """Read a dataframe according to a CSV or Parquet file suffix."""
    source = Path(path)
    if source.suffix.lower() == ".csv":
        return pd.read_csv(source, parse_dates=parse_dates)
    if source.suffix.lower() == ".parquet":
        return pd.read_parquet(source)
    raise ValueError("Supported input formats are .csv and .parquet")
