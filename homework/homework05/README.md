# Homework 05: Data Storage

This submission implements a reproducible storage layer for the SPY market data acquired in Homework 04. Run `homework05_data-storage_submission.ipynb` from top to bottom with the `bootcamp_env` kernel.

## Data Storage

- `data/raw/` contains CSV snapshots. CSV is portable, human-readable, and convenient for inspecting raw data.
- `data/processed/` contains Parquet snapshots. Parquet is compact, typed, and efficient for analytical reads.
- `.env` defines `DATA_DIR_RAW=data/raw` and `DATA_DIR_PROCESSED=data/processed`. The notebook resolves these paths relative to the Homework 05 directory, creates missing directories, and never relies on the caller's working directory.
- `write_df` and `read_df` select pandas CSV or Parquet IO from the `.csv` or `.parquet` suffix. Unsupported suffixes raise a clear error; Parquet operations also explain how to install an engine if one is unavailable.

The notebook saves the same DataFrame in both formats, reloads both snapshots, and validates that their shapes, critical columns, and expected dtype families agree.
