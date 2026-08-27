# Monitoring Plan

The production candidate is the monthly six-month ETF momentum rotation. Monitoring covers four layers and starts with thresholds that can be revised after three months of live observations.

| Layer | Failure mode | Metric and starting threshold | Alert and first response |
|---|---|---|---|
| Data | Yahoo data is stale or incomplete | Latest trading date older than two business days, any required ticker missing, or close-price null rate above 1% | Data owner checks the download and reruns ingestion once. |
| Data | Schema or scale changes | Expected columns differ, nonpositive prices appear, or any one-day return exceeds 40% | Data owner quarantines the batch and compares it with the source. |
| Model | Signal behavior drifts | Three-month rolling turnover above 150% per month or no valid selection at rebalance | Quant analyst reviews feature and ranking tables before the next rebalance. |
| Model | Performance deteriorates | Six-month rolling Sharpe below 0 or drawdown below -25% | Quant analyst pauses recommendations and starts a documented review. |
| System | Pipeline or API becomes unreliable | Job success below 95% over 20 runs, or API p95 latency above 1 second | Platform on-call checks logs, retries once, then rolls back the last release. |
| Business | Strategy loses decision value | Twelve-month return trails SPY by more than 10 percentage points | Portfolio owner reviews whether to retire or redesign the rule. |

The data owner reviews daily ingestion alerts. The quant analyst reviews model and portfolio metrics monthly and retrains the regression baseline quarterly or when schema, feature, or performance thresholds fail. The platform on-call owns runtime incidents; the portfolio owner approves pauses and rollbacks. Issues are logged in the repository issue tracker with the data date, failing threshold, action, and resolution. A rollback uses the last tagged release and its saved requirements file.
