import pandas as pd

def calculate_aum(df: pd.DataFrame) -> pd.DataFrame:
    if (df["fx_rate"] <= 0).any():
        raise ValueError("FX rate must be positive")

    df["aum"] = (df["units"] * df["nav"] * df["fx_rate"]).round(2)
    return df


def aggregate_aum(df: pd.DataFrame, period: str) -> float:
    if period in ["DAILY", "MTD", "YTD", "YEARLY"]:
        return df["aum"].sum()
    raise ValueError("Invalid period")
