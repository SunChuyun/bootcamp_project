# Cross-Asset ETF Momentum Rotation

## Project Summary

This project tests a monthly ETF momentum rotation strategy. It ranks a diversified ETF universe by six-month price momentum and holds the two strongest ETFs at equal weights for the following month.

The intended stakeholder is an investment analyst evaluating whether a simple, transparent allocation rule is useful as a research baseline. The main concerns are return, volatility, drawdown, stability across assumptions, and implementation risk.

## Strategy Scope

- Universe: SPY, EFA, EEM, TLT, IEF, GLD, VNQ, and DBC.
- Data: adjusted daily prices and volume from Yahoo Finance through `yfinance`.
- Sample: January 2016 through August 2026.
- Rebalancing: monthly.
- Signal: six-month total return.
- Portfolio: equal-weight the top two ETFs, with a one-month lag between signal and realized return.
- Benchmark: SPY.

This is an educational backtest. The main result is gross of costs, with a 10 bps-per-traded-dollar sensitivity. Taxes, bid-ask variation, market impact, and live trading constraints remain excluded.

## Project Structure

- `data/raw/`: unedited Yahoo Finance observations.
- `data/processed/`: cleaned prices, engineered features, and backtest tables.
- `notebooks/`: the cumulative project pipeline and the Stage 03 Python summary.
- `src/`: reusable acquisition, cleaning, analysis, feature, strategy, and evaluation functions.
- `docs/`: stakeholder context and modeling assumptions.
- `reports/images/`: charts created by the pipeline.
- `reports/`: metrics, sensitivity tables, and the executive summary.
- `model/`: the saved linear-regression baseline.

## Data Storage

Relative paths are defined in `.env`. Raw observations are stored as CSV for portability. Cleaned and feature tables are stored as Parquet to preserve dates and numeric types. The pipeline reloads each saved table and validates its structure.

## Cleaning and Outlier Policy

Duplicate ticker-date rows are removed, dates and numeric columns are parsed, nonpositive prices are rejected, and missing volume is set to zero. Daily-return outliers are flagged within each ETF using the 1.5-IQR rule. Raw observations are retained; outliers are not automatically deleted because they may represent genuine market shocks.

## Feature Definitions

- `return_1d`: one-day ETF return.
- `momentum_21d`, `momentum_63d`, `momentum_126d`: trailing price returns.
- `volatility_21d`: annualized rolling standard deviation of daily returns.
- `drawdown_63d`: price relative to its rolling 63-day high.
- ticker indicators: one-hot encoding for the pooled regression baseline.
- `next_day_return`: next trading day's return, used only as the model target.

## Modeling and Evaluation

The strategy is rule-based. A separate linear-regression baseline uses a time-aware train/test split to test whether the engineered features contain short-horizon predictive information. Outlier thresholds for its sensitivity check are estimated from training rows only. Results include MAE, RMSE, $R^2$, sign accuracy, annualized return, annualized volatility, zero-risk-free-rate Sharpe ratio, maximum drawdown, turnover, a 10 bps cost sensitivity, and a bootstrap interval.

## Current Results

Using data through August 26, 2026, the momentum strategy produced a 9.24% gross annualized return, 12.73% annualized volatility, a 0.76 gross Sharpe ratio, and a -19.58% maximum drawdown. With the 10 bps cost sensitivity, annualized return falls to 8.45% and Sharpe falls to 0.70. SPY produced a 14.98% annualized return, a 0.99 Sharpe ratio, and a -23.93% maximum drawdown over the aligned monthly sample. The strategy therefore reduced drawdown but underperformed SPY on return and risk-adjusted return.

The regression baseline has limited predictive value: test $R^2$ is 0.003 and sign accuracy is 52.6%. Excluding training observations flagged by training-only IQR thresholds raises sign accuracy to 53.9% but does not materially improve $R^2$. The latest completed-month signal selects DBC and VNQ.

## Run

Activate the repository's `bootcamp_env`, install the root `requirements.txt`, and run `notebooks/project_pipeline.ipynb` from top to bottom. No API key is required.
