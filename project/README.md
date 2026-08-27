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
- `app.py`: Flask prediction API that loads the saved model once.
- `requirements.txt`: minimal direct dependencies for this project.

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

## Install and Run

From a fresh clone:

```powershell
conda create -n bootcamp_env python=3.11 -y
conda activate bootcamp_env
pip install -r project/requirements.txt
copy project/.env.example project/.env
jupyter lab
```

Open `project/notebooks/project_pipeline.ipynb` and run it from top to bottom. It refreshes the committed small data files, saved model, and reports. No API key is required.

## Prediction API

Run the pipeline first so `model/return_model.pkl` exists. From `project/`, start the service:

```powershell
python app.py
```

Check it with `requests`:

```python
import joblib
import requests

bundle = joblib.load("model/return_model.pkl")
payload = {"features": {name: 0.0 for name in bundle["features"]}}
print(requests.get("http://127.0.0.1:5001/health").json())
print(requests.post("http://127.0.0.1:5001/predict", json=payload).json())
```

Missing, extra, nonnumeric, or nonfinite feature values return a JSON error with HTTP 400.

## Command-Line Reporting Step

Run the pipeline first so `data/processed/monthly_backtest.csv` exists. From `project/`:

```powershell
python -m src.run_step
```

The command rebuilds `reports/orchestration_metrics.csv` and writes `reports/pipeline.log`. It accepts optional `--input`, `--output`, and `--log` paths. The step is idempotent: the same validated input overwrites the same output.

## Lifecycle Map

| Stage | Main location |
|---|---|
| 01 Problem framing | `docs/stakeholder_memo.md` |
| 02 Tooling | `.env.example`, `requirements.txt`, `src/config.py` |
| 03 Python fundamentals | `notebooks/python_fundamentals_summary.ipynb`, `src/utils.py` |
| 04 Acquisition | `src/data.py`, `data/raw/` |
| 05 Storage | `src/storage.py`, `data/processed/` |
| 06 Preprocessing | `src/cleaning.py` |
| 07 Outliers | `src/outliers.py`, `docs/assumptions.md` |
| 08 EDA | `src/eda.py`, `reports/images/` |
| 09 Features | `src/features.py` |
| 10a Regression | `src/modeling.py`, cumulative notebook |
| 10b Time series | `src/strategy.py`, cumulative notebook |
| 11 Evaluation | `src/evaluation.py`, `reports/risk_summary.csv` |
| 12 Reporting | `reports/executive_summary.md`, `reports/images/` |
| 13 Productization | `app.py`, `docs/stakeholder_handoff.md` |
| 14 Monitoring | `docs/monitoring_plan.md`, `docs/handoff_plan.md` |
| 15 Orchestration | `docs/orchestration_plan.md`, `src/run_step.py` |
| 16 Lifecycle review | `docs/lifecycle_framework_guide.md`, `docs/project_summary.md` |

The detailed lifecycle decisions are in `docs/lifecycle_framework_guide.md`.
