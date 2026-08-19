# Homework 04: Data Acquisition and Ingestion

This submission implements two reproducible ingestion workflows: daily SPY market data from Yahoo Finance through `yfinance`, and the public S&P 500 constituents table from Wikipedia through `requests` and BeautifulSoup. The notebook parses dates and numeric fields, validates schema and missing values, and saves timestamped raw CSV files under `data/raw/`.

Run `homework04_data-acquisition-and-ingestion_submission.ipynb` from top to bottom using the existing `bootcamp_env` kernel. Local parameters are read from `.env`; `.env.example` documents the expected settings and `.env` is excluded from Git.
