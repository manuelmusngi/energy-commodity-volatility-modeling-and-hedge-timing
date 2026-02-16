def storage_surprise(df):
    df["storage_change"] = df["storage"].diff(7)
    df["storage_surprise"] = (
        df["storage_change"] -
        df["storage_change"].rolling(5 * 52).mean()
    )
    return df
