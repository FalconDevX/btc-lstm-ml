import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df_btc = pd.read_parquet("BTCUSDT/BTCUSDT-1d-closed.parquet")
# #removing weekends
# df_btc = df_btc[df_btc["date"].dt.dayofweek < 5]

# df_btc.to_parquet("BTCUSDT/BTCUSDT-1d-closed-nowknd.parquet", index=False)

df_btc = pd.read_parquet("BTCUSDT/BTCUSDT-1d-closed-nowknd.parquet")
df_nasdaq = pd.read_parquet("NASDAQ/NASDAQ-1d-closed.parquet")

df_btc["date"] = pd.to_datetime(df_btc["date"])
df_nasdaq["date"] = pd.to_datetime(df_nasdaq["date"])

df_btc = df_btc.rename(columns={"close": "close_btc"})
df_nasdaq = df_nasdaq.rename(columns={"close": "close_nasdaq"})

df_btc["close_btc"] = pd.to_numeric(df_btc["close_btc"], errors="coerce")
df_nasdaq["close_nasdaq"] = pd.to_numeric(df_nasdaq["close_nasdaq"], errors="coerce")

df = df_btc.merge(df_nasdaq, on="date", how="inner")

df = df.sort_values("date")

# log returns
df["btc_log_ret"] = np.log(df["close_btc"]).diff()
df["nasdaq_log_ret"] = np.log(df["close_nasdaq"]).diff()

df = df.drop(columns=["_index_level_0_"], errors="ignore")

df = df.dropna(subset=["btc_log_ret", "nasdaq_log_ret"])

df = df.reset_index(drop=True)

df.to_parquet("DATA/merged-btc-nasdaq.parquet")

corr = df["btc_log_ret"].corr(df["nasdaq_log_ret"])
print("Correlation:", corr)

df_2020 = df[df["date"] >= "2024-01-01"]

corr = df_2020["btc_log_ret"].corr(df_2020["nasdaq_log_ret"])
print("Correlation from 2024:", corr)

#wykres log return btc i nasdaq
plt.plot(df["date"], df["btc_log_ret"], label="BTC")
plt.plot(df["date"], df["nasdaq_log_ret"], label="NASDAQ")
plt.legend()
plt.show()