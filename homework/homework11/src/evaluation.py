"""Bootstrap and subgroup metrics for the Stage 11 homework."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


def bootstrap_rmse(
    actual: np.ndarray,
    predicted: np.ndarray,
    samples: int = 1000,
    seed: int = 42,
) -> tuple[float, float]:
    """Return a percentile interval for RMSE under row resampling."""
    generator = np.random.default_rng(seed)
    values = []
    for _ in range(samples):
        indices = generator.integers(0, len(actual), len(actual))
        values.append(mean_squared_error(actual[indices], predicted[indices]) ** 0.5)
    return tuple(np.quantile(values, [0.025, 0.975]))


def subgroup_rmse(
    frame: pd.DataFrame,
    group_column: str,
    actual_column: str,
    prediction_column: str,
) -> pd.Series:
    """Calculate RMSE separately for each categorical subgroup."""
    return frame.groupby(group_column).apply(
        lambda group: mean_squared_error(
            group[actual_column],
            group[prediction_column],
        ) ** 0.5,
        include_groups=False,
    )
