import numpy as np
import pandas as pd


def add_zscore(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of df with a Z column computed as BETA / SE."""
    if not {"BETA", "SE"} <= set(df.columns):
        raise ValueError("sumstats must contain BETA and SE columns")
    out = df.copy()
    out["Z"] = out["BETA"] / out["SE"]
    out.loc[~np.isfinite(out["Z"]), "Z"] = np.nan
    return out
