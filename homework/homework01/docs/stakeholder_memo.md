# Stakeholder Memo: Multi-Asset Market Stress Monitoring

**To:** Portfolio Risk Manager  
**Purpose:** Support weekly portfolio risk reviews

## Decision Context

The portfolio risk manager needs a concise and reproducible way to
determine whether current market conditions indicate elevated stress
across multiple asset classes. Monitoring equities alone may overlook
risk signals appearing in market volatility, government bonds, or gold.

## Proposed Analysis

The project will analyze daily market data for SPY, VIX, TLT, and GLD.
These assets represent U.S. equities, expected equity-market volatility,
long-term U.S. government bonds, and gold.

The analysis will summarize asset returns, rolling volatility, and changes
in cross-asset relationships. It will also highlight periods in which
multiple markets show unusual risk conditions.

## Decision Supported

The results will help the portfolio risk manager decide whether current
market conditions require closer monitoring, additional investigation,
or consideration of reduced portfolio risk exposure.

## Expected Deliverable

The final deliverable will include a reproducible analysis pipeline,
summary risk metrics, and visualizations designed for weekly portfolio
risk reviews.

## Assumptions and Limitations

- Public daily market data are sufficiently reliable for the analysis.
- The selected assets provide a simplified representation of major
  financial-market risk channels.
- Historical cross-asset relationships may not remain stable.
- The framework is descriptive and does not guarantee prediction of
  future market movements.
- Results may be affected by missing observations, different trading
  calendars, and preprocessing assumptions.