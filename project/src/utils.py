def clean_column_names(df):
    """
    Return a copy of a DataFrame with standardized column names.
    """
    cleaned_df = df.copy()
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return cleaned_df