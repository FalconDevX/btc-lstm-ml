import polars as pl
import plotly.graph_objects as go

df_btc = (
    pl.read_parquet("BTCUSDT/BTCUSDT-1d-closed.parquet")
    .with_columns(pl.col("close").cast(pl.Float64))
    .sort("date")
)

df_nasdaq = (
    pl.read_parquet("NASDAQ/NASDAQ-1d-closed.parquet")
    .with_columns(pl.col("close").cast(pl.Float64))
    .sort("date")
)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_btc["date"].to_list(),
    y=df_btc["close"].to_list(),
    mode='lines',
    name='BTC Price',
    line=dict(color='#F7931A', width=2)
))

fig.add_trace(go.Scatter(
    x=df_nasdaq["date"].to_list(),
    y=df_nasdaq["close"].to_list(),
    mode='lines',
    name='NASDAQ Price',
    line=dict(color='#00FF00', width=2)
))

fig.update_layout(
    title='Kurs BTC/USDT (Dzienny)',
    xaxis_title='Data',
    yaxis_title='Cena (USDT)',
    template='plotly_dark',
    xaxis=dict(
        rangeslider=dict(visible=True),
        type='date'
    )
)

fig.show()
