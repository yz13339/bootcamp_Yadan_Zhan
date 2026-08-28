# Orchestration and system design

| Task | Input | Output | Depends on | Idempotent |
|---|---|---|---|---|
| Ingest | Yahoo Finance parameters | `data/raw/multi_asset_market_data_raw.csv` | none | Yes for a fixed date range |
| Clean | raw CSV | `data/processed/multi_asset_market_data_processed.csv` | ingest | Yes; overwrite from immutable raw |
| Feature | processed prices | `data/processed/market_features.csv` | clean | Yes; deterministic overwrite |
| Train | feature CSV | `model/market_stress_model.pkl` | feature | Yes for fixed data/seed |
| Evaluate | model and feature CSV | notebook metrics/figures | train | Yes for fixed seed |
| Report | metrics and figures | `reports/stakeholder_report.md` | evaluate | Yes; replace generated report |
| Serve | model bundle | HTTP predictions | train | No persistent output; repeatable service |

The dependency chain is `ingest → clean → feature → train → evaluate → report`; serving can start after training and reporting can run in parallel with API smoke tests. Each file boundary is a checkpoint. Log row counts, date range, schema, model version, metrics, and failures to standard output initially; a scheduler can capture these logs.

Network ingestion retries three times with exponential backoff. Validation, schema, and model failures do not retry automatically because repeated execution cannot correct bad inputs. Preserve the prior model and report until the complete downstream chain succeeds. Automate deterministic cleaning, features, training, evaluation, report generation, and API health checks now. Keep model promotion, outlier adjudication, threshold changes, and portfolio action manual because they require risk judgment.

`src/run_step.py` proves feature engineering can run outside Jupyter and creates its parent directory safely. Re-running it on the same input produces the same CSV.
