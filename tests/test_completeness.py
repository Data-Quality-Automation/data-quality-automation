from db.db_utils import fetch_df

def test_layer_record_counts():
    landing = fetch_df("SELECT COUNT(*) cnt FROM landing_fund")["cnt"][0]
    mart = fetch_df("SELECT COUNT(*) cnt FROM mart_fund")["cnt"][0]
    final = fetch_df("SELECT COUNT(*) cnt FROM final_fund")["cnt"][0]

    assert mart <= landing
    assert final <= mart


def test_missing_funds_in_mart():
    df = fetch_df("""
        SELECT DISTINCT fund_id
        FROM landing_fund
        WHERE fund_id NOT IN (
            SELECT DISTINCT fund_id FROM mart_fund
        )
    """)
    assert df.empty
