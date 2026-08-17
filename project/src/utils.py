
def parse_date_column(df, column_name="Date"):
    """
    Convert a DataFrame column to datetime format.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    column_name : str
        Name of the date column.

    Returns
    -------
    pandas.DataFrame
        DataFrame with a converted datetime column.
    """
    df = df.copy()
    df[column_name] = pd.to_datetime(df[column_name])
    return df

# `parse_date_column()` converts a selected DataFrame column into datetime
# format, making it suitable for time-series analysis.


def calculate_log_returns(prices):
    """
    Calculate logarithmic returns from a price series.

    Parameters
    ----------
    prices : pandas.Series
        Series containing asset prices.

    Returns
    -------
    pandas.Series
        Logarithmic returns.
    """
    return np.log(prices / prices.shift(1))
#`calculate_log_returns()` calculates logarithmic returns, which are commonly
# used in financial analysis.