# Cross-Asset ETF Momentum Rotation: Project Summary

## The Question

An investment analyst often needs a simple baseline before evaluating more complicated allocation models. This project asks whether a transparent momentum rule can improve the balance between return and risk across several liquid asset classes. The rule ranks a fixed universe of exchange-traded funds by their previous six-month price change, selects the strongest two, and holds them at equal weights during the following month.

The universe contains U.S., international developed, and emerging-market equities; long- and intermediate-term U.S. Treasury bonds; gold; real estate; and broad commodities. SPY is the comparison benchmark. The project is educational and does not provide investment advice.

## What Was Done

Daily adjusted prices and volume were downloaded from Yahoo Finance for January 2016 through August 2026. The acquisition step requires no API key. Raw observations were saved as CSV, while cleaned and engineered tables were saved as Parquet so dates and numeric types remain stable. Every saved table was reloaded and checked before the next stage used it.

Cleaning removed duplicate ticker-date rows, parsed dates and numeric fields, rejected nonpositive prices, and filled missing volume with zero. Large daily returns were flagged within each ETF with an interquartile-range rule. They were not automatically deleted because an extreme return may be a real market event rather than a data error.

The main strategy uses six-month total return as its signal. Rankings are formed at month-end, and the portfolio uses those rankings only in the next month. This one-month lag is essential: without it, the test would use information that was not yet available. The two selected ETFs receive equal weight. Turnover is calculated from changes in portfolio weights, and a sensitivity subtracts 10 basis points for each dollar traded.

A separate linear-regression baseline tests whether lagged returns, momentum, volatility, drawdown, and ticker indicators explain the next daily return. Training and test periods are separated chronologically. This model is not the allocation rule; it is a diagnostic baseline that shows whether simple engineered features contain short-horizon predictive information.

## Main Findings

Through August 26, 2026, the momentum strategy earned about 9.24% per year before costs with 12.73% annualized volatility, a 0.76 Sharpe ratio using a zero risk-free rate, and a maximum drawdown of about 19.58%. Under the constant 10 basis point trading-cost sensitivity, annualized return fell to about 8.45% and the Sharpe ratio fell to 0.70.

Over the aligned monthly sample, SPY earned about 14.98% per year with a 0.99 Sharpe ratio and a maximum drawdown of about 23.93%. The momentum rule therefore reduced the worst historical decline but did not compensate for that reduction with competitive return or risk-adjusted performance. The practical conclusion is cautious: diversification helped drawdown, but this specific rule did not beat the simple benchmark.

The regression baseline also provides a warning. Its test $R^2$ is approximately 0.003 and directional accuracy is approximately 52.6%. Removing training observations flagged as outliers slightly raises directional accuracy but does not materially improve explanatory power. The model should not be treated as a reliable daily return forecaster.

## What Not to Rely On

The results come from one historical period and one fixed ETF universe. ETFs that exist today were selected in advance, so the test contains selection and survivorship bias. Adjusted prices simplify corporate actions but do not reproduce executable prices. The trading-cost scenario is constant and excludes taxes, changing bid-ask spreads, liquidity, and market impact.

Six-month momentum and a top-two portfolio were chosen as a transparent baseline, not through a full preregistered search. Testing many alternatives and reporting only the best would create data-mining bias. The bootstrap interval resamples monthly returns as if they were independent, which does not preserve volatility clusters or market regimes. The latest signal is an output of the rule, not a recommendation.

Operational risks also matter. Yahoo data can be late or incomplete, columns can change, the API can fail, and portfolio leadership can reverse quickly. The monitoring plan therefore defines freshness, null-rate, schema, turnover, performance, latency, job-success, and business-value thresholds. Named owners review alerts and approve pauses or rollbacks.

## How the Work Can Be Used

The cumulative notebook rebuilds the complete analysis: acquisition, storage, cleaning, exploratory analysis, feature engineering, modeling, backtesting, evaluation, and reporting. Reusable functions live in `src/`. The saved regression model is loaded once when the Flask service starts. A caller can check service health and request a next-day return prediction by posting a complete feature mapping. Invalid input receives a clear HTTP 400 response.

The API makes the model callable, but productization does not make the model trustworthy. The weak predictive results remain visible in the README, executive summary, handoff document, and monitoring plan. A separate command-line reporting step demonstrates how one notebook task can run independently and be scheduled later.

## Recommended Next Steps

The first research extension is walk-forward testing of several economically motivated lookbacks and portfolio sizes with parameter choices fixed before each test window. A cash or defensive rule could be evaluated when all momentum signals are negative. Cost assumptions should vary by ETF and market condition, and results should include taxes where relevant.

Before deployment, the strategy should be paper-traded. Live observations can verify data timing, signal formation, turnover, execution assumptions, and monitoring thresholds. Only after stable out-of-sample evidence should an analyst consider whether the rule adds value to a broader investment process. Until then, the project is best used as a reproducible baseline and a demonstration of the full data-project lifecycle.
