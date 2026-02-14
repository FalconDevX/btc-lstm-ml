import pandas as pd

df_btc_1d = pd.read_parquet("BTCUSDT/BTCUSDT-1d.parquet")

df_btc_1d['open_time'] = pd.to_numeric(df_btc_1d['open_time'], errors='coerce')

mask_us = df_btc_1d['open_time'] > 10**14
df_btc_1d.loc[mask_us, 'open_time'] = df_btc_1d.loc[mask_us, 'open_time'] // 1000

df_btc_1d['open_time'] = df_btc_1d['open_time'].astype('int64')

df_btc_1d = df_btc_1d.sort_values("open_time")

df_btc_1d['date'] = pd.to_datetime(df_btc_1d['open_time'], unit='ms')

(
    df_btc_1d[["date", "close"]]
    .drop_duplicates(subset=["date"])
    .to_parquet("BTCUSDT/BTCUSDT-1d-closed.parquet", index=False)
)

print("Konwersja zakończona sukcesem!")
