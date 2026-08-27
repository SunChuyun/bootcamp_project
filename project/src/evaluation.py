"""Regression, strategy, and sensitivity evaluation utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(predictions: pd.DataFrame) -> dict[str, float]:
    """Calculate prediction error, fit, and directional accuracy."""
    actual = predictions["next_day_return"]
    predicted = predictions["predicted_return"]
    return {
        "mae": mean_absolute_error(actual, predicted),
        "rmse": mean_squared_error(actual, predicted) ** 0.5,
        "r2": r2_score(actual, predicted),
        "sign_accuracy": ((actual >= 0) == (predicted >= 0)).mean(),
    }


def strategy_metrics(returns: pd.Series, periods_per_year: int = 12) -> dict[str, float]:
    """Calculate annualized performance with a zero-risk-free-rate Sharpe ratio."""
    growth = (1 + returns).cumprod()
    years = len(returns) / periods_per_year
    annual_return = growth.iloc[-1] ** (1 / years) - 1
    annual_volatility = returns.std(ddof=1) * np.sqrt(periods_per_year)
    sharpe = (
        returns.mean() / returns.std(ddof=1) * np.sqrt(periods_per_year)
        if returns.std(ddof=1)
        else np.nan
    )
    max_drawdown = (growth / growth.cummax() - 1).min()
    return {
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe,
        "max_drawdown": max_drawdown,
        "total_return": growth.iloc[-1] - 1,
    }


def bootstrap_mean_interval(
    returns: pd.Series,
    samples: int = 2000,
    confidence: float = 0.95,
    seed: int = 7,
) -> tuple[float, float]:
    """Estimate an IID bootstrap interval for the mean period return."""
    values = returns.dropna().to_numpy()
    generator = np.random.default_rng(seed)
    boot_means = np.array([
        generator.choice(values, size=len(values), replace=True).mean()
        for _ in range(samples)
    ])
    tail = (1 - confidence) / 2
    return tuple(np.quantile(boot_means, [tail, 1 - tail]))
