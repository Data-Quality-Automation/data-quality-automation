import pandas as pd
import pytest
from logic.aum_calculator import calculate_aum, aggregate_aum
from config.settings import AUM_TOLERANCE

@pytest.mark.parametrize(
    "row",
    pd.read_csv("data/test_cases_aum.csv").to_dict("records")
)
def test_aum_calculation_data_driven(row):
    df = pd.DataFrame([{
        "units": row["units"],
        "nav": row["nav"],
        "fx_rate": row["fx_rate"]
    }])

    df = calculate_aum(df)
    actual = aggregate_aum(df, row["period"])

    assert abs(actual - row["expected_aum"]) <= AUM_TOLERANCE
