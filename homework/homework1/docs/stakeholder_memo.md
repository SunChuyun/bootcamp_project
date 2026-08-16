# Stakeholder Memo: ETF Momentum Rotation Strategy

**To:** Portfolio Manager  
**From:** Student Quantitative Analyst  
**Subject:** Monthly ETF selection using momentum

## Context

The portfolio manager needs a simple and repeatable way to select an ETF each month.

## Proposed Rule

At each month-end, rank the selected ETFs by trailing six-month return. Hold the highest-ranked ETF during the next month.

## Deliverable

The final report will show the selected ETF, cumulative return, annualized return, volatility, Sharpe ratio, maximum drawdown, and turnover.

## Success Criteria

The strategy should have a higher Sharpe ratio and a lower maximum drawdown than the benchmark after transaction costs.

## Main Risks

- Momentum can reverse quickly.
- Results may change with the ETF universe or lookback period.
- Historical performance may not continue in the future.
