import requests
from datetime import date, timedelta
from tqdm import tqdm

start = date(2017, 8, 17)
end   = date(2026, 2, 12)

total_days = (end - start).days + 1
day = start

for _ in tqdm(range(total_days)):
    
    name = f"BTCUSDT-1m-{day}.zip"
    url  = f"https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/{name}"

    r = requests.get(url)

    if r.status_code == 200:
        with open(f"data/{name}", "wb") as f:
            f.write(r.content)
    else:
        print("Brak:", name)

    day += timedelta(days=1)