import numpy as np

def filter_store(df, store_id):
    return (
        df[df["store_id"] == store_id]
        .set_index("date")
        .sort_index()
    )

def weekly_aggregate(df):
    return df["sales"].resample("W").sum()

def train_test_split_ts(series, train_ratio=0.8):
    split = int(len(series) * train_ratio)
    return series.iloc[:split], series.iloc[split:]

def create_sequences(data, window_size):
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)
