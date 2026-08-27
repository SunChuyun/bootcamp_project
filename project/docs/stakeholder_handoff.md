# Stakeholder Handoff Summary

## Overview

This project evaluates a transparent monthly rule that ranks eight cross-asset ETFs by six-month momentum and holds the strongest two during the next month.

## Findings and Recommendation

The strategy reduced maximum drawdown relative to SPY but produced lower return and lower risk-adjusted performance in the tested sample. Treat it as a research baseline, not a deployment recommendation.

## Assumptions and Risks

The backtest uses a fixed ETF universe, adjusted Yahoo Finance data, monthly execution, and a constant cost sensitivity. It excludes taxes, varying spreads, market impact, and live operational constraints. The regression baseline has little predictive value, and the IID bootstrap does not preserve time dependence.

## Using the Deliverables

Run the cumulative notebook to rebuild data, model, figures, metrics, and the executive summary. After the model exists, start `app.py` and call `/health` or `/predict` as shown in `README.md`. Review `docs/monitoring_plan.md` before treating any output as operational.

## Next Steps

Test alternate lookbacks without selecting on the final period, use walk-forward evaluation, add a cash rule, estimate realistic trading costs, and paper-trade before considering deployment.
