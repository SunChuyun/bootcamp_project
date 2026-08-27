"""Yahoo Finance acquisition for the project ETF universe."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pandas as pd
import yfinance as yf


def download_etf_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted daily close and volume data in long format."""
    cache_dir = Path(tempfile.gettempdir()) / "bootcamp_yfinance_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    yf.set_tz_cache_location(str(cache_dir))

    downloaded = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
        threads=False,
    )
    if downloaded.empty:
        raise ValueError("Yahoo Finance returned no observations")

    close = (
        downloaded["Close"]
        .rename_axis(index="date", columns="ticker")
        .stack(future_stack=True)
        .rename("close")
    )
    volume = (
        downloaded["Volume"]
        .rename_axis(index="date", columns="ticker")
        .stack(future_stack=True)
        .rename("volume")
    )
    prices = pd.concat([close, volume], axis=1).reset_index()
    prices["date"] = pd.to_datetime(prices["date"]).dt.tz_localize(None)

    received = set(prices["ticker"].unique())
    missing = sorted(set(tickers) - received)
    if missing:
        raise ValueError(f"No downloaded observations for: {missing}")
    return prices.sort_values(["ticker", "date"]).reset_index(drop=True)
