"""Project configuration and environment-driven paths."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

RAW_DIR = PROJECT_ROOT / os.getenv("DATA_DIR_RAW", "data/raw")
PROCESSED_DIR = PROJECT_ROOT / os.getenv("DATA_DIR_PROCESSED", "data/processed")
REPORTS_DIR = PROJECT_ROOT / "reports"
IMAGES_DIR = REPORTS_DIR / "images"
MODEL_DIR = PROJECT_ROOT / "model"

START_DATE = os.getenv("PROJECT_START_DATE", "2016-01-01")
END_DATE = os.getenv("PROJECT_END_DATE", "2026-08-27")

TICKERS = ["SPY", "EFA", "EEM", "TLT", "IEF", "GLD", "VNQ", "DBC"]
BENCHMARK = "SPY"


def create_project_directories() -> None:
    """Create all output directories used by the cumulative pipeline."""
    for directory in (RAW_DIR, PROCESSED_DIR, REPORTS_DIR, IMAGES_DIR, MODEL_DIR):
        directory.mkdir(parents=True, exist_ok=True)
