# import yfinance as yf
# import os

# ticker = "^IXIC"

# os.makedirs("NASDAQ", exist_ok=True)

# data = yf.download(
#     ticker,
#     start="2017-08-17",
#     end="2026-02-12",
#     interval="1d",
#     auto_adjust=False,
#     progress=False
# )

# if hasattr(data.columns, "levels"):
#     data.columns = data.columns.get_level_values(0)

# data.to_parquet("NASDAQ/NASDAQ-1d.parquet")

import pandas as pd

nasdaq = pd.read_parquet("NASDAQ/NASDAQ-1d.parquet")

nasdaq = nasdaq.reset_index()

if hasattr(nasdaq.columns, "levels"):
    nasdaq.columns = nasdaq.columns.get_level_values(0)

nasdaq = nasdaq.rename(columns={
    "Date": "date",
    "Close": "close"
})

nasdaq = nasdaq[["date", "close"]]

nasdaq = nasdaq.sort_values("date")

nasdaq.to_parquet("NASDAQ/NASDAQ-close.parquet")




