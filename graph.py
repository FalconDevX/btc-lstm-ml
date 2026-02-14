import polars as pl
import plotly.graph_objects as go

df = pl.read_parquet("/BTCUSDT/BTCUSDT-1h.parquet")

df = df.with_columns(
    pl.col("open_time")
    .cast(pl.Int64)
    .cast(pl.Datetime("ms"))
).sort("open_time")

fig = go.Figure(go.Candlestick(
    x=df["open_time"],
    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"]
))


fig.show()
