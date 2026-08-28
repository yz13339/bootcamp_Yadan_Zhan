# Deployment handoff

- Risk analyst runs `python -m project.src.run_step` and checks data freshness/null alerts.
- Model owner executes `notebooks/project_pipeline.ipynb` and reviews chronological test metrics.
- Promote only a reviewed `model/market_stress_model.pkl`; record its commit and training end date.
- Platform on-call starts the API with `python project/app.py` and verifies `/health`.
- Prediction clients use the feature contract documented in the project README.
- Alerts and incidents go to the repository issue tracker; attach logs, dates, and model version.
- On breach, stop new scores, preserve prior output, validate source data, then roll back if needed.
- Portfolio manager approves production promotion and any risk-threshold change.
- Monitoring thresholds and ownership are defined in `docs/monitoring_plan.md`.
