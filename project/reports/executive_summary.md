# Executive Summary

## Headline

The six-month ETF momentum rotation underperformed SPY on gross annualized return through 2026-08-26. A 10 bps-per-traded-dollar sensitivity lowers the strategy result, while the strategy still reduces maximum drawdown.

## Results

- Momentum gross annualized return: 9.24%
- Momentum net annualized return at 10 bps: 8.45%
- Momentum annualized volatility: 12.73%
- Momentum gross Sharpe ratio: 0.76
- Momentum net Sharpe ratio at 10 bps: 0.70
- Average monthly turnover: 60.8%
- Momentum maximum drawdown: -19.58%
- SPY annualized return: 14.98%
- SPY annualized volatility: 15.32%
- SPY Sharpe ratio: 0.99
- SPY maximum drawdown: -23.93%
- Regression test R-squared: 0.003
- Regression sign accuracy: 52.6%
- Outlier-filtered sign accuracy: 53.9%
- 95% bootstrap interval for mean monthly strategy return: 0.144% to 1.431%
- Latest completed-month signal (2026-07-31): DBC, VNQ

## Decision Implication

The rule is useful as a transparent diversification baseline, but these results do not justify deployment. Further work should test alternate lookbacks and cost levels, walk-forward stability, and an investable cash rule without selecting parameters on the final test period.

## Main Risks

The cost sensitivity uses a constant 10 bps rate and does not model taxes, bid-ask variation, liquidity, or market impact. The fixed ETF universe creates selection and survivorship bias. The regression has very limited predictive power. The bootstrap interval treats monthly observations as independent, and momentum can fail when market leadership reverses quickly.
