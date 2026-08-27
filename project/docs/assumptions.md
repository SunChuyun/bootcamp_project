# Assumptions and Risks

## Data

- Yahoo Finance adjusted prices are treated as the available historical record.
- The eight-ETF universe is fixed for the full sample.
- Missing volume is set to zero, while rows without a valid positive close are excluded.
- Raw downloaded observations are preserved without outlier deletion.

## Strategy

- Signals are computed at month-end and applied to the next month's return.
- The top two ETFs receive equal weights.
- The main backtest is gross of costs; a 10 bps-per-traded-dollar sensitivity is reported.
- Taxes, bid-ask variation, market impact, and liquidity limits remain excluded.
- Six-month momentum and monthly rebalancing are research assumptions, not optimized choices.

## Modeling

- The regression is a diagnostic baseline and does not drive portfolio holdings.
- Training observations occur strictly before test observations.
- Outlier thresholds used for model sensitivity are estimated from training rows only.
- Linear relationships and stable feature behavior are simplifying assumptions.
- Daily rows within an ETF and across ETFs are not fully independent.

## Risk Communication

- Historical performance does not establish future profitability.
- A fixed ETF universe introduces survivorship and selection bias.
- Market regimes can change the direction and strength of momentum.
- Removing genuine shock observations can understate tail risk.
