# Homework 09: Feature Engineering

The notebook uses the ETF-style schema introduced in Homework 08 and creates:

- five-day price momentum;
- ten-day rolling return volatility;
- one-hot ticker indicators.

Each feature is tied to an EDA observation and checked against next-day return. The reusable transformations live in `src/features.py`, and the processed feature table is saved under `data/processed/`.
