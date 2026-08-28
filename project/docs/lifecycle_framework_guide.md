# Project lifecycle framework guide

| Stage | Project artifact | Decision |
|---|---|---|
| 1 Problem framing | `README.md` | Support weekly human risk review, not trading automation. |
| 2 Setup | `.env.example`, `requirements.txt` | Reproducible paths and isolated Python environment. |
| 3 Python fundamentals | `notebooks/python_fundamentals_summary.ipynb` | Use pandas/NumPy for market transformations. |
| 4 Acquisition | `notebooks/project_pipeline.ipynb`, `data/raw/` | Yahoo Finance daily SPY/VIX/TLT/GLD. |
| 5 Storage | `data/raw/`, `data/processed/` | Separate immutable source and derived data. |
| 6 Preprocessing | `src/cleaning.py` | Adjusted closes, dates, duplicates and missing values validated. |
| 7 Outliers | `src/outliers.py`, `docs/outliers.md` | Flag real extremes and test winsorized sensitivity. |
| 8 EDA | `src/eda.py`, pipeline notebook | Examine returns, volatility, drawdown and dependence. |
| 9 Features | `src/features.py` | Past-only cross-asset stress features. |
| 10 Modeling | `src/modeling.py`, pipeline notebook | Time-split logistic baseline for next-day high stress. |
| 11 Evaluation | `src/evaluation.py` | Bootstrap uncertainty and class-weight scenario. |
| 12 Delivery | `reports/stakeholder_report.md` | Decision memo with risk-aware interpretation. |
| 13 Productization | `app.py`, `model/` | Saved bundle and validated JSON endpoint. |
| 14 Monitoring | `docs/monitoring_plan.md` | Data/model/system/business thresholds and owners. |
| 15 Orchestration | `docs/orchestration_plan.md`, `src/run_step.py` | Idempotent file checkpoints and manual promotion. |
| 16 Review | this guide, `docs/project_summary.md` | Make the complete chain auditable and transferable. |
