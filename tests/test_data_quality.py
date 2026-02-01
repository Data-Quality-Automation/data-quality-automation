from db.db_utils import fetch_df

def test_no_nulls_or_invalid_ranges():
    df = fetch_df("""
        SELECT COUNT(*) cnt
        FROM mart_fund
        WHERE nav IS NULL
           OR nav <= 0
           OR units < 0
    """)
    assert df["cnt"][0] == 0
