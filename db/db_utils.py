import sqlite3
import pandas as pd
from config.settings import DB_NAME

def fetch_df(query: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql(query, conn)
    conn.close()
    return df
