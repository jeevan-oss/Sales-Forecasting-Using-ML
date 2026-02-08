import pandas as pd

def load_store_daily_sales(path="../data/processed/store_daily_sales.csv"):
    return pd.read_csv(path, parse_dates=["date"])
