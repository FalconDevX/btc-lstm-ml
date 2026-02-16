import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_btc = pd.read_parquet("PARQUET/BTCUSDT-1d.parquet")
df_btc["open_time"] = pd.to_numeric(df_btc["open_time"], errors="coerce")
df_btc["date"] = pd.to_datetime(df_btc["open_time"], unit="ms")
df_btc = df_btc.sort_values("date")
df_btc["close"] = pd.to_numeric(df_btc["close"], errors="coerce")

btc_monthly = df_btc.set_index("date")["close"].resample("ME").last()
btc_monthly_ret = np.log(btc_monthly).diff().dropna()
btc_monthly_ret = btc_monthly_ret.to_frame(name="btc_log_ret")

df_infl = pd.read_parquet("PARQUET/T10YIE.parquet")
df_infl["date"] = pd.to_datetime(df_infl.iloc[:, 0])
df_infl["CPI"] = pd.to_numeric(df_infl.iloc[:, 1], errors="coerce")
df_infl = df_infl.set_index("date").resample("ME").last()
df_infl["cpi_change"] = df_infl["CPI"].diff()
df_infl = df_infl[["cpi_change"]].dropna()

df_monthly = btc_monthly_ret.merge(df_infl, left_index=True, right_index=True, how="inner")
corr = df_monthly["btc_log_ret"].corr(df_monthly["cpi_change"])
print("Miesięczna korelacja BTC vs zmiana inflacji:", corr)
df_monthly["rolling_corr"] = df_monthly["btc_log_ret"].rolling(6).corr(df_monthly["cpi_change"])

plt.figure(figsize=(12,6))
plt.plot(df_monthly.index, df_monthly["rolling_corr"])
plt.axhline(0, linestyle="--")
plt.title("6-miesięczna rolling correlation: BTC vs zmiana inflacji")
plt.xlabel("Date")
plt.ylabel("Correlation")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()