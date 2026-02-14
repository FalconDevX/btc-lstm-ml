import zipfile
from datetime import date, timedelta
from tqdm import tqdm

start = date(2017, 8, 17)
end   = date(2026, 2, 12)

total_days = (end - start).days + 1
day = start

for _ in tqdm(range(total_days)):
    name = f"BTCUSDT-1m-{day}.zip"

    path_to_zip_file = f"data/{name}"
    directory_to_extract_to = "data_extracted"

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

    day += timedelta(days=1)