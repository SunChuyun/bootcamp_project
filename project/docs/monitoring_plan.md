# Monitoring Plan

The production candidate is the monthly ETF momentum rotation. Starting thresholds can be revised after three months of live observations.

| Layer | Failure mode | Metric and starting threshold | Alert and first response |
|---|---|---|---|
| Data | Data is stale, incomplete, or malformed | Latest date older than two business days, a ticker or column missing, null rate above 1%, or nonpositive prices | Data owner checks the source, quarantines the batch, and retries once. |
| Model | Signal behavior drifts | Three-month rolling turnover above 150% per month or no valid selection at rebalance | Quant analyst reviews feature and ranking tables before the next rebalance. |
| Model | Performance deteriorates | Six-month rolling Sharpe below 0 or drawdown below -25% | Quant analyst pauses recommendations and starts a documented review. |
| System | Pipeline or API becomes unreliable | Job success below 95% over 20 runs, or API p95 latency above 1 second | Platform on-call checks logs, retries once, then rolls back the last release. |
| Business | Strategy loses decision value | Twelve-month return trails SPY by more than 10 percentage points | Portfolio owner reviews whether to retire or redesign the rule. |

The data owner reviews ingestion alerts daily. The quant analyst reviews portfolio metrics monthly and retrains the regression baseline quarterly or after a schema, feature, or performance failure. Platform on-call owns runtime incidents, while the portfolio owner approves pauses and rollbacks. Each issue is logged in the repository with the data date, threshold, action, and resolution. Rollbacks use the last tagged release and its requirements file.
