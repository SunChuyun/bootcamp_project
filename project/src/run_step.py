"""CLI wrapper for the idempotent reporting step of the ETF pipeline."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd

from src.evaluation import strategy_metrics


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "processed" / "monthly_backtest.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "reports" / "orchestration_metrics.csv"
DEFAULT_LOG = PROJECT_ROOT / "reports" / "pipeline.log"


# --- Logging --- #

def configure_logging(log_path: Path) -> None:
    """Configure one file and one console handler for the CLI step."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(log_path), logging.StreamHandler()],
        force=True,
    )


# --- Reporting task --- #

def run_reporting_step(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Read monthly backtest returns and overwrite a deterministic metrics table."""
    backtest = pd.read_csv(input_path)
    required = {"strategy_return", "benchmark_return"}
    missing = sorted(required - set(backtest.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    metrics = pd.DataFrame({
        "momentum_strategy": strategy_metrics(backtest["strategy_return"]),
        "SPY_benchmark": strategy_metrics(backtest["benchmark_return"]),
    }).T
    output_path.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(output_path)
    logging.info("Wrote %s from %s", output_path, input_path)
    return metrics


# --- Command-line interface --- #

def parse_args() -> argparse.Namespace:
    """Parse optional input, output, and log paths."""
    parser = argparse.ArgumentParser(description="Rebuild the ETF strategy metrics table.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    return parser.parse_args()


def main() -> None:
    """Run the reporting step with CLI-provided paths."""
    args = parse_args()
    configure_logging(args.log)
    metrics = run_reporting_step(args.input, args.output)
    print(metrics.round(4))


if __name__ == "__main__":
    main()
