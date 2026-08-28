# Multi-Asset Market Stress Monitoring — Project Summary

## The problem

A portfolio manager needs an interpretable early-warning view of market stress. Equity prices alone may miss signals visible in expected volatility, Treasury bonds, or gold. This project combines daily SPY, VIX, TLT, and GLD data to estimate whether the next trading day is likely to meet a simple high-stress definition. It supports an additional risk review; it does not recommend or execute trades.

## What was built

The pipeline acquires and cleans adjusted market prices, then calculates returns, trailing equity volatility, drawdown, lagged VIX movement, a rolling VIX z-score, and lagged bond/gold returns. Every predictive feature is shifted so that it would be known before the predicted day. High stress is defined as next-day VIX at least 25 or SPY return at most −2.5%. A scaled logistic-regression pipeline is trained on the earliest 80% of observations and evaluated on the latest 20%.

Exploration explicitly flags extreme returns. They are retained because crisis observations are usually meaningful; a winsorized sensitivity check shows how conclusions change if their influence is capped. Evaluation reports accuracy, precision, recall, F1, a confusion matrix, a paired bootstrap interval, a class-balanced scenario, and volatility subgroups. A stakeholder report translates these results into a cautious decision message. The saved model is exposed through a Flask JSON API.

## What was found

Stress is rare and clustered, making raw accuracy potentially misleading. Cross-asset and volatility features provide an interpretable baseline, but performance varies with class weighting and volatility regime. Recall is especially important: missing a high-stress day is more damaging to this use case than generating an extra human review. Bootstrap uncertainty is material because the chronological holdout contains relatively few stress events.

## What not to rely on

Do not treat the probability as a calibrated loss forecast, causal result, or automatic allocation signal. The label thresholds are policy choices, relationships can change across regimes, Yahoo data can be delayed or revised, and a standard paired bootstrap understates time dependence. The selected liquid proxies do not represent every exposure in the stakeholder’s portfolio. Transaction costs and portfolio-level drawdowns are outside scope.

## Recommended use and next steps

Use the output as one input to a weekly analyst review. Display the score with current VIX, drawdown, data freshness, and recent false-negative history. Before production, extend walk-forward testing across more history, use time-block bootstrap, calibrate probabilities, quantify portfolio-specific costs, and obtain threshold approval from the portfolio manager. Monitor schema, freshness, feature drift, rolling recall, API latency, and alert volume. Retrain quarterly or after persistent drift/performance breaches, but keep promotion and rollback under human approval.
