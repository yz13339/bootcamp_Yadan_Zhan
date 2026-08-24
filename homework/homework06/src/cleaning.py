"""Reusable DataFrame cleaning functions for Homework 06."""

from collections.abc import Sequence

import pandas as pd
from pandas.api.types import is_numeric_dtype


def _resolve_numeric_columns(
    df: pd.DataFrame, columns: Sequence[str] | None
) -> list[str]:
    """Validate and return numeric columns selected for a transformation."""
    selected = list(df.select_dtypes(include="number").columns) if columns is None else list(columns)
    missing = [column for column in selected if column not in df.columns]
    if missing:
        raise KeyError(f"Columns not found: {missing}")

    non_numeric = [column for column in selected if not is_numeric_dtype(df[column])]
    if non_numeric:
        raise TypeError(f"Columns must be numeric: {non_numeric}")
    return selected


def fill_missing_median(
    df: pd.DataFrame, columns: Sequence[str] | None = None
) -> pd.DataFrame:
    """Return a copy with missing values in selected numeric columns median-filled.

    If ``columns`` is omitted, all numeric columns are selected. A column whose
    values are all missing cannot have a median calculated and remains missing.
    """
    result = df.copy()
    selected = _resolve_numeric_columns(result, columns)
    if selected:
        result[selected] = result[selected].fillna(result[selected].median())
    return result


def drop_missing(
    df: pd.DataFrame, subset: Sequence[str] | None = None
) -> pd.DataFrame:
    """Return a copy with rows containing missing values removed.

    ``subset`` limits the required fields; when omitted, every column is
    required. The original index is retained for traceability.
    """
    if subset is not None:
        missing = [column for column in subset if column not in df.columns]
        if missing:
            raise KeyError(f"Columns not found: {missing}")
    return df.dropna(subset=subset).copy()


def normalize_data(
    df: pd.DataFrame, columns: Sequence[str] | None = None
) -> pd.DataFrame:
    """Return a copy with selected numeric columns min-max scaled to [0, 1].

    Constant non-null columns are mapped to 0.0 because they contain no
    relative variation. Missing values remain missing.
    """
    result = df.copy()
    selected = _resolve_numeric_columns(result, columns)
    for column in selected:
        minimum = result[column].min()
        span = result[column].max() - minimum
        result[column] = 0.0 if pd.notna(span) and span == 0 else (result[column] - minimum) / span
    return result
