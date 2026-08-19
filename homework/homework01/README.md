# Multi-Asset Market Stress Monitoring for Portfolio Risk Management

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Portfolio risk managers need to identify periods of elevated market stress when reviewing portfolio exposures and diversification. Monitoring only the equity market may provide an incomplete picture because stress can also appear through rising expected volatility, changing government-bond prices, or movements in gold.

This project proposes a reproducible multi-asset market-stress monitoring framework using daily data for SPY, VIX, TLT, and GLD. The analysis will examine asset returns, rolling volatility, and cross-asset relationships to identify periods in which several markets show unusual risk conditions.

## Stakeholder & User

The primary stakeholder and end user is a portfolio risk manager responsible for weekly portfolio risk reviews.

The stakeholder needs a concise summary of current and historical market conditions to determine whether the portfolio requires closer monitoring, further investigation, or consideration of reduced risk exposure. The output should be reproducible and understandable without requiring the stakeholder to inspect the underlying code.

## Useful Answer & Decision

The project is primarily descriptive rather than predictive or causal. A useful answer will indicate when market stress appears elevated and identify which assets are contributing to the signal.

Relevant metrics may include daily log returns, rolling volatility, correlations between assets, and indicators of unusually stressed market conditions. The expected final artifact is a set of summary risk metrics and visualizations that can support weekly portfolio risk reviews.

The analysis is intended to support risk-monitoring decisions rather than provide investment advice or guarantee predictions of future market movements.

## Assumptions & Constraints

* Reliable daily market data are available for SPY, VIX, TLT, and GLD.
* SPY, VIX, TLT, and GLD provide simplified representations of U.S. equities, expected equity-market volatility, long-term U.S. government bonds, and gold.
* Adjusted closing prices are appropriate for calculating asset returns.
* The analysis is designed for weekly portfolio monitoring rather than high-frequency trading.
* Public market data may contain missing observations, revisions, or differences in trading calendars.
* The project is limited by the selected assets and does not represent every source of portfolio risk.
* The analysis will be completed using Python and reproducible data-processing code.

## Known Unknowns / Risks

* Historical relationships between assets may change during future market regimes.
* Extreme market events may behave differently from ordinary market conditions.
* Missing observations or differences in trading calendars may affect cross-asset comparisons.
* Thresholds used to define elevated market stress will need to be tested and documented.
* A descriptive stress signal may identify elevated risk without predicting the timing or direction of future market movements.
* Data preprocessing and outlier-handling decisions may affect the resulting risk measures.

## Lifecycle Mapping

Goal → Stage → Deliverable

* Define the market-risk problem and stakeholder decision → Problem Framing & Scoping (Stage 01) → Scoping paragraph and stakeholder memo
* Establish a reproducible working environment → Tooling Setup (Stage 02) → Repository structure and environment configuration
* Develop reusable Python components → Python Fundamentals (Stage 03) → Modular utility functions
* Obtain multi-asset market data → Data Acquisition & Ingestion (Stage 04) → Raw SPY, VIX, TLT, and GLD dataset
* Store and reload data reproducibly → Data Storage (Stage 05) → Documented raw and processed data structure
* Prepare the dataset for analysis → Data Preprocessing (Stage 06) → Cleaned adjusted-price dataset
* Examine unusual market observations and related assumptions → Outliers & Risk Assumptions (Stage 07) → Documented outlier analysis
* Measure and communicate market stress → Later lifecycle stages → Risk metrics, visualizations, and final conclusions

## Repo Plan

The cumulative project will use the following structure:

* `data/raw/` for data saved directly from the original source
* `data/processed/` for cleaned and transformed datasets
* `src/` for reusable Python functions
* `notebooks/` for the reproducible project pipeline
* `docs/` for stakeholder context, assumptions, and supporting documentation
* `reports/` for final summaries and visualizations

The repository will be updated, committed, and pushed to GitHub as each lifecycle stage is completed.
