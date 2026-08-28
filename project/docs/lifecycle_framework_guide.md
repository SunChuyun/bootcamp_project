# Lifecycle Framework Guide

| Stage | Project location | Decision made |
|---|---|---|
| 01 Problem framing | `README.md` | Evaluate a transparent ETF allocation baseline for an investment analyst. |
| 02 Tooling | `.env.example`, `requirements.txt`, `src/config.py` | Use one reproducible environment and relative project paths. |
| 03 Python fundamentals | `notebooks/python_fundamentals_summary.ipynb`, `src/utils.py` | Use small reusable checks instead of notebook-only logic. |
| 04 Acquisition | `src/data.py`, `data/raw/` | Use adjusted Yahoo Finance prices without an API key. |
| 05 Storage | `src/storage.py`, `data/raw/`, `data/processed/` | Keep raw CSV and typed processed Parquet, then reload and validate. |
| 06 Preprocessing | `src/cleaning.py` | Remove duplicates, reject invalid prices, and retain auditable rows. |
| 07 Outliers | `src/outliers.py`, `README.md` | Flag market shocks and test sensitivity instead of deleting them automatically. |
| 08 EDA | `src/eda.py`, `reports/images/` | Inspect prices, returns, volatility, drawdowns, and cross-asset relationships. |
| 09 Features | `src/features.py` | Build lagged momentum, volatility, drawdown, ticker, and next-day target fields. |
| 10a Regression | `src/modeling.py`, `notebooks/project_pipeline.ipynb` | Use a chronological split and residual/error diagnostics for a weak baseline model. |
| 10b Time series | `src/strategy.py` | Rank six-month momentum monthly and apply weights with a one-month lag. |
| 11 Evaluation | `src/evaluation.py`, `reports/risk_summary.csv` | Compare costs and outlier assumptions and quantify bootstrap uncertainty. |
| 12 Reporting | `reports/executive_summary.md`, `reports/images/` | Lead with the decision, then show evidence, assumptions, and sensitivity. |
| 13 Productization | `app.py`, `model/`, `docs/stakeholder_handoff.md` | Save with joblib and expose a validated JSON prediction route. |
| 14 Monitoring | `docs/monitoring_plan.md`, `docs/handoff_plan.md` | Monitor data, model, system, and business risks with named owners. |
| 15 Orchestration | `docs/orchestration_plan.md`, `src/run_step.py` | Define a six-task DAG and prove one task can run from the CLI. |
| 16 Lifecycle review | `README.md`, `docs/project_summary.md` | Make the full chain reproducible and readable for technical and nontechnical users. |
