# Stakeholder Memo

## Decision Context

An investment analyst wants a transparent baseline for rotating across major ETF asset classes. The analysis should show whether recent relative strength can guide monthly allocation without relying on a complex black-box model.

## Decision to Support

The project compares a six-month momentum rotation strategy with SPY and reports whether the strategy improves return, volatility, or drawdown. The result is intended to support further research, not an immediate live-trading decision.

## Success Criteria

- The data pipeline is reproducible from a documented public source.
- Signals use only information available before the holding period.
- Performance is compared with a clear benchmark.
- Turnover and a simple transaction-cost sensitivity are reported.
- Risks and sensitivity to outlier assumptions are reported.

## Constraints

The backtest includes only a simple 10 bps cost sensitivity. It does not model taxes, bid-ask variation, market impact, survivorship changes, or intraday execution. The ETF universe is fixed in advance and is not a claim that these are the optimal instruments.
