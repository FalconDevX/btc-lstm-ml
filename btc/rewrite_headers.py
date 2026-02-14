import polars as pl
import os

path = "/BTCUSDT/BTCUSDT-1m.parquet"
temp_path = "/BTCUSDT/BTCUSDT-1m.parquet.tmp"

df = pl.read_parquet(path)

df = df.rename({
    "column_1": "open_time",
    "column_2": "open",
    "column_3": "high",
    "column_4": "low",
    "column_5": "close",
    "column_6": "volume",
    "column_7": "close_time",
})

df.write_parquet(temp_path)

os.replace(temp_path, path)

