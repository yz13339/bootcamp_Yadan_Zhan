import pandas as pd


def clean_market_data(df):
    """
    Clean the raw multi-asset market dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw market data downloaded from Yahoo Finance.

    Returns
    -------
    pandas.DataFrame
        Cleaned adjusted-close prices.
    """

    cleaned = df.copy()

    # Select adjusted closing prices from the two-level columns.
    if isinstance(cleaned.columns, pd.MultiIndex):
        cleaned = cleaned["Adj Close"].copy()

    # Rename the VIX ticker for clearer column naming.
    cleaned = cleaned.rename(columns={"^VIX": "VIX"})

    # Convert the index to dates and remove invalid dates.
    cleaned.index = pd.to_datetime(cleaned.index, errors="coerce")
    cleaned = cleaned[~cleaned.index.isna()]

    # Remove duplicate dates and sort chronologically.
    cleaned = cleaned[
        ~cleaned.index.duplicated(keep="first")
    ]
    cleaned = cleaned.sort_index()

    # Ensure all price columns are numeric.
    cleaned = cleaned.apply(
        pd.to_numeric,
        errors="coerce"
    )

    # Treat non-positive market prices as invalid.
    cleaned = cleaned.mask(cleaned <= 0)

    # Fill internal missing values using the previous valid observation.
    cleaned = cleaned.ffill()

    # Remove any missing values left at the beginning.
    cleaned = cleaned.dropna()

    cleaned.index.name = "Date"

    return cleaned