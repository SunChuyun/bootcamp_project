# Cross-Asset ETF Momentum Rotation

## Overview

This project tests a monthly ETF rotation strategy. It ranks eight ETFs by six-month momentum and holds the top two at equal weights in the following month. SPY is the benchmark.

The data comes from Yahoo Finance through `yfinance` and covers January 2016 through August 2026. The analysis uses lagged signals to avoid look-ahead bias. Results are educational and exclude taxes, market impact, and changing bid-ask spreads.

## Main Results

Through August 26, 2026, the strategy produced a 9.24% gross annualized return, 12.73% annualized volatility, a 0.76 Sharpe ratio, and a -19.58% maximum drawdown. At a constant 10 bps per traded dollar, annualized return falls to 8.45% and Sharpe falls to 0.70.

Over the aligned sample, SPY returned 14.98% annually with a 0.99 Sharpe ratio and a -23.93% maximum drawdown. The strategy reduced drawdown but underperformed SPY on return and risk-adjusted return. The regression baseline also has limited predictive value, with test $R^2$ of 0.003 and 52.6% sign accuracy.

## Project Structure

- `data/`: raw and processed data.
- `notebooks/`: the complete project pipeline.
- `src/`: reusable data, modeling, strategy, and evaluation functions.
- `model/`: saved regression model.
- `reports/`: tables, charts, and the executive summary.
- `docs/`: assumptions, monitoring, handoff, and lifecycle documents.
- `app.py`: Flask prediction API.

## Install and Run

From a fresh clone:

```powershell
conda create -n bootcamp_env python=3.11 -y
conda activate bootcamp_env
pip install -r project/requirements.txt
copy project/.env.example project/.env
jupyter lab
```

Open `project/notebooks/project_pipeline.ipynb` and run all cells from top to bottom. The pipeline downloads data, rebuilds the analysis, saves the model, and updates the reports. No API key is required.

## Prediction API

After running the pipeline, start the API from `project/`:

```powershell
python app.py
```

Example requests:

```python
import joblib
import requests

bundle = joblib.load("model/return_model.pkl")
features = {name: 0.0 for name in bundle["features"]}

print(requests.get("http://127.0.0.1:5001/health").json())
print(requests.post(
    "http://127.0.0.1:5001/predict",
    json={"features": features},
).json())
```

Invalid, missing, or extra feature values return HTTP 400 with a JSON error.

## Command-Line Step

After running the pipeline, rebuild the orchestration report from `project/`:

```powershell
python -m src.run_step
```

This command reads the saved monthly backtest, writes `reports/orchestration_metrics.csv`, and records the run in `reports/pipeline.log`.

## Lifecycle Map

| Stage | Main artifact |
|---|---|
| 01–03: Scope and setup | `docs/stakeholder_memo.md`, `.env.example`, `requirements.txt` |
| 04–05: Acquisition and storage | `src/data.py`, `src/storage.py`, `data/` |
| 06–09: Cleaning, EDA, and features | `src/cleaning.py`, `src/eda.py`, `src/features.py` |
| 10–11: Modeling and evaluation | `src/modeling.py`, `src/strategy.py`, `src/evaluation.py` |
| 12–13: Reporting and API | `reports/`, `app.py` |
| 14–15: Monitoring and orchestration | `docs/monitoring_plan.md`, `src/run_step.py` |
| 16: Lifecycle review | `docs/lifecycle_framework_guide.md`, `docs/project_summary.md` |

## Limits and Next Steps

The fixed universe creates selection and survivorship bias, and the cost model is simplified. Before any deployment, the strategy should be tested with walk-forward parameter selection, different cost assumptions, and paper trading. Detailed assumptions and decisions are documented in `docs/`.
