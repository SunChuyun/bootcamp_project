"""Monthly ETF momentum rotation backtest."""

from __future__ import annotations

import pandas as pd

from src.utils import require_columns


def run_momentum_rotation(
    prices: pd.DataFrame,
    benchmark: str = "SPY",
    lookback_months: int = 6,
    top_n: int = 2,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run a lagged monthly top-momentum rotation and return results and weights."""
    require_columns(prices, ["date", "ticker", "close"])
    if lookback_months <= 0 or top_n <= 0:
        raise ValueError("lookback_months and top_n must be positive")

    monthly_prices = (
        prices.pivot(index="date", columns="ticker", values="close")
        .sort_index()
        .resample("ME")
        .last()
    )
    last_observation = prices["date"].max().normalize()
    if last_observation < last_observation + pd.offsets.MonthEnd(0):
        monthly_prices = monthly_prices.iloc[:-1]
    monthly_returns = monthly_prices.pct_change(fill_method=None)
    momentum = monthly_prices.pct_change(lookback_months, fill_method=None)
    ranks = momentum.rank(axis=1, ascending=False, method="first")
    weights = (ranks <= top_n).astype(float) / top_n
    weights = weights.where(momentum.notna().all(axis=1))

    applied_weights = weights.shift(1)
    strategy_return = (applied_weights * monthly_returns).sum(axis=1, min_count=1)
    turnover = applied_weights.fillna(0).diff().abs().sum(axis=1)
    results = pd.DataFrame({
        "strategy_return": strategy_return,
        "benchmark_return": monthly_returns[benchmark],
        "turnover": turnover,
    }).dropna()
    results["strategy_growth"] = (1 + results["strategy_return"]).cumprod()
    results["benchmark_growth"] = (1 + results["benchmark_return"]).cumprod()
    return results, weights.loc[results.index]
