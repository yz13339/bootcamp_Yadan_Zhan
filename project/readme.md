# Multi-Asset Market Stress Monitoring for Portfolio Risk Management

## Project Summary

Financial stress is not always visible from the equity market alone. During periods of uncertainty, stock prices, expected volatility, government bonds, and gold may react differently. Looking at these markets together may therefore provide a more complete picture of changing financial conditions than relying on a single asset or risk measure.

This project aims to develop an interpretable multi-asset market stress indicator using daily data for SPY, the VIX, TLT, and GLD. The analysis will examine returns, volatility, drawdowns, and cross-asset relationships to identify periods of low, moderate, and high market stress. The resulting indicator is intended to support portfolio monitoring and weekly risk-review decisions.

## Research Question

How can equity, volatility, bond, and gold market indicators be combined to identify periods of elevated financial-market stress?

## Assets

The project will initially use the following market indicators:

* **SPY:** represents the broad U.S. equity market
* **VIX:** represents expected U.S. equity-market volatility
* **TLT:** represents long-term U.S. Treasury bonds
* **GLD:** represents the gold market

## Stakeholder Context

The primary stakeholder is a portfolio manager responsible for a diversified investment portfolio. The portfolio manager needs to monitor whether overall market stress is increasing and determine whether the portfolio's asset allocation, risk limits, or hedging needs require additional review.

The primary user is a risk analyst who collects and validates market data, calculates risk indicators, monitors changes across assets, and communicates the results to the portfolio manager. The stakeholder and user care about the reliability, timeliness, and interpretability of the market stress indicator.

## Decision Supported

The analysis is designed to support weekly portfolio risk reviews. If the indicator suggests that financial markets have entered a high-stress condition, the portfolio manager may conduct an additional review of:

* Portfolio risk exposure
* Asset allocation
* Risk limits
* Diversification
* Hedging needs

The indicator will support human judgment rather than automatically recommend or execute trades.

## Intended Outputs

The project is expected to produce:

* Clean and validated daily market data
* Summary statistics and visualizations
* Return, volatility, and drawdown measures
* Analysis of relationships among equities, volatility, bonds, and gold
* Classification of low-, moderate-, and high-stress periods
* An interpretable market stress indicator

## Project Scope

The project will focus on publicly available daily U.S. market data. It will analyze SPY, VIX, TLT, and GLD over a common historical period. The analysis will focus on market-level stress rather than the risk of individual securities.

The initial scope will not include:

* Intraday or high-frequency data
* Individual-stock selection
* Automatic trade execution
* Transaction-cost optimization
* Personalized investment recommendations

## Assumptions

* SPY is a reasonable proxy for the broad U.S. equity market.
* The VIX contains useful information about expected equity-market volatility.
* TLT and GLD provide additional information about investor behavior across asset classes.
* Daily observations are sufficiently frequent for weekly risk monitoring.
* Historical relationships contain useful information for identifying current market conditions.
* The selected data sources are sufficiently accurate and consistent.

## Constraints

* The project relies on publicly available market data.
* API rate limits or data delays may restrict data collection.
* Different assets may have missing observations or different trading calendars.
* The project has limited time and computing resources.
* A simplified indicator cannot capture every source of financial risk.

## Risks and Known Unknowns

* Market relationships may change during new economic regimes.
* Bonds or gold may not behave as safe-haven assets in every stress period.
* Missing data or data-source changes may affect the results.
* Stress classifications may be sensitive to selected indicators and thresholds.
* Extreme historical events may have a disproportionate influence on the analysis.
* Future model development may introduce overfitting or look-ahead bias.
* The selected assets may not fully represent the stakeholder's actual portfolio.

## Goal-to-Deliverable Mapping

| Goal                                       | Lifecycle Stage             | Deliverable                                |
| ------------------------------------------ | --------------------------- | ------------------------------------------ |
| Define the financial-market stress problem | Problem Framing and Scoping | Project summary and research question      |
| Identify the decision-maker and user       | Problem Framing and Scoping | Stakeholder context                        |
| Define the supported decision              | Problem Framing and Scoping | Decision description                       |
| Establish project boundaries               | Problem Framing and Scoping | Scope, assumptions, constraints, and risks |
| Create a persistent workspace              | Problem Framing and Scoping | GitHub repository and project structure    |

## Project Structure

```text
project/
├── data/
│   ├── raw/          # Original, unmodified source data (not committed)
│   └── processed/    # Cleaned and analysis-ready data (not committed)
├── notebooks/        # Exploration and analysis notebooks
├── src/              # Reusable data and modeling code
├── docs/             # Project documentation
├── reports/          # Final figures, tables, and written reports
├── model/            # Saved model artifacts (not committed)
├── README.md         # Project purpose, scope, and instructions
└── requirements.txt  # Reproducible Python dependencies
```

Empty directories contain `.gitkeep` files so that the project structure is
preserved in Git. Generated data and model artifacts are excluded to avoid
committing large or reproducible files.

## Environment Setup

Python 3.11 or newer is required; this setup has been verified with Python
3.14.3. From the repository root, create and activate an isolated environment,
then install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r project/requirements.txt
```

To make the environment available in JupyterLab:

```bash
python -m ipykernel install --user --name market-stress \
  --display-name "Python (Market Stress)"
jupyter lab
```

Store API keys and other secrets in a local `.env` file. The `.env` file,
virtual environment, raw/processed data, and generated model files are ignored
by Git.


## Data Storage

Project data are organized into two folders:

- `data/raw/` stores immutable data downloaded directly from the source.
- `data/processed/` stores datasets produced through reproducible
  cleaning and transformation steps.

The raw market data are stored in CSV format because the dataset is
small and CSV is widely readable. Data are loaded using pandas, with
folder paths configured through environment variables in `.env`.

The `.env` file is excluded from version control, while `.env.example`
documents the required path variables.
