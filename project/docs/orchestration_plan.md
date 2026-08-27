# Orchestration Plan

## Tasks, Inputs, and Outputs

| Task | Inputs | Outputs | Depends on | Idempotent? |
|---|---|---|---|---|
| 1. Ingest | Yahoo Finance; tickers and dates in `src/config.py` | `data/raw/etf_prices_raw.csv` | None | Yes. The same dated request overwrites the same raw path. |
| 2. Clean and validate | Raw CSV; `src/cleaning.py` | `data/processed/etf_prices_cleaned.parquet` | 1 | Yes. Deterministic rules overwrite the processed file. |
| 3. Engineer features | Clean Parquet; `src/features.py` | `data/processed/etf_features.parquet` | 2 | Yes. Rolling definitions and inputs are fixed. |
| 4. Fit baseline model | Feature Parquet; `src/modeling.py` | `model/return_model.pkl`, model predictions | 3 | Yes for the same data and split. |
| 5. Backtest and evaluate | Clean prices; `src/strategy.py`, `src/evaluation.py` | Monthly backtest, weights, metrics, and charts | 2; task 4 only for model diagnostics | Yes. Files are rebuilt rather than appended. |
| 6. Report and package | Backtest, predictions, saved model | `reports/`, `app.py`, stakeholder documents | 4 and 5 | Yes. Reports are overwritten from validated inputs. |

## Dependency Design

The main chain is `ingest → clean → features → model → report`. After cleaning, the rule-based backtest can run in parallel with feature engineering and model fitting. Reporting waits for both branches. The notebook keeps this order visible; a scheduler could later represent the same graph without changing the task boundaries.

## Logging and Checkpoints

Each durable file is a checkpoint. A task logs its start, input path, row count, output path, and exception. The standalone reporting proof writes to `reports/pipeline.log`. Validation occurs immediately after raw, clean, feature, model, and report checkpoints. Files are overwritten only after the producing step succeeds.

## Failure and Retry Policy

Network failures receive one delayed retry because repeated requests can worsen rate limits. Schema, missing-column, nonpositive-price, or empty-data failures receive no automatic retry; the batch is quarantined for review. Deterministic local tasks receive one retry after confirming their input checkpoint exists. The API is restarted once; a second failure triggers rollback to the last tagged commit.

## Automation Boundary

Automate ingestion, validation, transformations, model fitting, backtesting, reporting, artifact checks, and the API health check. Keep investment approval, threshold changes, incident classification, and rollback approval manual. Those decisions depend on context and should leave a human audit trail.

## CLI Proof

From `project/`, run `python -m src.run_step`. It reads `data/processed/monthly_backtest.csv`, rebuilds `reports/orchestration_metrics.csv`, and records the step in `reports/pipeline.log`. Optional `--input`, `--output`, and `--log` arguments support an isolated test without changing the default production paths.
