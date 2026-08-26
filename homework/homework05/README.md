# Homework 05: Data Storage

## Data Storage

- `data/raw/` stores the source CSV.
- `data/processed/` stores the typed Parquet version and validation outputs.
- `.env` defines `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`; `.env.example` documents the same relative paths without secrets.
- CSV is portable and readable. Parquet preserves data types and is efficient for analytical workflows.

The notebook saves both formats, reloads them, checks shape and critical data types, and demonstrates suffix-based `write_df()` and `read_df()` utilities.
