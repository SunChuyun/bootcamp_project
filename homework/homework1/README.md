# ETF Momentum Rotation Strategy

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

This project studies whether a simple momentum rule can help select an ETF for the next holding period. At each month-end, the strategy ranks a selected group of ETFs by trailing six-month return and holds the strongest ETF during the next month.

The strategy will be compared with a buy-and-hold benchmark. It will be considered useful if it produces a higher Sharpe ratio and a lower maximum drawdown over the same test period.

## Stakeholder & User

- **Decision owner:** A portfolio manager who decides the monthly ETF allocation.
- **User:** A quantitative analyst who updates the ranking and prepares the report.
- **Timing:** The decision is made after each month-end for the following month.

## Useful Answer & Decision

- **Answer type:** Predictive ranking supported by historical backtesting.
- **Decision:** Select the highest-ranked ETF for the next month.
- **Metrics:** Annualized return, volatility, Sharpe ratio, maximum drawdown, and turnover.
- **Artifact:** A reproducible notebook and a short performance report.

## Assumptions & Constraints

- Adjusted price data is available and uses consistent trading dates.
- The ETF universe and lookback period are fixed before testing.
- The selected ETFs have enough liquidity for monthly trading.
- Transaction costs are included using a simple estimate.
- The strategy uses end-of-day data and does not require intraday data.

## Known Unknowns / Risks

- Momentum may reverse when market conditions change.
- Results may depend on the ETF universe and lookback period.
- Transaction costs may reduce performance.
- Historical performance may not continue in the future.

## Lifecycle Mapping

Goal → Stage → Deliverable

- Define the allocation decision → Problem Framing & Scoping (Stage 01) → Scoping paragraph.
- Identify the stakeholder and useful output → Problem Framing & Scoping (Stage 01) → Stakeholder memo.
- Organize the assignment → Problem Framing & Scoping (Stage 01) → README and folder structure.

## Repo Plan

Use `data/` for data, `src/` for reusable code, `notebooks/` for analysis, and `docs/` for project notes. Update the files as each stage is completed.
