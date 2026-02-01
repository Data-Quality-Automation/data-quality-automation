import pandas as pd
from db.db_utils import fetch_df

def test_true_duplicates_removed():
    """
    Validate that true duplicates are removed from the Mart layer.
    Duplicates are defined as rows with the same fund_id and trade_date.
    """
    df = fetch_df("""
        SELECT fund_id, trade_date, COUNT(*) as cnt
        FROM mart_fund
        GROUP BY fund_id, trade_date
        HAVING COUNT(*) > 1
    """)
    assert df.empty, "Duplicate records found in Mart layer!"


def test_fund_id_mapping():
    """
    Validate that all fund_ids in Mart are correctly mapped according to fund_id_mapping.csv.
    This ensures the Source → Mart → Final pipeline uses normalized IDs.
    """
    # Load expected mappings from CSV
    mapping = pd.read_csv("data/fund_id_mapping.csv")
    valid_ids = mapping["mapped_fund_id"].astype(str).tolist()

    # Fetch unique fund_ids from Mart
    mart_funds = fetch_df("SELECT DISTINCT fund_id FROM mart_fund")["fund_id"].astype(str).tolist()

    # Assert that all Mart fund IDs exist in mapping
    invalid_ids = [fid for fid in mart_funds if fid not in valid_ids]
    assert not invalid_ids, f"Unexpected fund_ids in Mart layer: {invalid_ids}"
